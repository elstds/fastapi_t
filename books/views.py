from fastapi import APIRouter

router = APIRouter(prefix='/books', tags=['books'])

@router.get('/')
async def get_books():
    return {'get books': 'success'}

@router.get('/{id}')
async def get_book_by_id(id: int):
    return {f'book with id {id}': 'success'}

@router.post('/{id}')
async def new_book(id: int):
    return {f'new book with id {id}': 'success'}

@router.put('/{id}')
async def update_book(id: int):
    return {f'book {id} was updated': 'success'}

@router.delete('{id}')
async def delete_book():
    pass
