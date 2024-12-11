from fastapi import FastAPI
from typing import Union
from routing.authors import router as authors_r

app = FastAPI()
app.include_router(authors_r)
