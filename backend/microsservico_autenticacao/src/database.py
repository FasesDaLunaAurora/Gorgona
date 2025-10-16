from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Base = declarative_base()   

def pegar_sessao():
    try:
        Session = sessionmaker(bind=engine)
        db = Session()
        yield db
    finally:
        db.close()