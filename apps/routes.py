from fastapi import APIRouter
from .users.router import router as users_router


router = APIRouter(
    prefix = "/api")

router.include_router(
    router = users_router)