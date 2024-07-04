from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Item(BaseModel):
    name: str
    price: float

items = {}

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return item

@router.get("/items/{item_name}", response_model=Item)
def read_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_name]
