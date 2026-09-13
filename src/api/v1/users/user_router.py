# Fastapi dependencies
from fastapi import APIRouter
# Users service
from src.services.users.user_services import UserService
from src.schemas.users.user import UserCreate, UserResponse

from typing import Annotated
from fastapi import Depends


# User router
router = APIRouter()

# Returns concrete user by his ID
@router.get('/users/{user_id}', response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    return UserService.get_user(id=user_id)

# Returns all users
@router.get('/users', response_model=list[UserResponse])
async def get_users() -> list[UserResponse]:
    return UserService.get_all_users()

# Creates new user
@router.post('/users', response_model=UserResponse)
async def create_user(user_data: UserCreate, user_service: Annotated[UserService, Depends()]) -> UserResponse:
    new_user = await UserService.create_user(user_data=user_data)
    return new_user
