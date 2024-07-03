from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

fake_items_db = [{"item_name": "Foo", "item_price": 50.2}]

@app.get("/items/", response_model=List[Item])
def read_items():
    return fake_items_db

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
