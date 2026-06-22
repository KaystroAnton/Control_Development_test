from typing import Sequence
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

async def create_row(
        session: AsyncSession,
        schema: DeclarativeBase,
)-> DeclarativeBase:
    row = schema(**schema.model_dump())
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row

async def get_all_rows(
        session: AsyncSession,
        table: DeclarativeBase,
)-> Sequence[DeclarativeBase]:
    stmt = select(table)
    result = await session.scalars(stmt)
    return result.all()

async def create_row(
        session: AsyncSession,
        model_create: BaseModel,
        table: DeclarativeBase
)-> DeclarativeBase:
    row = table(**model_create.model_dump())
    session.add(row)
    await session.commit()
    #await session.refresh()
    return row