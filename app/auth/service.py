from sqlalchemy.orm import Session
from app.database.models import User
from app.utils.security import hash_password
from fastapi import HTTPException
from app.utils.security import verify_password


def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return user


def create_user(db:Session,username:str,email:str,password:str):
    existing_user = get_user_by_email(db, email)

    if existing_user is not None:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )
    hashed_password = hash_password(password)
    user = User(
        username = username,
        email = email,
        hashed_password = hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email==email).first()