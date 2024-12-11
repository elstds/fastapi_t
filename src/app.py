from fastapi import FastAPI
from src.routing.authors import router as authors_r

app = FastAPI()
app.include_router(authors_r)
