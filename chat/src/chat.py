import logging

from ollama import Message

from broker import rabbit_broker
from config import chat_settings
from src.client import async_client

logger = logging.getLogger(__name__)


@rabbit_broker.subscriber("to_generate_answer")
async def generate_answer(messages: list[Message]) -> str:
    logger.info("Generating response")

    response = await async_client.chat(model=chat_settings.MODEL, messages=messages)

    logger.info("Response has been generated")

    answer = (
        response.message.content
        if response.message.content
        else "Something went wrong..."
    )

    return answer
