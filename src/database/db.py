# Async dependencies
from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    create_async_engine, 
    async_sessionmaker,
)

# Base
from sqlalchemy.orm import (
    DeclarativeBase
)

from src.core.settings import settings

# Database connection URL
DB_URL = f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

# Session pool
engine = create_async_engine(url=DB_URL)

# Sessionmaker
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession ,expire_on_commit=False)

# Base class for enheritance
class Base(DeclarativeBase):
    pass

# Session generator getter
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
