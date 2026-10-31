from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Automation Demo API", version="1.0.0")
_items: dict[int, dict] = {}
_next_id = 1

class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    quantity: int = Field(ge=1, le=1000)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return {"items": list(_items.values())}

@app.post("/items", status_code=201)
def create_item(payload: ItemIn):
    global _next_id
    item = {"id": _next_id, **payload.model_dump()}
    _items[_next_id] = item
    _next_id += 1
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="item not found")
    return _items[item_id]