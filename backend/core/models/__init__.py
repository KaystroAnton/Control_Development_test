# Обязательно импортировать новый таблицы в Инит, иначе алембик их не увидит
__all__ =(
    "db_helper",
    "Base",
)

from .db_helper import db_helper
from .base_model import Base