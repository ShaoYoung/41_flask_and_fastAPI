from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
# ... - поле обязательное
async def read_item(item_id: int = Path(..., ge=1), q: str = None):
    return {"item_id": item_id, "q": q}

