from typing import Optional

from fastapi import FastAPI, Depends
from user import get_user

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "wooooooooorrrrrrrrld"}

@app.get("/api/")
async def hello():
    return {"msg":"Hello, this is API server"}

@app.get("/api/me")
async def hello_user(user = Depends(get_user)):
    return {"msg":"Hello, user","uid":user['uid']} 

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}