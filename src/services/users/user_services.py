# User's repository
from src.repositories.users.user_repository import UserRepository
from fastapi import (
    status, 
    HTTPException
)

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.database.db import get_db


from src.schemas.users.user import UserCreate


# User's services
class UserService:
    def __init__(self, db: Annotated[AsyncSession, Depends(get_db)]):
            self.db = db

    # Returns one concrete user
    async def get_user_by_id(self, id: int):
        user = UserRepository.get_by_id(id)

        # Check if user with given ID exists
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User with this ID not found"
            )
        return user

    # Returns all users
    async def get_all_users(self):
        users = UserRepository.get_all()

        # Check if users exists
        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User with this ID not found"
            )
        return users

    # Add user handle
    async def create_user(self, user: UserCreate):
        # Check if this email already taken
        if UserRepository.get_by_email(user.email) is not None:
            raise HTTPException(
                 status_code=status.HTTP_400_BAD_REQUEST,
                 detail="This email is already taken"
                 )
        # Check if this username is already taken
        if UserRepository.get_by_username(user.username) is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This username is already taken"
                )
        UserRepository.add(user)

        # Session commit and refresh new user instance
        await self.db.commit()
        await self.db.refresh(user)
