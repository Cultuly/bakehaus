# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    Field,
    UUID4,
)
# Price type context dependencies
from decimal import Decimal
# Time context dependencies
from datetime import datetime
# Order statuses
from src.models.orders.order_status import OrderStatus
from src.models.orders.order_payment_status import OrderPaymentStatus
# Order items
from src.schemas.orders.order_item import OrderItemResponse
from src.schemas.users.user import UserResponse


# Order creation schema (POST)
class OrderCreate(BaseModel):
    commentary: str | None = Field(max_length=1000)
    delivery_address: str = Field(min_length=1, max_length=255)
    delivery_time: datetime


# Order update schema (PUT/PATCH) (in progress)
class OrderUpdate(BaseModel):
    #items: list[OrderItemResponse] | None
    total_price: Decimal | None
    status: OrderStatus | None
    payment_status: OrderPaymentStatus | None
    delivery_address: str | None
    delivery_time: datetime | None


# Order response schema (GET)
class OrderResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: UUID4
    user: UserResponse
    items: list[OrderItemResponse]
    total_price: Decimal
    status: str = OrderStatus
    payment_status: str = OrderPaymentStatus
    delivery_address: str
    delivery_time: datetime
    created_at: datetime
    updated_at: datetime | None
