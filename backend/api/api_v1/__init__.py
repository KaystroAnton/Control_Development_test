from fastapi import APIRouter
from core.config import settings

from api.api_v1.bookings import router as bookings_router

router = APIRouter(
    prefix= settings.api.v1.prefix
)

router.include_router(
    bookings_router,
    prefix = settings.api.v1.bookings,
)