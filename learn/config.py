import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class Settings:
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.0.1"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "db_jobcard")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    ALGORITHM = "HS256"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    TEST_EMAIL: str = "test1@test.com"
    TEST_PASS: str = "test1pass"
    TEST_ITEM: str = "testitem"
    TEST_ITEM_DESC: str = "testitem description"


settings = Settings()
