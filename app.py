from fastapi import FastAPI
from authors.views import router as authors_r
from books.views import router as books_r
from borrows.views import router as borrows_r

app = FastAPI()
app.include_router(authors_r)
app.include_router(books_r)
app.include_router(borrows_r)
