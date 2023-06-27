from fastapi import APIRouter, Body, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from utils.interfaces import Response, User
from services.user import UserService
from dependencies import validate_api_key


over = APIRouter(
    dependencies=[Depends(validate_api_key)]
)


@over.get('/api/compare/{name}', tags=['Over'], response_model=Response)
async def get_compare(name: str):
    return JSONResponse(status_code=200, content={'message': 'Building services'})

@over.post('/api/forgetPassword', tags=['Over'], response_model=Response)
async def forget_password(email: str = Query()):
    db = Session()
    result = UserService(db).post_forgetPassword(email)
    return JSONResponse(status_code=200, content={'message': jsonable_encoder(result)})

@over.post('/api/login', tags=['Over'], response_model=Response)
async def post_login(user: User = Body()):
    db = Session()
    result = UserService(db).post_login(user)
    return JSONResponse(status_code=200, content={'message': 'Get user success', 'data':jsonable_encoder(result)})
