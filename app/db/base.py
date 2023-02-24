from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from app import config

# db initialization
DATABASE_URL = URL.create("postgresql+asyncpg",
                          username=config.USERNAME,
                          password=config.PASSWORD,
                          host=config.HOST,
                          port=config.PORT,
                          database=config.DATABASE)
engine = create_async_engine(url=DATABASE_URL, encoding="UTF-8", pool_pre_ping=True)
sm = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# FastAPI Dependency
async def get_session() -> AsyncSession:
    async with sm() as session:
        yield session
