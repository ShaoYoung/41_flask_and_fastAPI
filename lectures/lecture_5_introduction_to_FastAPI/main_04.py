import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

#  post - новые данные
@app.post("/items/")
# объект (модель данных, словарь или json-объект), к-й мы хотим получить через POST-запрос
# Функция create_item() принимает объект Item и возвращает его же.
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item
