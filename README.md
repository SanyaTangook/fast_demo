# FastAPI Demo for cURL

## Run Server

```bash
cd /Users/sanya/develop/fast_demo
pip install fastapi uvicorn
uvicorn main:app --reload
```

Server will start at `http://localhost:8000`

---

## cURL Examples

### GET - หน้าแรก

```bash
curl -X GET "http://localhost:8000/"
```

### GET - ดึงข้อมูล item ด้วย ID

```bash
curl -X GET "http://localhost:8000/items/1"
```

### GET - ค้นหาด้วย query parameters

```bash
curl -X GET "http://localhost:8000/search?q=iphone&limit=5"
```

### POST - สร้าง Item ใหม่

```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "iPhone 15", "description": "Smartphone", "price": 999.00, "tax": 79.92}'
```

### POST - สร้าง User ใหม่

```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "email": "john@example.com", "full_name": "John Doe"}'
```

### PUT - อัพเดท Item

```bash
curl -X PUT "http://localhost:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "iPhone 15 Pro", "description": "Updated", "price": 1199.00}'
```

### DELETE - ลบ Item

```bash
curl -X DELETE "http://localhost:8000/items/1"
```

### POST - รวมหลาย Object

```bash
curl -X POST "http://localhost:8000/combine" \
  -H "Content-Type: application/json" \
  -d '{
    "item": {"name": "Test", "price": 100},
    "user": {"username": "user1", "email": "user@test.com"},
    "include_extra": true
  }'
```

---

## Interactive Documentation

เปิด browser ไปที่: http://localhost:8000/docs

จะเห็น Swagger UI สำหรับทดสอบ API ได้โดยตรง