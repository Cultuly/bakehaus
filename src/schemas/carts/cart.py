# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    computed_field,
)
# Price type context dependencies
from decimal import Decimal
# Time context dependencies
from datetime import datetime

from src.schemas.users.user import UserResponse
from src.schemas.carts.cart_item import CartItemResponse


# Cart creation schema (POST)
class CartCreate(BaseModel):
    pass


# Cart update schema (PUT/PATCH) (soon)
#class CartUpdate(BaseModel):
#    pass


# Cart response schema (GET)
class CartResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    user: UserResponse
    items: list[CartItemResponse]
    total_price: Decimal
    created_at: datetime
    updated_at: datetime | None
