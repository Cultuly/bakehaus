from uuid import UUID

from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Integer,
    UniqueConstraint,
    Uuid
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.database.db import Base
from src.models.time_stamps import TimeStampMixin


# Cart's content (items) table
class CartItem(TimeStampMixin, Base):
    __tablename__ = "cart_items"

    # Record id
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Cart id
    cart_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("carts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    # Cart item (product) id
    product_id: Mapped[int | None] = mapped_column(
        Integer, 
        ForeignKey("products.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    # Item (product) quantity
    quantity: Mapped[int] = mapped_column(
        Integer, 
        nullable=False, 
        default=1
    )

    
    # Product relationship
    product: Mapped["Product"] = relationship()
    # Cart relationship
    cart: Mapped["Cart"] = relationship(back_populates="items")


    # Table constraints
    __table_args__ = (
        UniqueConstraint("cart_id", "product_id", name="uq_cart_product"),
        CheckConstraint("quantity > 0", name="ck_cart_items_quantity_positive")
    )
