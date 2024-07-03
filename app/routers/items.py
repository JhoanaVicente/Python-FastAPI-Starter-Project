from fastapi import APIRouter
from app.models.item import Item

router = APIRouter()

items = []

@router.post("/items/")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created", "item": item}

@router.get("/items/")
def get_items():
    return items

