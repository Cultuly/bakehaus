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


# Product creation schema (POST)
class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=32)
    price: Decimal = Field(gt=0, decimal_places=2)
    descriprion: str = Field(None, min_length=1, max_length=1000)
    #slug: str = Field(None, min_length=1, max_length=255)
    is_active: bool = True
    category_ids: list[int] = Field(default_factory=list)


# Product update schema (PUT/PATCH)
class ProductUpdate(BaseModel):
    name: str | None = Field(min_length=1, max_length=32)
    price: Decimal | None = Field(gt=0, decimal_places=2)
    descriprion: str | None = Field(None, min_length=1, max_length=1000)
    #slug: str | None = Field(None, min_length=1, max_length=255)
    is_active: bool | None
    category_ids: list[int] | None = Field(default_factory=list)


# Product response schema (GET)
class ProductResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    name: str
    price: Decimal
    descriprion: str
    #slug: str
    is_active: bool
    category_ids: list[int]
    created_at: datetime
    updated_at: datetime | None
