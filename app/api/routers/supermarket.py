from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.db.database import Session
from app.api.interfaces.interfaces import Response
from app.services.supermarket import SupermarketService
from dependencies import validate_api_key


supermarket = APIRouter(
    prefix="/supermarket",
    tags=["Supermarket"],
    dependencies=[Depends(validate_api_key)]
)


@supermarket.get('/all', response_model=Response)
async def get_supermarkets():
    db = Session()
    result = SupermarketService(db).get_supermarkets()
    return JSONResponse(status_code=200, content={'message': 'Supermarkets list', 'data':jsonable_encoder(result)})

@supermarket.get('/{id}', response_model=Response)
async def get_supermarket_by_id(id: int):
    db = Session()
    result = SupermarketService(db).get_supermarket_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found Supermarket', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get Supermarket success', 'data':jsonable_encoder(result)})

@supermarket.post('', response_model=Response)
async def create_supermarket(name: str = Query()):
    db = Session()
    SupermarketService(db).create_supermarket(name)
    return JSONResponse(status_code=200, content={'message': 'Supermarket created', 'data': jsonable_encoder(name)})

@supermarket.put('/{id}')
async def update_supermarket(id: int, name: str = Query()):
    db = Session()
    result = SupermarketService(db).update_supermarket(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked updated'})

@supermarket.delete('/{id}')
async def delete_supermarket(id: int):
    db = Session()
    result = SupermarketService(db).delete_supermarket(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked deleted'})
