# Type checking dependencies
from typing import Annotated
from fastapi import Depends
from src.database.db import get_db
# SQL dependencies
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Models
import src.models.categories.category as models
from src.schemas.categories.category import CategoryCreate


# Category repository
class CategoryRepository():
    def __init__(self, db: AsyncSession):
        self.db = db

    # Returns concrete category by it's id
    async def get_by_id(self, id: int) -> models.Category:
        # SQL querry
        querry = select(models.Category).where(models.Category.id == id)
        result = await self.db.execute(querry)

        # Category object
        category = result.scalars().one_or_none()

        return category

    # Returns all categories
    async def get_all(self) -> list[models.Category]:
        # SQL querry
        querry = select(models.Category)
        result = await self.db.execute(querry)

        # List of categories objects
        categories = result.scalars().all()

        return categories

    # Returns concrete category by it's name
    async def get_by_name(self, name: str) -> models.Category:
        # SQL querry
        querry = select(models.Category).where(models.Category.name == name)
        result = await self.db.execute(querry)

        # Category object
        category = result.scalars().first()

        return category

    # Add new category to database
    async def add(self, category: CategoryCreate) -> models.Category:
        # New category creation
        new_category = models.Category(
            name = category.name
        )

        # Addition to database
        self.db.add(new_category)

        # Returns created category object
        return new_category
