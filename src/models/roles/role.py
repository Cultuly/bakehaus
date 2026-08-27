from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.database.db import Base
from src.models.time_stamps import TimeStampMixin


# Roles table
class Role(TimeStampMixin, Base):
    __tablename__ = "roles"

    # Role id
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
    )
    # Role's code
    code: Mapped[str] = mapped_column(
        String(32),
        unique=True,
        nullable=False,
    )
    # Role name
    name: Mapped[str] = mapped_column(
        String(64), 
        unique=True,
        nullable=False,
    )