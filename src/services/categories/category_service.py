# Exceptions dependencies
from fastapi import (
    status, 
    HTTPException
)
# SQL dependencies
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.categories.category_repository import CategoryRepository
# Schemas
from src.schemas.categories.category import CategoryCreate
# Models
from src.models.categories import category as models


# Category service
class CategoryService:
    def __init__(self, db: AsyncSession, category_repo: CategoryRepository):
        self.db = db
        self.category_repo = category_repo

    # Returns category by it's id
    async def get_category_by_id(self, id: int) -> models.Category:
        category = await self.category_repo.get_by_id(id=id)

        # Check if category with this id exists
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category with this id is not found"
                )
        
        return category

    # Returns category by it's name
    async def get_category_by_name(self, name: str) -> models.Category:
        category = await self.category_repo.get_by_name(name=name)

        # Check if category with this name exists
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category with this name not found"
            )

        return category

    # Returns all categories
    async def get_all_categories(self) -> list[models.Category] | list:
        categories = await self.category_repo.get_all()

        # Check if categories exists
        if not categories:
            return []
        return categories

    # Creates new category
    async def create_category(self, category_data: CategoryCreate) -> models.Category:
        # Check if category with this name already exists
        if await self.category_repo.get_by_name(category_data.name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category with this name already exists"
            )

        # New category object
        new_category = await self.category_repo.add(category=category_data)

        # Session commit and refresh new_category object
        await self.db.commit()
        await self.db.refresh(new_category)

        # Returns new category object        
        return new_category