from fastapi import APIRouter
from datetime import date

router = APIRouter(prefix='/authors', tags=['authors'])

@router.get('/')
async def read_root():
    return {'authors': 'success'}

@router.get('/{id}')
async def read_item(id: int):
    return {'author_id': id}

@router.post('/{id}')
async def new_author(id: int, name: str, surname: str, birth_date: date):
    return {''}

@router.delete('/{id}')
async def delete_author(id: int):
    return {'answer': f'author with id {id} was deleted'}
