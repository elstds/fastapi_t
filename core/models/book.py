from .base import Base
from sqlalchemy.orm import Mapped, WriteOnlyMapped


class Book(Base):
    title: Mapped[str]
    description: Mapped[str]
    author_id: WriteOnlyMapped[]
    amount: Mapped[int]