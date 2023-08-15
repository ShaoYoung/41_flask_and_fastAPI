from models import Order, OrderIn
# from fastapi.responses import HTMLResponse
from fastapi import APIRouter
# from fastapi import Request
from db import db, orders, users, products
import sqlalchemy

# from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="templates")
router = APIRouter()


# проверка корректности заполнения пользователя и продукта в заказе
async def check_order(order: OrderIn) -> bool:
    query = users.select().where(users.c.id == order.user_id)
    existing_user = await db.fetch_one(query)
    query = products.select().where(products.c.id == order.product_id)
    existing_product = await db.fetch_one(query)
    return existing_user and existing_product


# Создание нового заказа
@router.post('/orders/new/', summary='Создать новый заказ')
async def create_order(order: OrderIn):
    # для заказа должны существовать user_id и product_id. проверяем.
    if await check_order(order):
        query = orders.insert().values(
            user_id=order.user_id,
            product_id=order.product_id,
            order_date=order.order_date,
            status=order.status)
        last_record_id = await db.execute(query)
        return {**order.dict(), "id": last_record_id}
    return {'message': 'Input data (user or product) not correct'}


# Получить список всех заказов
@router.get('/orders/', response_model=list[Order], summary='Получить список заказов')
async def read_orders():
    query = orders.select()
    return await db.fetch_all(query)


# Получить заказы одного пользователя
@router.get('/orders/{user_id}', response_model=list[Order], summary='Получить заказы одного пользователя')
async def get_orders_by_user(user_id: int):
    query = orders.select().where(orders.c.user_id == user_id)
    return await db.fetch_all(query)


# Изменение заказа
@router.put('/orders/change/{order_id}', summary='Изменить данные заказа')
async def change_order(order_id: int, new_order: OrderIn):
    # для изменённого заказа должны существовать user_id и product_id. проверяем.
    if await check_order(new_order):
        query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
        await db.execute(query)
        return {**new_order.dict(), "id": order_id}
    return {'message': 'Input data (user or product) in new_order not correct'}


# Удаление заказа
@router.delete('/orders/del/{order_id}', summary='Удалить заказ')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {'message': f'Order ({order_id=}) deleted'}


# Получение расширенной информации по заказам выбранного пользователя
@router.get('/orders_extended/{user_id}', summary='Расширенная информация по заказам выбранного пользователя')
async def get_orders_extended(user_id: int):
    query = sqlalchemy.select(orders.c.order_date.label('date'), users.c.username.label('username'),
                              products.c.product_name.label('product'), products.c.price.label('price')).join(
        users).join(products).where(
        orders.c.user_id == user_id)
    rows = await db.fetch_all(query)
    orders_list = []
    for row in rows:
        orders_list.append({'date': row.date,
                            'username': row.username,
                            'product': row.product,
                            'price': row.price})
    # print(orders_list)
    return orders_list
