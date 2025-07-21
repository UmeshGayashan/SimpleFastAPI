from fastapi import FastAPI,HTTPException
from models.item import ItemModel

app = FastAPI()

items = []

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: ItemModel):
    items.append(item)
    return items

@app.get("/items/{item_id}")
async def get_item(item_id: int)->dict:
    if item_id < len(items):
        return {"item1": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/status")
async def status():
    return {"status": "running"}

@app.get("/info")
async def info():
    return {"app": "FastAPI Example", "version": "1.0.0"}

@app.get("/echo/{message}")
async def echo(message: str):
    return {"echo": message}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"greeting": f"Hello, {name}!"}