# app/core/auth.py
import streamlit as st
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import User
from passlib.context import CryptContext

# Контекст для хэширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def register_user(email: str, password: str) -> bool:
    db: Session = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            return False  # Пользователь уже существует
        hashed_password = get_password_hash(password)
        new_user = User(email=email, password_hash=hashed_password)
        db.add(new_user)
        db.commit()
        return True
    finally:
        db.close()

def authenticate_user(email: str, password: str) -> bool:
    db: Session = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return False
        return verify_password(password, user.password_hash)
    finally:
        db.close()

def login_user(email: str, password: str):
    if authenticate_user(email, password):
        st.session_state["logged_in"] = True
        st.session_state["page"] = "Home page"
        st.success("Logged in successfully")
    else:
        st.error("Incorrect email or password")
