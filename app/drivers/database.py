from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config

try:
    
    DATABASE_URL = config('DATABASE_URL')

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autoflush=False)
    Base = declarative_base()
    
except Exception as e:
    raise e

def get_db_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()