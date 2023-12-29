import uvicorn

from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse

from app.api.routers.product import product
from app.api.routers.category import category
from app.api.routers.supermarket import supermarket

from app.db.database import engine, Base
from app.utils.middlewares.error_handle import ErrorHandler


app = FastAPI(
    title='Market project backend',
    version='1.0.0'
)


@app.get("/")
async def root():
    return HTMLResponse('<h2>Welcome to Market Backend Project with Python and FastAPI!.</h2>')


app.add_middleware(ErrorHandler)
app.include_router(supermarket)
app.include_router(category)
app.include_router(product)
Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)