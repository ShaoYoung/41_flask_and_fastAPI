import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///mydatabase.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

# создание переменной, к-я будет взаимодействовать с БД
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
...
# создание движка
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
app = FastAPI()

# событие - запуск приложения FastAPI
@app.on_event("startup")
async def startup():
    # асинхронное подключение к БД
    await database.connect()

# событие - выключение сервера
@app.on_event("shutdown")
async def shutdown():
    # асинхронное отключение от БД
    await database.disconnect()
