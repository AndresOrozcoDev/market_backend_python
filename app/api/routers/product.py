from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.db.database import Session
from app.api.interfaces.interfaces import Response, Product
from app.services.product import ProductService
from dependencies import validate_api_key


product = APIRouter(
    prefix="/api/product",
    tags=["Product"],
    dependencies=[Depends(validate_api_key)]
)


@product.get('/all', tags=['Product'], response_model=Response)
async def get_products():
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Products list', 'data':jsonable_encoder(result)})

@product.get('/{id}', tags=['Product'], response_model=Response)
async def get_product_by_id(id: int):
    db = Session()
    result = ProductService(db).get_product_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found product', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Get product success', 'data':jsonable_encoder(result)})

@product.post('', tags=['Product'], response_model=Response)
async def create_product(product: Product = Body()):
    db = Session()
    result = ProductService(db).create_product(product)
    return JSONResponse(status_code=200, content={'status_code': 201, 'message': result})

@product.put('/{id}', tags=['Product'])
async def update_product(id: int, product: Product = Body()):
    db = Session()
    result = ProductService(db).update_product(id, product)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Product updated'})

@product.delete('/{id}', tags=['Product'])
async def delete_product(id: int):
    db = Session()
    result = ProductService(db).delete_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Product deleted'})

