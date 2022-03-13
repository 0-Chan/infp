from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

###########################################

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

###########################################


class ReceiptBase(BaseModel):
    date: str
    from_: str = None
    to: str
    message: str

    class Config:
        fields = {
            'from_': 'from'
        }
        
class ReceiptCreate(ReceiptBase):
    pass

class Receipt(ReceiptBase):
    # id: int
    
    class Config:
        orm_mode = True
