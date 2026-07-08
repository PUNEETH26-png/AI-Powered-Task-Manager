from pydantic import BaseModel,EmailStr,ConfigDict

class SignupRequest(BaseModel):
    username : str
    password : str
    email    : EmailStr

class LoginRequest(BaseModel):
    email    : EmailStr
    password : str

class UserReponse(BaseModel):
    id : int
    username : str
    email : EmailStr
    model_config = ConfigDict(from_attributes=True)

