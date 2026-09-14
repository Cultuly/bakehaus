# Fastapi dependencies
from fastapi import APIRouter
# Users service
from src.services.users.user_services import UserService
from src.schemas.users.user import UserCreate, UserResponse

from typing import Annotated
from fastapi import Depends
from src.core.factories import get_user_service


# User router
router = APIRouter()

# Returns concrete user by his ID
@router.get('/users/{user_id}', response_model=UserResponse)
async def get_user(user_id: int,
                   service: Annotated[UserService, Depends(get_user_service)]) -> UserResponse:
    return await service.get_user(user_id)

# Returns all users
@router.get('/users', response_model=list[UserResponse])
async def get_users(service: Annotated[UserService, Depends(get_user_service)]) -> list[UserResponse]:
    # Returns list of users instances
    return await service.get_all_users()

# Creates new user
@router.post('/users', response_model=UserResponse)
async def create_user(user_data: UserCreate,
                      service: Annotated[UserService, Depends(get_user_service)]) -> UserResponse:
    new_user = await service.create_user(user_data)
    # Returns new_user instance
    return new_user
