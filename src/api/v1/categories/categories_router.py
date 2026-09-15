# Fastapi dependencies
from fastapi import APIRouter, status
# Users service
from src.services.categories.category_service import CategoryService 
from src.schemas.categories.category import CategoryCreate, CategoryResponse

from typing import Annotated
from fastapi import Depends
from src.core.factories import get_category_service


# User router
router = APIRouter()

# Returns all categories
@router.get("/categories", 
            response_model=list[CategoryResponse], 
            status_code=status.HTTP_200_OK)
async def get_categories(
    service: Annotated[CategoryService, Depends(get_category_service)]) -> list[CategoryResponse] | list:
    # Returns list of CategoryResponse object if exists, or empty list if not
    return await service.get_all_categories()

# Returns concrete category by it's id
@router.get("/categories/{category_id}", 
            response_model=CategoryResponse, 
            status_code=status.HTTP_200_OK)
async def get_category(category_id: int, 
                       service: Annotated[CategoryService, Depends(get_category_service)]) -> CategoryResponse:
    # Returns CategoryResponse object
    return await service.get_category_by_id(id=category_id)

# Create category
@router.post("/categories", 
             response_model=CategoryResponse, 
             status_code=status.HTTP_201_CREATED)
async def create_category(category_data: CategoryCreate, 
                          service: Annotated[CategoryService, Depends(get_category_service)]) -> CategoryResponse:
    # Add new category into database and returns it object
    new_category = await service.create_category(category_data=category_data)

    return new_category