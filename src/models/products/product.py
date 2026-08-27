from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Numeric,
    String,
    Text,
    CheckConstraint,
    Integer,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.database.db import Base
from src.models.time_stamps import TimeStampMixin


# Products table
class Product(TimeStampMixin, Base):
    __tablename__ = "products"

    # Product id
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
    )
    # Product name
    name: Mapped[str] = mapped_column(
        String(128), 
        nullable=False
    )
    # Product price
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), 
        nullable=False
    )
    # Product description
    description: Mapped[str | None] = mapped_column(
        Text, 
        nullable=True
    )
    # Product slug
    slug: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
        unique=True,
    )
    # Product status
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )


    # Categories relationship
    categories: Mapped[list["ProductCategory"]] = relationship(
        secondary="product_categories",
        back_populates="products",
    )


    # Table constraints
    __table_args__ = (
        CheckConstraint("price > 0", name="ck_product_price_positive")
    )
