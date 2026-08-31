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


# Order item update schema (PUT/PATCH)
class OrderItemUpdate(BaseModel):
    product_id: int | None

    # Change quantity only if product id is given
    if product_id is not None:
        quantity: int | None


# Order item response schema (GET)
class OrderItemResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    product_id: int
    product_name: str
    quantity: int
    price_snapshot: Decimal
    created_at: datetime
    updated_at: datetime | None
