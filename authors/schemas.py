
from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    first_name: str
    last_name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
