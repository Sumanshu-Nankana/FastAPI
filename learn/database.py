from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator

# For PostgreSQL Database
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# For SQLite Database
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./sqlite.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread" : False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
