from sqlalchemy import (
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.database.db import Base
from src.models.time_stamps import TimeStampMixin


# Product categories (pivot table)
class ProductCategory(TimeStampMixin, Base):
    __tablename__ = "product_categories"

    # Product id (foreign key on products table)
    product_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("products.id", ondelete="CASCADE"), 
        nullable=False,
        primary_key=True
    )
    # Product's category (category id) (foreign key on categories table)
    category_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("categories.id", ondelete="CASCADE"), 
        nullable=False,
        primary_key=True,
    )

