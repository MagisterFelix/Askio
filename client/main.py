import logging

import gradio as gr

from config import client_settings
from src.api import get_history
from src.chat import send_message
from src.session import session

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Starting a client")

    logger.info("Building an app")

    with gr.Blocks(
        title="Askio",
        fill_height=True,
        fill_width=True,
        theme="soft",
        css="""
            * {
                scrollbar-width: none !important;
                -ms-overflow-style: none !important;
            }
            *::-webkit-scrollbar {
                display: none !important;
            }
            .message-buttons-left {
                display: none !important;
            }
            .progress-text {
                display: none !important;
            }
            footer {
                display: none !important;
            }
            """,
    ) as app:
        chat = gr.ChatInterface(
            fn=send_message,
            type="messages",
            chatbot=gr.Chatbot(
                value=get_history,
                type="messages",
                label="Assistant",
                placeholder="<center><strong>Welcome!</strong><br>Send a message to get started!</center>",
                scale=1,
            ),
            title="Askio",
            description="<center>Askio is an ultra-simple chat assistant that delivers instant answers to your queries</center>",
            stop_btn=False,
        )
        chat.chatbot.clear(fn=session.clear_data)

    logger.info("App has been built")

    app.launch(server_name=client_settings.HOST, server_port=client_settings.PORT)

    logger.info("Client has been stopped")


if __name__ == "__main__":
    main()
