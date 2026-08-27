# Context dependencies
import os
from dotenv import load_dotenv

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


# Loading .env file
load_dotenv()

# Database config
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# Database connection URL
DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

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
