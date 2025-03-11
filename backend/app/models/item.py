from typing import Optional
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """Base item model with common attributes."""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    price: float = Field(..., ge=0)


class ItemCreate(ItemBase):
    """Model for creating a new item."""
    pass


class ItemUpdate(BaseModel):
    """Model for updating an existing item."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    price: Optional[float] = Field(None, ge=0)


class Item(ItemBase):
    """Full item model including ID."""
    id: int
    
    class Config:
        """Pydantic configuration."""
        from_attributes = True 