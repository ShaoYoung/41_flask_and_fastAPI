import uvicorn
from db import db
from fastapi import FastAPI
# from fastapi import Request, HTTPException
# from fastapi.templating import Jinja2Templates
import users_routers
import products_routers
import orders_routers

app = FastAPI()


# templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(users_routers.router, tags=['users'])
app.include_router(products_routers.router, tags=['products'])
app.include_router(orders_routers.router, tags=['orders'])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
