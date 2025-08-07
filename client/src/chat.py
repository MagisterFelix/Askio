import logging

from gradio import Error
from gradio.components.chatbot import Message, MessageDict

from src.api import post_message
from src.session import session

logger = logging.getLogger(__name__)


def send_message(message: str, history: list[MessageDict | Message]) -> str:
    if not message.strip():
        raise Error("Message cannot be empty!", print_exception=False)

    logger.info("Sending a message to chat")

    if not history:
        messages = session.get_messages()
        history.extend(messages)

    answer = post_message(message)

    logger.info("Answer has been sent to chat")

    session.add_messages(
        [
            MessageDict(role="user", content=message),
            MessageDict(role="assistant", content=answer),
        ]
    )

    return answer
