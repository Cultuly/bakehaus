from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import (
    ForeignKey,
    Numeric,
    Text,
    Uuid,
    Enum,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.database.db import Base

# Models
from src.models.time_stamps import TimeStampMixin
from src.models.orders.order_status import OrderStatus
from src.models.orders.order_payment_status import OrderPaymentStatus


# Orders table
class Order(TimeStampMixin, Base):
    __tablename__ = "orders"

    # Order id
    id: Mapped[UUID] = mapped_column(
        Uuid, 
        primary_key=True, 
        default=uuid4,
    )
    # Customer id
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), 
        nullable=False, 
        index=True
    )
    # Order commetary (from customer)
    comment: Mapped[str | None] = mapped_column(
        Text, 
        nullable=True
    )
    # Order's total price
    total_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    # Order status
    status: Mapped[str] = mapped_column(
        Enum(OrderStatus),
        nullable=False,
        default=OrderStatus.PENDING,
        index=True,
    )
    # Order's payment status
    payment_status: Mapped[str] = mapped_column(
        Enum(OrderPaymentStatus),
        nullable=False,
        default=OrderPaymentStatus.UNPAID,
        index=True,
    )


    # Order content (relationship with pivot table)
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )


    # Calculates order's total price
    @property
    def calculated_total(self) -> Decimal:
        total = Decimal("0")
        for item in self.items:
            total += item.price_snapshot * item.quantity

        return total
    