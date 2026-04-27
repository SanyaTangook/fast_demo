import logging
from fastapi import FastAPI, Query, Path, Body, Request
from pydantic import BaseModel
from typing import Optional, List
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI Demo for cURL", version="1.0.0")

# Middleware for logging requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url.path}")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Response: {response.status_code} - Time: {process_time:.3f}s")
    return response

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
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to FastAPI Demo!", "endpoints": "/docs"}

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., description="ID ของ item")):
    """ดึงข้อมูล item ด้วย ID"""
    logger.info(f"Get item: {item_id}")
    return {"item_id": item_id, "name": "Sample Item", "price": 9.99}

@app.get("/search")
def search_items(q: str = Query(..., description="คำค้นหา"), limit: int = Query(10, ge=1, le=100)):
    """ค้นหาข้อมูลด้วย query parameters"""
    logger.info(f"Search: q={q}, limit={limit}")
    return {"query": q, "limit": limit, "results": ["item1", "item2", "item3"]}

# --- POST Endpoints ---

@app.post("/items")
def create_item(item: Item):
    """สร้าง item ใหม่"""
    logger.info(f"Create item: {item.name}")
    return {"message": "Item created", "item": item}

@app.post("/users")
def create_user(user: User):
    """สร้าง user ใหม่"""
    logger.info(f"Create user: {user.username}")
    return {"message": "User created", "user": user}

# --- PUT Endpoints ---

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """อัพเดท item"""
    logger.info(f"Update item: {item_id} - {item.name}")
    return {"message": "Item updated", "item_id": item_id, "item": item}

# --- DELETE Endpoints ---

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """ลบ item"""
    logger.info(f"Delete item: {item_id}")
    return {"message": "Item deleted", "item_id": item_id}

# --- Multiple Parameters ---

@app.post("/combine")
def combine_data(
    item: Item,
    user: User,
    include_extra: bool = Body(False)
):
    """รับข้อมูลหลาย object พร้อมกัน"""
    logger.info(f"Combine data: item={item.name}, user={user.username}, extra={include_extra}")
    return {
        "item": item,
        "user": user,
        "include_extra": include_extra
    }