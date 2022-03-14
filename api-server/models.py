from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Receipt(Base):
    __tablename__ = "receipt"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    from_ = Column("from", String)
    to = Column(String)
    message = Column(String)

class Receipt2(Base):
    __tablename__ = "receipt2"

    id = Column(Integer, primary_key=True, index=True)
    payer = Column(String)
    expense = Column(Integer)
    installment = Column(Integer)
    date = Column(String, index=True)
    store = Column(String)
    total_expense = Column(Integer)