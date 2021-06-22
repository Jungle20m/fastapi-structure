from fastapi import APIRouter

from src.api.routes import users


router = APIRouter()
router.include_router(users.router, prefix="/user")
