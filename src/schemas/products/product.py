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
#
from src.schemas.categories.category import CategoryResponse


# Product creation schema (POST)
class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=128)
    price: Decimal = Field(gt=0, decimal_places=2)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    #slug: str = Field(None, min_length=1, max_length=255)
    is_active: bool = True
    categories: list[CategoryResponse] = Field(default_factory=list)


# Product update schema (PUT/PATCH)
class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=32)
    price: Decimal | None = Field(default=None, gt=0, decimal_places=2)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    #slug: str | None = Field(default=None, min_length=1, max_length=255)
    categories: list[int] | None = Field(default=None, default_factory=list)
    is_active: bool | None = None


# Product response schema (GET)
class ProductResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    name: str
    price: Decimal
    description: str | None
    #slug: str
    is_active: bool
    categories: list[CategoryResponse]
    created_at: datetime
    updated_at: datetime | None
