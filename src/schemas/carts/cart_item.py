# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
)
# Time context dependencies
from datetime import datetime


# Cart item update schema (PUT/PATCH)(soon)
class CartItemUpdate(BaseModel):
    product_id: int | None
    quantity: int | None

# Cart item response schema (GET)
class CartItemResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    product_id: int
    quantity: int
    created_at: datetime
    updated_at: datetime | None
