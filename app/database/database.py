from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABSE_URL = "sqlite:///./task_manager.db"
engine = create_engine(
    DATABSE_URL,
    connect_args={"check_same_thread" : False}
)

SessionLocal = sessionmaker(autoflush=False,bind=engine)
Base = declarative_base()