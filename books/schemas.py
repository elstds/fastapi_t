from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    description: str
    author_id: int
    amount: int

class Book(BookBase):
    id: int