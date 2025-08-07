import asyncio
import logging

from uvicorn import Config, Server

from config import api_settings
from src.core import app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("Starting an API")

    config = Config(app=app, host=api_settings.HOST, port=api_settings.PORT)
    server = Server(config=config)

    await server.serve()

    logger.info("API has been stopped")


if __name__ == "__main__":
    asyncio.run(main())
