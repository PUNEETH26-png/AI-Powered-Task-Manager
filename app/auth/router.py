from fastapi import APIRouter
from app.auth.schema import SignupRequest,UserReponse,LoginRequest
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.auth.service import create_user,get_user_by_email,login_user
from app.database.dependencies import get_db
from fastapi import HTTPException
router = APIRouter()

@router.post("/signup")
def signup(user : SignupRequest,db:Session = Depends(get_db)):
    new_user = create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password
        )
    return new_user

@router.get("/User/{email}",response_model=UserReponse)
def get_user(email:str,db:Session=Depends(get_db)):
    user = get_user_by_email(db=db,email=email)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@router.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)):
    return login_user(
        db=db,
        email=user.email,
        password=user.password
    )

