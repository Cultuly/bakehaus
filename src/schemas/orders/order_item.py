# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    UUID4,
    Field,
)
# Price type context dependencies
from decimal import Decimal
# Time context dependencies
from datetime import datetime
# Product response schema
from src.schemas.products.product import ProductResponse


# Order item create schema (POST)
class OrderItemCreate(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


# Order item update schema (PUT/PATCH)
class OrderItemUpdate(BaseModel):
    id: int
    quantity: int | None = Field(default=None, gt=0)


# Order item response schema (GET)
class OrderItemResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    order_id: UUID4
    product_id: int
    quantity: int
    price_snapshot: Decimal
    product: ProductResponse | None
    created_at: datetime
    updated_at: datetime | None
