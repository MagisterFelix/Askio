import json
import logging
from uuid import UUID

from fastapi import APIRouter, Form, HTTPException, Query

from broker import rabbit_broker
from src.models import Message, Response

logger = logging.getLogger(__name__)


router = APIRouter()


async def session_exists(session_id: UUID) -> bool:
    async with rabbit_broker as broker:
        response = await broker.request(str(session_id), queue="to_session_exists")

    return bool(json.loads(response.body))


async def get_session_messages(session_id: UUID) -> list[Message]:
    async with rabbit_broker as broker:
        response = await broker.request(
            str(session_id), queue="to_get_queries_from_session"
        )

    queries: list[tuple[str, str]] = json.loads(response.body)

    messages: list[Message] = []
    for msg, ans in queries:
        messages.extend(
            (
                Message(role="user", content=msg),
                Message(role="assistant", content=ans),
            )
        )

    return messages


@router.get("/messages")
async def get_messages(session_id: UUID = Query()) -> list[Message]:
    logger.info(f"Retrieving messages from session `{session_id}`")

    if not await session_exists(session_id):
        raise HTTPException(status_code=404, detail="Session was not found")

    messages = await get_session_messages(session_id)

    logger.info(f"Retrieved messages from session `{session_id}`: {len(messages)}")

    return messages


@router.post("/messages")
async def send_message(
    session_id: UUID | None = Query(default=None), message: str = Form()
) -> Response:
    if session_id is None or not await session_exists(session_id):
        async with rabbit_broker as broker:
            response = await broker.request(queue="to_create_session")

        session_id = UUID(json.loads(response.body))

    logger.info(f"Sending a message to session `{session_id}`")

    messages = await get_session_messages(session_id)
    messages.append(Message(role="user", content=message))

    async with rabbit_broker as broker:
        response = await broker.request(messages, queue="to_generate_answer")
        answer: str = response.body.decode()

        await broker.publish(
            (str(session_id), message, answer), queue="to_create_query"
        )

    logger.info("Answer has been received")

    return Response(session_id=session_id, message=answer)
