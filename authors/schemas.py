
from pydantic import BaseModel#, date


class Author(BaseModel):
    id: int
    first_name: str
    last_name: str
    #birth_date: date
