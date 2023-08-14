import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
# описание таблицы
users = sqlalchemy.Table(
    # имя
    "users",
    # метаданные
    metadata,
    # колонки
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)
engine = sqlalchemy.create_engine(
    # connect_args нужен только для БД sqlite
    DATABASE_URL, connect_args={"check_same_thread": False}
)
# создание таблиц
metadata.create_all(engine)

app = FastAPI()
