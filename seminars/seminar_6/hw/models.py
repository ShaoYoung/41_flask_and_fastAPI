from pydantic import BaseModel, Field
from datetime import date


class UserIn(BaseModel):
    username: str = Field(..., title='username', min_length=2)
    surname: str = Field(title='surname', min_length=2)
    email: str = Field(..., title="email", min_length=6)
    password: str = Field(..., title="password", min_length=3)


class User(UserIn):
    id: int


class ProductIn(BaseModel):
    product_name: str = Field(..., title='product_name', min_length=2)
    description: str = Field(title='description', min_length=2)
    price: int = Field(..., title='price', ge=0)


class Product(ProductIn):
    id: int


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    order_date: date = Field(..., title='order_date')
    status: str = Field(..., title='status')


class Order(OrderIn):
    id: int
