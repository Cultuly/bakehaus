# FastAPI dependencies
from fastapi import FastAPI

# Context dependencies
from contextlib import asynccontextmanager

# Models
import src.models

# Base class
from src.database.db import Base, engine


# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⚙️ Starting app...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    print("⚙️ Stopping app...")
    await engine.dispose()

# App init
app = FastAPI(lifespan=lifespan)


@app.get("/")
def healthcheck():
    return {"detail": "work"}
