# Exceptions dependencies
from fastapi import (
    status, 
    HTTPException
)
# SQL dependencies
from src.repositories.users.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
# Schemas
from src.schemas.users.user import UserCreate
# Models
from src.models.users import user as models


# User's services
class UserService:
    def __init__(self, db: AsyncSession, user_repo: UserRepository):
        self.db = db
        self.user_repo = user_repo

    # Returns one concrete user
    async def get_user(self, id: int) -> models.User:
        user = await self.user_repo.get_by_id(id=id)

        # Check if user with given ID exists
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User with this ID not found"
            )
        return user

    # Returns all users
    async def get_all_users(self) -> list[models.User] | list:
        users = await self.user_repo.get_all()

        # Return empty list if users not found
        if not users:
             users = []
        return users

    # Add user handle
    async def create_user(self, user_data: UserCreate) -> models.User:
        # Check if this email already taken
        if await self.user_repo.get_by_email(email=user_data.email) is not None:
            raise HTTPException(
                 status_code=status.HTTP_400_BAD_REQUEST, 
                 detail="This email is already taken"
                 )
        # Check if this username is already taken
        if await self.user_repo.get_by_username(username=user_data.username) is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This username is already taken"
                )
        
        # New user instance
        new_user = await self.user_repo.add(user=user_data)

        # Session commit and refresh new user instance
        await self.db.commit()
        await self.db.refresh(new_user)

        return new_user