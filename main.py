from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

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