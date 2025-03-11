from typing import List, Optional
from fastapi import APIRouter, HTTPException, status

from app.models.item import Item, ItemCreate, ItemUpdate

router = APIRouter()

# Sample in-memory database
items_db = [
    {"id": 1, "name": "Example Item 1", "description": "This is an example item", "price": 10.5},
    {"id": 2, "name": "Example Item 2", "description": "Another example item", "price": 20.0},
]


@router.get("/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 100):
    """
    Retrieve items.
    """
    return items_db[skip: skip + limit]


@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """
    Get item by ID.
    """
    item = next((item for item in items_db if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """
    Create new item.
    """
    # Find the next available ID
    next_id = max(item["id"] for item in items_db) + 1 if items_db else 1
    
    # Create new item
    new_item = Item(id=next_id, **item.model_dump())
    items_db.append(new_item.model_dump())
    
    return new_item


@router.patch("/{item_id}", response_model=Item)
async def update_item(item_id: int, item_update: ItemUpdate):
    """
    Update an item.
    """
    # Find the item
    item_idx = next((idx for idx, item in enumerate(items_db) if item["id"] == item_id), None)
    if item_idx is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Update only provided fields
    update_data = item_update.model_dump(exclude_unset=True)
    current_item = items_db[item_idx]
    updated_item = {**current_item, **update_data}
    items_db[item_idx] = updated_item
    
    return updated_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """
    Delete an item.
    """
    # Find the item
    item_idx = next((idx for idx, item in enumerate(items_db) if item["id"] == item_id), None)
    if item_idx is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Remove the item
    items_db.pop(item_idx) 