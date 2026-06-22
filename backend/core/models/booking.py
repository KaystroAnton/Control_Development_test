from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime as time
from .mixins.int_id_pk import IntIdPkMixin
from .base_model import Base


class Booking(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column(String(50))
    datetime: Mapped[time] 
    service_type: Mapped[str] 
    status: Mapped[str]

    __table_args__ = (
    UniqueConstraint("name","datetime"),
    )
    