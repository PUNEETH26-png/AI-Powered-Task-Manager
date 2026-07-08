from fastapi import FastAPI
from app.database.database import Base,engine
from app.database import models
from app.auth.router import router as auth_router
from app.tasks.router import router as task_router
from app.ai.router import router as ai_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(task_router)
app.include_router(ai_router)
@app.get("/")
def home():
    return {"message" : "Task manager API is running"}