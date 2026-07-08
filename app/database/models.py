from sqlalchemy import Column,Integer,String,Date,ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "Users"
    id              = Column(Integer,primary_key=True)
    username         = Column(String,nullable=False)
    email           = Column(String,nullable=False,unique=True)
    hashed_password = Column(String,nullable=False)

class Task(Base):
    __tablename__ = "Tasks"
    id          = Column(Integer,primary_key=True)
    title       = Column(String,nullable=False)
    description = Column(String)
    due_date    = Column(Date)
    priority    = Column(String,nullable=False)
    status      = Column(String,nullable=False)

    user_id = Column(Integer,ForeignKey("Users.id"))