from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    points: Mapped[int] = mapped_column(default=0)