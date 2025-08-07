import asyncio
import logging

from broker import rabbit_broker
from config import chat_settings
from src.client import async_client

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("Starting a chat")

    models = await async_client.list()
    model_exists = chat_settings.MODEL in models

    logger.info(f"Model `{chat_settings.MODEL}` existence: {model_exists}")

    if not model_exists:
        logger.info(f"Pulling a model `{chat_settings.MODEL}`")

        await async_client.pull(chat_settings.MODEL)

        logger.info(f"Model `{chat_settings.MODEL}` has been pulled")

    async with rabbit_broker as broker:
        logger.info("Chat broker initialization")

        await broker.start()

        await asyncio.Event().wait()

        logger.info("Chat broker has been stopped")

    logger.info("Chat has been stopped")


if __name__ == "__main__":
    asyncio.run(main())
