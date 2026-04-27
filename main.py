from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="FastAPI Demo for cURL", version="1.0.0")

# --- Models ---
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

# --- GET Endpoints ---

@app.get("/")
def read_root():
    """หน้าแรก"""
    return {"message": "Welcome to FastAPI Demo!", "endpoints": "/docs"}

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., description="ID ของ item")):
    """ดึงข้อมูล item ด้วย ID"""
    return {"item_id": item_id, "name": "Sample Item", "price": 9.99}

@app.get("/search")
def search_items(q: str = Query(..., description="คำค้นหา"), limit: int = Query(10, ge=1, le=100)):
    """ค้นหาข้อมูลด้วย query parameters"""
    return {"query": q, "limit": limit, "results": ["item1", "item2", "item3"]}

# --- POST Endpoints ---

@app.post("/items")
def create_item(item: Item):
    """สร้าง item ใหม่"""
    return {"message": "Item created", "item": item}

@app.post("/users")
def create_user(user: User):
    """สร้าง user ใหม่"""
    return {"message": "User created", "user": user}

# --- PUT Endpoints ---

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """อัพเดท item"""
    return {"message": "Item updated", "item_id": item_id, "item": item}

# --- DELETE Endpoints ---

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """ลบ item"""
    return {"message": "Item deleted", "item_id": item_id}

# --- Multiple Parameters ---

@app.post("/combine")
def combine_data(
    item: Item,
    user: User,
    include_extra: bool = Body(False)
):
    """รับข้อมูลหลาย object พร้อมกัน"""
    return {
        "item": item,
        "user": user,
        "include_extra": include_extra
    }