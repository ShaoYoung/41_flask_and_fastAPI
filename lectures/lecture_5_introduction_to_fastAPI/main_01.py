from fastapi import FastAPI

# создаём приложение
app = FastAPI()


@app.get("/")
async def root():
    # возвращает словарь
    return {"message": "Hello World"}
    # fastAPI делает JSON-объект

# http://127.0.0.1:8000/items/42
# http://127.0.0.1:8000/items/42?q=text
# item_id, q - это переменные
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    # тип указывается внутри функции, а не внутри пути
    return {"item_id": item_id, "q": q}
