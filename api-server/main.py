# from typing import Optional

# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel

# from sqlalchemy.orm import Session

# from . import crud, models, schemas
# from .database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "wooooooooorrrrrrrrld"}

# @app.get("/api/")
# async def hello():
#     return {"msg":"Hello, this is API server"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str]):
#     return {"item_id": item_id, "q": q}

# class Contact(BaseModel):
#   contact_id:int
#   first_name:str
#   last_name:str
#   user_name:str
#   password:str

# class ContactOut(BaseModel):
#     contact_id:int
#     first_name:str
#     last_name:str
#     user_name:str

# # @app.post('/contact')
# # async def create_contact(contact: Contact):
# #     return contact

# @app.post('/contact', response_model=ContactOut)
# async def create_contact(contact: Contact):
#     return contact

import inspect
import logging
from typing import List, Type, Optional

from fastapi import Depends, FastAPI, HTTPException, Request, status, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from pydantic import BaseModel
import httpx

from . import crud, models, schemas
from .database import SessionLocal, engine
from pydantic.fields import ModelField

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


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# class AnyForm(BaseModel):
#     any_param: str

#     @classmethod
#     def as_form(
#         cls,
#         any_param: str = Form(...),
#     ) -> AnyForm:
#         return cls(any_param=any_param)


# class Test1(BaseModel):
#     a: str

# @as_form
# class Test(BaseModel):
#     name: str
#     pkg: str
#     title: str
#     text: str

# @app.post('/me', response_model=Test)
# async def me(request: Request, form: Test = Depends(Test.as_form)):
#     return form

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str}")
	content = {'status_code': 422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.post("/receipt", response_model=schemas.Receipt)
def create_receipt(receipt: schemas.ReceiptCreate, db: Session = Depends(get_db)):
    return crud.create_receipt(db=db, receipt=receipt)

@app.post("/receipt2", response_model=schemas.Receipt2)
def create_receipt2(receipt: schemas.ReceiptCreate, db: Session = Depends(get_db)):
    return crud.create_receipt2(db=db, receipt=receipt)

@app.post("/receipt3", response_model=schemas.Receipt2)
async def create_receipt3(request: Request, form: schemas.Receipt3Form = Depends(schemas.Receipt3Base.as_form), db: Session = Depends(get_db)):
    msg = {"text": form.bigtext}
    print(msg)
    async with httpx.AsyncClient() as client:
        response = await client.post('https://hooks.slack.com/services/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', json=msg)
        # URL hardcode part has to be changed.
    return crud.create_receipt3(db=db, receipt=form)
    # return form

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items