import asyncio
import logging

from broker import rabbit_broker
from src.base import Base
from src.database import async_engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("Starting a database")

    logger.info("Database initialization")

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Database has been initialized")

    async with rabbit_broker as broker:
        logger.info("Database broker initialization")

        await broker.start()

        await asyncio.Event().wait()

        logger.info("Database broker has been stopped")

    logger.info("Database has been stopped")


if __name__ == "__main__":
    asyncio.run(main())
