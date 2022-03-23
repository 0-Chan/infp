from typing import List, Optional, Type
import inspect
from fastapi import Form

from pydantic import BaseModel

def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        new_parameters.append(
             inspect.Parameter(
                 model_field.alias,
                 inspect.Parameter.POSITIONAL_ONLY,
                 default=Form(...) if not model_field.required else Form(model_field.default),
                 annotation=model_field.outer_type_,
             )
         )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, 'as_form', as_form_func)
    return cls


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
class Receipt3Form(BaseModel):
    a: str

@as_form
class Receipt3Base(BaseModel):
    name: str
    pkg: str
    title: str
    text: str
    token: str

class Receipt3Create(Receipt3Base):
    pass

class Receipt3(Receipt3Base):

    class Config:
        orm_mode = True

###
# class Test1(BaseModel):
#     a: str

# @as_form
# class Test(BaseModel):
#     name: str
#     pkg: str
#     title: str
#     text: str
###########################################
    # id = Column(Integer, primary_key=True, index=True)
    # is_refund = Column(Boolean)
    # payer = Column(String)
    # expense = Column(Integer)
    # installment = Column(Integer)
    # date = Column(String, index=True)
    # store = Column(String)
    # total_expense = Column(Integer)