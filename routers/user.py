from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from utils.interfaces import Response, User
from services.user import UserService
from dependencies import validate_api_key


user = APIRouter(
    prefix="/user",
    tags=["User"],
    dependencies=[Depends(validate_api_key)]
)


@user.get('/all', response_model=Response)
async def get_users():
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content={'message': 'Users list', 'data':jsonable_encoder(result)})

@user.get('/{id}', response_model=Response)
async def get_user_by_id(id: int):
    db = Session()
    result = UserService(db).get_user_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found user', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get user success', 'data':jsonable_encoder(result)})


@user.post('', response_model=Response)
async def create_user(user: User = Body()):
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=200, content={'message': jsonable_encoder(user)})

@user.put('/api/product/{id}', tags=['User'])
async def update_user(id: int, password: str = Body()):
    db = Session()
    result = UserService(db).update_user(id, password)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found user'})
    return JSONResponse(status_code=200, content={'message': 'User updated'})

@user.delete('/{id}', tags=['User'])
async def delete_user(id: int):
    db = Session()
    result = UserService(db).delete_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found user'})
    return JSONResponse(status_code=200, content={'message': 'User deleted'})

