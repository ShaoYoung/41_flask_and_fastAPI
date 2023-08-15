from models import User, UserIn
# from fastapi.responses import HTMLResponse
from fastapi import APIRouter
# from fastapi import Request
from db import db, users

# from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="templates")
router = APIRouter()


# стартовый ендпоинт
@router.get('/')
async def main():
    return {'endpoint': 'online_store'}


# Создание тестовых пользователей
@router.get('/fake_users/{count}', summary='Создать тестовых пользователей')
async def create_fake_users(count: int):
    for i in range(1, count + 1):
        query = users.insert().values(
            username=f'username_{i}',
            surname=f'surname_{i}',
            email=f'mail_{i}@mail.ru',
            password=f'password_{i}')
        await db.execute(query)
    return {'message': f'{count} fake users create'}


# Создание нового пользователя
@router.post('/users/new/', response_model=User, summary='Добавить нового пользователя')
async def create_user(user: UserIn):
    query = users.insert().values(
        username=user.username,
        surname=user.surname,
        email=user.email,
        password=user.password)
    last_record_id = await db.execute(query)
    return {**user.dict(), "id": last_record_id}


# Получить список пользователей
@router.get('/users/', response_model=list[User], summary='Получить список пользователей')
async def get_users():
    query = users.select()
    return await db.fetch_all(query)


# Получить одного пользователя
@router.get('/users/{user_id}', response_model=User, summary='Получить одного пользователя')
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)


# Изменение пользователя
@router.put('/users/change/{user_id}', response_model=User, summary='Изменить данные пользователя')
async def change_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await db.execute(query)
    return {**new_user.dict(), "id": user_id}


# Удаление пользователя
@router.delete('/users/del/{user_id}', summary='Удалить пользователя')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {'message': f'User ({user_id=}) deleted'}

