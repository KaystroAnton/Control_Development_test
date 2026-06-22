from pydantic import BaseModel
from datetime import  datetime as time
from pydantic import ConfigDict

class BookingBase(BaseModel):
    name: str 
    datetime: time = time.now()
    service_type: str 
    status: str

class BookingCreate(BookingBase):
    pass

class BookingRead(BookingBase):
    model_config = ConfigDict(
        from_attributes=True,
    ) # можно убрать так как это идёт по умолчанию
    id: int