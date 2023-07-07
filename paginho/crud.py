from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Session
from models import User, Transaction
from schemas import UserSchema

from datetime import datetime

def create_user(db: Session, user: UserSchema):
    _user = User(email=user.email,
                name=user.name, 
                password=user.password, 
                cuit=user.cuit, 
                phoneNumber=user.phoneNumber)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


# Transactions
def create_transaction(db: Session, cbuFrom: str, cbuTo: str, amount: float):
    formattedDatetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _transaction = Transaction(time= formattedDatetime, cbuFrom=cbuFrom, cbuTo=cbuTo, amount=amount)
    db.add(_transaction)
    db.commit()
    db.refresh(_transaction)
    return _transaction
