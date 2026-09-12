# Type checking dependencies
from typing import Annotated
from fastapi import Depends
from src.database.db import get_db
# SQL dependencies
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Models
import src.models.users.user as models
from src.schemas.users.user import UserResponse
from src.schemas.users.user import UserCreate


# User repository class (access to users data in database)
class UserRepository:
    # Database session getter
    def __init__(self, db: Annotated[AsyncSession, Depends(get_db)]):
        self.db = db

    # Return user by ID
    async def get_by_id(self, id: int) -> UserResponse:
        # SQL querry
        querry = select(models.User).where(models.User.id == id)

        result = await self.db.execute(querry)
        # User object
        user = result.scalars().first()

        return user

    # Get concrete user by his email
    async def get_by_email(self, email: str) -> UserResponse:
        # SQL querry
        try:
            querry = select(models.User).where(models.User.email == email)
            result = await self.db.execute(querry)

            # User object
            user = result.scalars().first()
        except Exception:
            return None

        return user

    # Get concrete user by his username
    async def get_by_username(self, username: str) -> UserResponse:
        try:
            # SQL querry
            querry = select(models.User).where(models.User.username == username)
            result = await self.db.execute(querry)

            # User object
            user = result.scalars().first()
        except Exception:
            return None

        return user

    # Returns all users
    async def get_all(self) -> list[UserResponse]:
        # SQL querry
        querry = select(models.User)
        result = await self.db.execute(querry)

        # Users objects
        users = result.scalars().all()

        return users

    # Add user to database
    async def add(self, user: UserCreate):
        # New user creation
        new_user = models.User(
            username = user.username,
            email = user.email,
            phone = user.phone,
        )

        self.db.add(new_user)
