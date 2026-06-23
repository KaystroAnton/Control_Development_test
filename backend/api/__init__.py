from fastapi import APIRouter
from api.api_v1 import router as bookings_router

router = APIRouter()
router.include_router(bookings_router)