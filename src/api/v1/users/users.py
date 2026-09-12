# Fastapi dependencies
from fastapi import APIRouter
# Users service
from src.services.users.user_services import UserService
from src.schemas.users.user import UserCreate


# User router
router = APIRouter()


# Returns all users (GET)
@router.get('/users')
async def get_users():
    return UserService.get_all()

# Returns concrete user by his ID
@router.get('/users/{user_id}')
async def get_user(id: int):
    return UserService.get_user_by_id(id)

# Returns all users
@router.get('/users')
async def get_users():
    return UserService.get_all_users()

# Creates new user
@router.post('/users')
async def create_user():
    new_user = UserService.create_user()
    return new_user
