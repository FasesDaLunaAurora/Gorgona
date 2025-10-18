from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não está definida no container")

engine = create_engine(DATABASE_URL)  
Base = declarative_base() 

def pegar_sessao():
    try:
        Session = sessionmaker(bind=engine)
        db = Session()
        yield db
    finally:
        db.close()