from fastapi import APIRouter

router = APIRouter(prefix='/borrows', tags=['borrows'])

@router.get('/')
async def get_borrows():
    return {'get books': 'success'}

@router.get('/{id}')
async def get_borrow_by_id(id: int):
    return {f'book with id {id}': 'success'}

@router.post('/')
async def new_borrow(id: int):
    return {f'new book with id {id}': 'success'}

@router.patch('/{id}/return')
async def close_borrow():
    pass
