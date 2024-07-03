from fastapi import FastAPI
from app.models.item import Item
from app.routers import items

app = FastAPI()

app.include_router(items.router)
# Lista para almacenar los ítems creados
items = []

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created", "item": item}

@app.get("/items/")
def get_items():
    return items

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application!"}
