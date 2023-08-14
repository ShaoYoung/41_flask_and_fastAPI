import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

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


# Создадим две модели данных Pydantic:
class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# В боевом режиме заполнение реальной БД через get-запрос крайне нежелательно
@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
        # асинхронный запрос к БД
        await database.execute(query)
    return {'message': f'{count} fake users create'}


# Создание пользователя в БД, create
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    # создание объекта-запрос (insert - добавление новых данных в БД)
    query = users.insert().values(name=user.name, email=user.email)
    # аналогичная запись (превращение в словарь и распаковка на пары ключ-значение)
    query = users.insert().values(**user.dict())
    # выполняем запрос и сохраняем id записи
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


# Чтение всех пользователей из БД, read
@app.get("/users/", response_model=List[User])
async def read_users():
    # выбрать из таблицы users (всех)
    query = users.select()
    # получить все записи по запросу query
    return await database.fetch_all(query)


# Чтение одного пользователя из БД, read
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    # выбрать из таблицы users, где
    # users - таблица, c - колонка, id - имя колонки
    query = users.select().where(users.c.id == user_id)
    # получить одну запись по запросу
    return await database.fetch_one(query)

# Обновление пользователя в БД, update
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    # обновление информации в таблице users
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}

# Удаление пользователя из БД, delete
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
