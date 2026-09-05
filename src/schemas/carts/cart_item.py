# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    Field,
)
# Time context dependencies
from datetime import datetime


# Cart item update schema (PUT/PATCH)(soon)
class CartItemUpdate(BaseModel):
    product_id: int | None = None
    quantity: int | None = Field(default=None, gt=0)

# Cart item response schema (GET)
class CartItemResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    product_id: int | None
    quantity: int
    created_at: datetime
    updated_at: datetime | None
