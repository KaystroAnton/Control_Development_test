
from typing import Optional

from pydantic.json_schema import SkipJsonSchema
from pydantic import BaseModel, Field, computed_field
from datetime import  datetime as time
from pydantic import ConfigDict
from enum import Enum

class Booking_Status(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    FAILD = "failed"

class BookingBase(BaseModel):
    name: str 
    datetime: time = Field(time.now())
    service_type: str 

    @computed_field
    @property
    def status(self)->Booking_Status:
        return Booking_Status.PENDING
    
    model_config = ConfigDict(
        extra='forbid',

    )

class BookingCreate(BookingBase):
    datetime: time = Field(time.now(), ge=time.now())



class BookingRead(BookingBase):
    model_config = ConfigDict(
        from_attributes=True,
    ) # можно убрать так как это идёт по умолчанию
    id: int