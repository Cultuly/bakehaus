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


# Users table
class User(TimeStampMixin, Base):
    __tablename__ = "users"

    # User id
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
    )
    # User's username
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True, 
        nullable=False
    )
    # User's email
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    # User's password hash (soon)
    #password_hash: Mapped[str] = mapped_column(
    # String(200), 
    # nullable=False
    #)
    # User's phone number (soon)
    phone: Mapped[str | None] = mapped_column(
        String(20), 
        nullable=True
    )
    # User's activity status
    is_active: Mapped[bool] = mapped_column(
        Boolean, 
        nullable=False,
        default=True,
    )

    
    # User roles relationship through pivot table
    roles: Mapped[list["UserRole"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

