# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    Field,
    UUID4,
    model_validator,
)
# Price type context dependencies
from decimal import Decimal
# Time context dependencies
from datetime import datetime
# Order statuses
from src.models.orders.order_status import OrderStatus
from src.models.orders.order_payment_status import OrderPaymentStatus
# Order items
from src.schemas.orders.order_item import OrderItemResponse, OrderItemCreate, OrderItemUpdate
from src.schemas.users.user import UserResponse
from src.models.orders.delivery_type import DeliveryType


# Order creation schema (POST)
class OrderCreate(BaseModel):
    items: list[OrderItemCreate] = Field(min_length=1)
    delivery_type: DeliveryType = DeliveryType.PICKUP # Pickup delivery status by default
    commentary: str | None = Field(default=None, max_length=1000)
    delivery_address: str | None = Field(default=None, min_length=1, max_length=255)
    delivery_time: datetime | None = None

    # Delivery fields validator
    @model_validator(mode='after')
    def validate_delivery_fields(self):
        if self.delivery_type == DeliveryType.DELIVERY:
            if self.delivery_address is None:
                raise ValueError("Delivery address is required for delivery")
            if self.delivery_time is None:
                raise ValueError("Delivery time is required for delivery")

        return self


# Order update schema (PUT/PATCH) (in progress)
class OrderUpdate(BaseModel):
    items: list[OrderItemUpdate] | None = None
    delivery_type: DeliveryType | None = None
    delivery_address: str | None = None
    delivery_time: datetime | None = None


# Order update schema for admins (PUT/PATCH) (soon)
#class OrderAdminUpdate(OrderUpdate):
#    total_price: Decimal | None = None
#    status: OrderStatus | None = None
#    payment_status: OrderPaymentStatus | None = None


# Order response schema (GET)
class OrderResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True, use_enum_values=True)

    id: UUID4
    user: UserResponse
    items: list[OrderItemResponse]
    commentary: str | None = None
    total_price: Decimal
    status: OrderStatus
    payment_status: OrderPaymentStatus
    delivery_type: DeliveryType
    delivery_address: str | None = None
    delivery_time: datetime | None = None
    created_at: datetime
    updated_at: datetime | None = None
