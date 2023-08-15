from models import Product, ProductIn
# from fastapi.responses import HTMLResponse
from fastapi import APIRouter
# from fastapi import Request
from db import db, products

# from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Создание тестовых продуктов
@router.get('/fake_products/{count}', summary='Создать тестовые продукты')
async def create_fake_products(count: int):
    for i in range(1, count + 1):
        query = products.insert().values(
            product_name=f'product_name_{i}',
            description=f'description_{i}',
            price=i * 10)
        await db.execute(query)
    return {'message': f'{count} fake products create'}


# Создание нового продукта
@router.post('/products/new/', response_model=Product, summary='Добавить новый продукт')
async def create_product(product: ProductIn):
    query = products.insert().values(
        product_name=product.product_name,
        description=product.description,
        price=product.price)
    last_record_id = await db.execute(query)
    return {**product.dict(), "id": last_record_id}


# Получить список продуктов
@router.get('/products/', response_model=list[Product], summary='Получить список продуктов')
async def get_products():
    query = products.select()
    return await db.fetch_all(query)


# Получить один продукт
@router.get('/products/{product_id}', response_model=Product, summary='Получить один продукт')
async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await db.fetch_one(query)


# Изменение продукта
@router.put('/products/change/{product_id}', response_model=Product, summary='Изменить продукт')
async def change_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await db.execute(query)
    return {**new_product.dict(), "id": product_id}


# Удаление продукта
@router.delete('/products/del/{product_id}', summary='Удалить продукт')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await db.execute(query)
    return {'message': f'Product ({product_id=}) deleted'}
