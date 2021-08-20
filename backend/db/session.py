from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# For postgrSQL database
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# For SQlLite Database
# By default SQLite will only allow one thread to communicate.
# But in FastAPI, more than one thread can interact with the database
# Thus we need to override default parameter and thus setting check_same_thread : False
# This is required only for SQLite database

#SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
