import logging
from typing import Sequence
from uuid import UUID

from sqlalchemy import exists, select

from broker import rabbit_broker
from src.database import async_session
from src.models import Query, Session

logger = logging.getLogger(__name__)


@rabbit_broker.subscriber("to_create_session")
async def create_session() -> UUID:
    logger.info("Creating a session")

    async with async_session() as session:
        session_obj = Session()
        session.add(session_obj)
        await session.commit()

    logger.info(f"Session `{session_obj.id}` has been created")

    return session_obj.id


@rabbit_broker.subscriber("to_session_exists")
async def session_exists(session_id: UUID) -> bool:
    logger.info(f"Checking if session `{session_id}` exists")

    async with async_session() as session:
        query = select(exists().where(Session.id == session_id))
        result = await session.execute(query)
        value = bool(result.scalar())

    logger.info(f"Session `{session_id}` existence: {value}")

    return value


@rabbit_broker.subscriber("to_create_query")
async def create_query(session_id: UUID, message: str, answer: str) -> int:
    logger.info(f"Creating a query in session `{session_id}`")

    async with async_session() as session:
        query_obj = Query(session_id=session_id, message=message, answer=answer)
        session.add(query_obj)
        await session.commit()

    logger.info(f"Query `{query_obj.id}` has been created")

    return query_obj.id


@rabbit_broker.subscriber("to_get_queries_from_session")
async def get_queries_from_session(session_id: UUID) -> Sequence[tuple[str, str]]:
    logger.info(f"Retrieving queries from session `{session_id}`")

    async with async_session() as session:
        query = (
            select(Query.message, Query.answer)
            .where(Query.session_id == session_id)
            .order_by(Query.created_at)
        )
        result = await session.execute(query)
        data: list[tuple[str, str]] = [tuple(row) for row in result.all()]

    logger.info(f"Queries have been received: `{len(data)}`")

    return data
