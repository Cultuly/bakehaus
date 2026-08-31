# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    Field,
)
# Price type context dependencies
from decimal import Decimal
# Time context dependencies
from datetime import datetime


# Category creation schema (POST)
class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=64)
    #parent_id: int | None
    is_active: bool = True


# Category update schema (PUT/PATCH)
class CategoryUpdate(BaseModel):
    name: int | None
    #parent_id: int | None
    is_active: bool | None

# Category response schema (GET)
class CategoryResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    name: str
    is_active: bool