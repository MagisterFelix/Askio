from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import db_settings

async_engine = create_async_engine(url=db_settings.URL)

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
