from fastapi import APIRouter, Body, Query
from config.database import Session
from utils.interfaces import Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.supermarket import SupermarketService

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@router.get('/api/supermarkets', tags=['Supermarket'], response_model=Response)
def get_supermarkets():
    db = Session()
    result = SupermarketService(db).get_supermarkets()
    return JSONResponse(status_code=200, content={'message': 'Supermarkets list', 'data':jsonable_encoder(result)})

@router.get('/api/supermarket/{id}', tags=['Supermarket'], response_model=Response)
def get_supermarket_by_id(id: int):
    db = Session()
    result = SupermarketService(db).get_supermarket_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found Supermarket', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get Supermarket success', 'data':jsonable_encoder(result)})

@router.post('/api/supermarket', tags=['Supermarket'], response_model=Response)
def create_supermarket(name: str = Query()):
    db = Session()
    SupermarketService(db).create_supermarket(name)
    return JSONResponse(status_code=200, content={'message': 'Supermarket created', 'data':jsonable_encoder(name)})

@router.put('/api/supermarket/{id}', tags=['Supermarket'])
def update_todo(id: int, name: str = Query()):
    db = Session()
    result = SupermarketService(db).update_supermarket(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked updated'})

@router.delete('/api/supermarket/{id}', tags=['Supermarket'])
def delete_supermarket(id: int):
    db = Session()
    result = SupermarketService(db).delete_supermarket(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked deleted'})