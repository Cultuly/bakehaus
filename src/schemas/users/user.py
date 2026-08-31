# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    Field,
    EmailStr,
)
# Time context dependencies
from datetime import datetime


# User base for enheritance
class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=16)
    email: EmailStr = Field(min_length=1, max_length=32)
    phone: str | None = Field(min_length=11, max_length=20)
    is_active: bool = True


# User creation schema (POST)
class UserCreate(UserBase):
    # password: str = Field(min_length=8, max_length=50)
    pass


# User update schema (PUT/PATCH)
class UserUpdate(BaseModel):
    username: str | None = Field(min_length=1, max_length=16)
    email: EmailStr | None = Field(min_length=1, max_length=32)
    phone: str | None = Field(min_length=11, max_length=20)
    password: str | None
    is_active: bool | None

# User response schema
class UserResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    phone: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None
