from fastapi import FastAPI
from typing import Union
from routing import authors

app = FastAPI()
app.include_router(authors)
