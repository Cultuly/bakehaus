from sqlalchemy import (
    Boolean,
    Integer,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from src.database.db import Base
from src.models.time_stamps import TimeStampMixin


# Categories table
class Category(TimeStampMixin, Base):
    __tablename__ = "categories"

    # Category id
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
    )
    # Category name
    name: Mapped[str] = mapped_column(
        String(64), 
        unique=True, 
        nullable=False
    )
    # Category parent id (soon)
    #parent_id: Mapped[int] = mapped_column(
    #    Integer, 
    #    unique=True, 
    #    nullable=True
    #)
    # Category activity status
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )


    # Products relationship
    products: Mapped[list["Products"]] = relationship(
        secondary="product_categories",
        back_populates="categories"
    )
