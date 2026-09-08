# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# TODO: при переносе на сервер можно поменять DATABASE_URL на PostgreSQL
# Например: "postgresql://user:password@host:5432/ngatu_db"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ngatu.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # для SQLite
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
