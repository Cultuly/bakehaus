# Context dependencies
from src.services.users.user_services import UserService
from src.services.categories.category_service import CategoryService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import Depends
from src.database.db import get_db
from src.repositories.users.user_repository import UserRepository
from src.repositories.categories.category_repository import CategoryRepository


# User services factory
def get_user_service(db: Annotated[AsyncSession, Depends(get_db)]) -> UserService:
    # User repository instance creation
    user_repo = UserRepository(db=db)

    # Returns UserService instance
    return UserService(db=db, user_repo=user_repo)

# Category services factory
def get_category_service(db: Annotated[AsyncSession, Depends(get_db)]) -> CategoryRepository:
    # Category repository instance creation
    category_repo = CategoryRepository(db=db)

    # Returns CategoryRepository instance
    return CategoryService(db=db, category_repo=category_repo)
