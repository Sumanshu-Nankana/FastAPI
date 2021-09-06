from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator, Any

import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Base, User
from database import get_db
from main import app
from config import settings
from schemas import UserCreate
from hashing import Hasher

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client


@pytest.fixture
def token_headers(client: TestClient):
    test_email = settings.TEST_EMAIL
    test_password = settings.TEST_PASS
    db = TestingSessionLocal()
    user = db.query(User).filter(User.email == test_email).first()
    if not user:
        user_schema = UserCreate(email=test_email, password=test_password)
        user = User(
            email=user_schema.email,
            password=Hasher.get_hash_password(user_schema.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    data = {"username": test_email, "password": test_password}
    response = client.post("/login/token", data=data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
