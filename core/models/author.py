from .base import Base
from sqlalchemy.orm import Mapped

class Author(Base):
    first_name: Mapped[str]
    last_name: Mapped[str]
