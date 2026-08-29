from decimal import Decimal
from uuid import UUID

from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Uuid,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.database.db import Base
from src.models.time_stamps import TimeStampMixin

from typing import Optional


# Order items
class OrderItem(TimeStampMixin, Base):
    __tablename__ = "order_items"

    # Record id
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Record's order id
    order_id: Mapped[UUID] = mapped_column(
        Uuid, 
        ForeignKey("orders.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    # Product id
    product_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("products.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )
    # Product name
    product_name: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )
    # Items quantity
    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )
    # Price snapshot
    price_snapshot: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )


    # Order relationship
    order: Mapped["Order"] = relationship(
        back_populates="items",
    )
    # Product relationship
    product: Mapped[Optional["Product"]] = relationship()


    # Table constraints
    __table_args__ = (
        CheckConstraint("quantity > 0", name="ck_order_items_quantity_positive"),
        UniqueConstraint("order_id", "product_id", name="uq_order_product"),
    )
