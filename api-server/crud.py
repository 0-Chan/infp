from sqlalchemy.orm import Session

from . import models, schemas
import datetime

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# def create_receipt(db: Session, receipt: schemas.ReceiptCreate):
#     db_receipt = models.Receipt(date=receipt.date, from_=receipt.from_, to=receipt.to, message=receipt.message)
#     db.add(db_receipt)
#     db.commit()
#     db.refresh(db_receipt)
#     return db_receipt

def create_receipt(db: Session, receipt: schemas.ReceiptCreate):
    db_receipt = models.Receipt(**receipt.dict())
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt

def create_receipt2(db: Session, receipt: schemas.ReceiptCreate):
#     db_receipt = models.Receipt(date=receipt.date, from_=receipt.from_, to=receipt.to, message=receipt.message)
    message=receipt.message
    is_refund_tmp = True
    installment_tmp = 0

    split_lines = message.split("\n")
    row = [None] * len(split_lines)
    print(split_lines)

    for i in range (0,len(split_lines)):
        row[i] = split_lines[i].split(" ")

    if row[0][2] != "승인":
        is_refund_tmp = True

    if row[1][0] != "김*찬":
        payer_tmp = "hun"
    else:
        payer_tmp = "chan"

    expense_tmp = row[2][0][:-1]
    expense_tmp = int(expense_tmp.replace(',', ''))

    if row[2][1] != "일시불":
        installment_tmp = row[2][1][1:2]

    date_tmp = str(datetime.date.today().year)+ '-' + split_lines[3].replace('/', '-')

    store_tmp = split_lines[4]

    total_expense_tmp = int(split_lines[5][2:-1].replace(',', ''))

    db_receipt = models.Receipt2(is_refund=is_refund_tmp,
                                 payer=payer_tmp,
                                 expense=expense_tmp,
                                 installment=installment_tmp,
                                 date=date_tmp,
                                 store=store_tmp,
                                 total_expense=total_expense_tmp)
    
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt

# def create_receipt3(db: Session, receipt: schemas.Receipt3Create):
#   db_receipt = models.Receipt3(**receipt.dict())
#   db.add(db_receipt)
#   db.commit()
#   db.refresh(db_receipt)
#   return db_receipt

def create_receipt3(db: Session, receipt: schemas.Receipt3Create):
  # db_receipt = models.Receipt3(name=receipt3.name, pkg=receipt3.pkg, title=receipt3.title, text=receipt3.text, subtext=receipt3.subtext, bigtext=receipt3.bigtext, infotext=receipt3.infotext)
  db_receipt = models.Receipt3(**receipt.dict())
  db.add(db_receipt)
  db.commit()
  db.refresh(db_receipt)
  return db_receipt