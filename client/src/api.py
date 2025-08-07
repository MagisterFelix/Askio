import logging
from uuid import UUID

import requests
from gradio.components.chatbot import Message, MessageDict

from config import api_settings
from src.session import session

logger = logging.getLogger(__name__)


def get_history() -> list[MessageDict | Message]:
    session_id = session.get_id()

    if session_id is None:
        return []

    logger.info("Sending request to get history of messages")

    response = requests.get(
        f"{api_settings.URL}/messages",
        params={"session_id": str(session_id)},
    )

    logger.info(f"Response has been received, status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        session.set_messages(data)

        return data

    return []


def post_message(message: str) -> str:
    session_id = session.get_id()

    logger.info("Sending request to post a message")

    response = requests.post(
        f"{api_settings.URL}/messages",
        params={"session_id": str(session_id)} if session_id else None,
        data={"message": message},
    )

    logger.info(f"Response has been received, status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        session.set_id(UUID(data["session_id"]))

        return data["message"]

    return "Something went wrong..."
