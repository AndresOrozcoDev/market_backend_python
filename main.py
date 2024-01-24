import uvicorn

from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.product import product
from app.api.routers.category import category
from app.api.routers.supermarket import supermarket

from app.db.database import engine, Base
from app.utils.middlewares.error_handle import ErrorHandler


app = FastAPI(
    title='Market project backend',
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="./app/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.add_middleware(ErrorHandler)
app.include_router(supermarket)
app.include_router(category)
app.include_router(product)
Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)