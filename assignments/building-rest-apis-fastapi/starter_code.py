from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float


# Simple in-memory store
items: List[Item] = []
_id_counter = 1


@app.get("/items/", response_model=List[Item])
def list_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    global _id_counter
    item.id = _id_counter
    _id_counter += 1
    items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for idx, it in enumerate(items):
        if it.id == item_id:
            updated.id = item_id
            items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, it in enumerate(items):
        if it.id == item_id:
            items.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")
