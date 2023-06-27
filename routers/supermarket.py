from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from utils.interfaces import Response
from services.supermarket import SupermarketService
from dependencies import validate_api_key


supermarket = APIRouter(
    dependencies=[Depends(validate_api_key)]
)


@supermarket.get('/api/supermarket/all', tags=['Supermarket'], response_model=Response)
async def get_supermarkets():
    db = Session()
    result = SupermarketService(db).get_supermarkets()
    return JSONResponse(status_code=200, content={'message': 'Supermarkets list', 'data':jsonable_encoder(result)})

@supermarket.get('/api/supermarket/{id}', tags=['Supermarket'], response_model=Response)
async def get_supermarket_by_id(id: int):
    db = Session()
    result = SupermarketService(db).get_supermarket_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found Supermarket', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get Supermarket success', 'data':jsonable_encoder(result)})

@supermarket.post('/api/supermarket', tags=['Supermarket'], response_model=Response)
async def create_supermarket(name: str = Query()):
    db = Session()
    SupermarketService(db).create_supermarket(name)
    return JSONResponse(status_code=200, content={'message': 'Supermarket created', 'data':jsonable_encoder(name)})

@supermarket.put('/api/supermarket/{id}', tags=['Supermarket'])
async def update_supermarket(id: int, name: str = Query()):
    db = Session()
    result = SupermarketService(db).update_supermarket(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked updated'})

@supermarket.delete('/api/supermarket/{id}', tags=['Supermarket'])
async def delete_supermarket(id: int):
    db = Session()
    result = SupermarketService(db).delete_supermarket(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked deleted'})
