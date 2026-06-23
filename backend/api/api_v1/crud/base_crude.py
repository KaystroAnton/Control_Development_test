from typing import Sequence
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from core.schemas.bookings import BookingRead

#get

async def get_all(
        session: AsyncSession,
        table: DeclarativeBase,
)-> Sequence[DeclarativeBase]:
    stmt = select(table)
    result = await session.scalars(stmt)
    return result.all()

async def get_one_by_id(
        session: AsyncSession,
        id: int,
        model: DeclarativeBase
)-> DeclarativeBase: # pending / confirmed / failed
    stmt = select(model).where(model.id == id)
    result = await session.scalar(stmt)
    if result is None:
        raise Exception("There is no row with such id")
    else:
        return result

#create

async def create_one(
        session: AsyncSession,
        model_create: BaseModel,
        table: DeclarativeBase,
)-> DeclarativeBase:
    row = table(**model_create.model_dump())
    session.add(row)
    await session.commit()
    # await session.refresh(row)
    return row
