from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    # не обязательное поле
    is_offer: bool = None


class User(BaseModel):
    username: str
    # не обязательное поле
    full_name: str = None


class Order(BaseModel):
    items: List[Item]
    user: User


