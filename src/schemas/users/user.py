# Pydantic dependencies
from pydantic import (
    BaseModel, 
    ConfigDict,
    Field,
    EmailStr,
)
# Time context dependencies
from datetime import datetime


# User creation schema (POST)
class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=32)
    email: EmailStr = Field(min_length=1, max_length=255)
    # password: str = Field(min_length=8, max_length=50)
    phone: str | None = Field(min_length=11, max_length=20)
    is_active: bool = True


# User update schema (PUT/PATCH)
class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=32)
    email: EmailStr | None = Field(default=None, min_length=1, max_length=255)
    phone: str | None = Field(default=None, min_length=11, max_length=20)
    password: str | None = None
    is_active: bool | None = None


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
