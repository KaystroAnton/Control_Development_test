from sqlalchemy import String, UniqueConstraint, func, text
from sqlalchemy.orm import Mapped, mapped_column
from .base_model import Base
from datetime import datetime as time
class Booking(Base):
    name: Mapped[str] = mapped_column(String(50))
    datetime: Mapped[time] 
    service_type: Mapped[str] 
    status: Mapped[str]

    __table_args__ = (
    UniqueConstraint("name","datetime"),
    )
    