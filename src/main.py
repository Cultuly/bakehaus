# FastAPI dependencies
from fastapi import FastAPI
# Context dependencies
from contextlib import asynccontextmanager
# Models
import src.models
# Base class
from src.database.db import Base, engine
# User router
from src.api.v1.users.user_router import router as user_router
from src.api.v1.categories.categories_router import router as categories_router


# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    # Action on stopping app
    print("⚙️ Stopping app...")
    await engine.dispose()


# App init
app = FastAPI(lifespan=lifespan)

# Routers registry
app.include_router(user_router, tags=['Users'])
app.include_router(categories_router, tags=['Categories'])

# App's healthcheck
@app.get("/", include_in_schema=False)
def healthcheck():
    return {"detail": "work"}
