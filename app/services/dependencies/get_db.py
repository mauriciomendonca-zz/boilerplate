from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
import app.config.config as envConfig

SQLALCHEMY_DATABASE_URL = str(envConfig.DATABASE_URL)


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
