import os
from fastapi import FastAPI
from app.models.item import Item
from app.routers import items
from databases import Database
import asyncpg

load_dotenv()
app = FastAPI()

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
database = Database(DATABASE_URL)

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

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Ejemplo de endpoint que consulta datos de la base de datos
@app.get("/items/")
async def read_items():
    query = "SELECT * FROM items;"
    return await database.fetch_all(query)
