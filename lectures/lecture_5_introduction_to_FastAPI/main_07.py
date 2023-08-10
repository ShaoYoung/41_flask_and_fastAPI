from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    # без дандера-метода
    name: str
    # параметр может не передаваться (опционально)
    description: Optional[str] = None
    price: float
    # параметр может не передаваться (опционально)
    tax: Optional[float] = None
