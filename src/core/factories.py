# Context dependencies
from src.services.users.user_services import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import Depends
from src.database.db import get_db
from src.repositories.users.user_repository import UserRepository


# User services factory
def get_user_service(db: Annotated[AsyncSession, Depends(get_db)], 
                     user_repo: type[UserRepository] = UserRepository) -> UserService:
    # Returns UserService instance
    return UserService(db=db, user_repo=user_repo)