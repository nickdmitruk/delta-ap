# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Создаём движок для SQLite
DATABASE_URL = "sqlite:///app/db/users.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаём сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс моделей
Base = declarative_base()
