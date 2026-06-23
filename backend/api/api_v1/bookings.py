from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core. config import settings
from fastapi import APIRouter, Depends
from core.schemas.bookings import BookingRead,BookingCreate
from core.models.booking import Booking
from api.api_v1.crud.base_crude import create_one, get_all, get_one_by_id


from core.models import db_helper

router = APIRouter(tags = ["Bookings"])

@router.get("/all",response_model=list[BookingRead])
async def get_bookings(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    bookings = await get_all(
        session=session,
        table= Booking,
    )
    return bookings

@router.get("/{id}")
async def get_booking_satus_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    id: int
):
    booking = await get_one_by_id(
        session = session,
        id = id,
        model = Booking,
    )
    return booking.status

@router.post("/",response_model=BookingRead) 
async def create_booking(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    booking_create: BookingCreate
):
    booking = await create_one(
        session= session, 
        table = Booking,
        model_create = booking_create,
        )
    return booking