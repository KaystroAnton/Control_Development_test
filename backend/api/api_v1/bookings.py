from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core. config import settings
from fastapi import APIRouter, Depends
from core.schemas.bookings import BookingRead,BookingCreate
from core.models.booking import Booking
from api.api_v1.crud.base_crude import create_row, get_all_rows

from core.models import db_helper

router = APIRouter(tags = ["Bookings"])

@router.get("/",response_model=list[BookingRead],)
async def get_bookings(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    bookings = await get_all_rows(session=session,table= Booking)
    return bookings

@router.post("/",response_model=BookingRead)
async def create_booking(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    booking_create: BookingCreate
):
    booking = await create_row(
        session= session, 
        table=Booking,
        model_create=booking_create,
        )
    return booking