from fastapi import APIRouter

router = APIRouter(prefix='/borrows', tags=['borrows'])

@router.get('/')
def get_borrows():
    return {'get books': 'success'}

@router.get('/{id}')
def get_borrow_by_id(id: int):
    return {f'book with id {id}': 'success'}

@router.post('/')
def new_borrow(id: int):
    return {f'new book with id {id}': 'success'}

@router.patch('/{id}/return')
def close_borrow():
    pass
