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

    
    class Config:
        orm_mode = True


class Receipt2Base(BaseModel):
    is_refund: bool
    payer: str
    expense: int
    installment: int
    date: str
    store: str
    total_expense: int
        
class Receipt2Create(Receipt2Base):
    pass

class Receipt2(Receipt2Base):

    
    class Config:
        orm_mode = True
###########################################
class Receipt3Base(BaseModel):
    name: str
    pkg: str
    title: str
    text: str
    subtext: str
    bigtext: str
    infotext: str

class Receipt3Create(Receipt3Base):
    pass

class Receipt3(Receipt3Base):

    
    class Config:
        orm_mode = True
###########################################
    # id = Column(Integer, primary_key=True, index=True)
    # is_refund = Column(Boolean)
    # payer = Column(String)
    # expense = Column(Integer)
    # installment = Column(Integer)
    # date = Column(String, index=True)
    # store = Column(String)
    # total_expense = Column(Integer)