from datetime import date
from pydantic import BaseModel

class Author(BaseModel):
    id: int
    name: str
    surname: str
    birth_date: date
