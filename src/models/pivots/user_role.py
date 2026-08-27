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


# Roles table (pivot table)
class UserRole(TimeStampMixin, Base):
    __tablename__ = "users_roles"

    # User's id
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    # Role id
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("roles.id", ondelete="CASCADE"),
        primary_key=True,
    )


    # User relationship
    user: Mapped["User"] = relationship(
        back_populates="roles",
    )
    # Role relationship
    role: Mapped["Role"] = relationship()
