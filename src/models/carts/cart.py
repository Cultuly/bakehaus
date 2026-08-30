from datetime import datetime, timedelta, UTC
from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Uuid,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.database.db import Base
from src.models.time_stamps import TimeStampMixin


# Carts table
class Cart(TimeStampMixin, Base):
    __tablename__ = "carts"

    # Cart unique id
    id: Mapped[UUID] = mapped_column(
        Uuid, 
        default=uuid4,
        primary_key=True,
    )
    # Customer id (foreign key on users table)
    user_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False,
        index=True,
    )
    # Cart expiration time
    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), 
        nullable=True,
        default=lambda: datetime.now(UTC) + timedelta(days=14)
    )


    # Cart items
    items: Mapped[list["CartItem"]] = relationship(
        back_populates="cart",
        cascade="all, delete-orphan"
    )
    # Cart's owner (user) relationship
    user: Mapped["User"] = relationship(
        back_populates="carts",
    )


    # Cart's total price
    @property
    def total_price(self) -> Decimal:
        total = Decimal("0")
        for item in self.items:
            if item.product is not None and item.product.is_active:
                total += item.product.price * item.quantity

        return total