# Fastapi dependencies
from fastapi import APIRouter
# Users service
from src.services.users.user_services import UserService
from src.schemas.users.user import UserCreate, UserResponse

from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_db


# User router
router = APIRouter()

# Returns concrete user by his ID
@router.get('/users/{user_id}', response_model=UserResponse)
async def get_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]) -> UserResponse:
    return UserService(db).get_user(id=user_id)

# Returns all users
@router.get('/users', response_model=list[UserResponse])
async def get_users(db: Annotated[AsyncSession, Depends(get_db)]) -> list[UserResponse]:
    return UserService(db).get_all_users()

# Creates new user
@router.post('/users', response_model=UserResponse)
async def create_user(user_data: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]) -> UserResponse:
    new_user = await UserService(db).create_user(user_data=user_data)
    return new_user
