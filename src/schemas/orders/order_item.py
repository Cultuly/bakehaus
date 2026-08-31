# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    model_validator,
)
# Price type context dependencies
from decimal import Decimal
# Time context dependencies
from datetime import datetime


# Order item update schema (PUT/PATCH)
class OrderItemUpdate(BaseModel):
    product_id: int | None
    quantity: int | None

    # Quantity check
    @model_validator(mode='after')
    def check_quantity(self) -> "OrderItemUpdate":
        if self.product_id is not None and self.quantity is None:
            raise ValueError("Quantity is required when product is providing")
        return self

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
