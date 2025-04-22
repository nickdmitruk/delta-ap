import streamlit as st
import json
import os
import hashlib
from streamlit.runtime.scriptrunner import get_script_run_ctx, RerunException

def rerun():
    raise RerunException(get_script_run_ctx())

def load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as file:
        return json.load(file)

def verify_user(email, password):
    users = load_users()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return email in users and users[email] == hashed_password

def show():
    st.markdown("## 🔐 Login to DELTA A.P.")

    email = st.text_input("Email")
    password = st.text_input("Пароль", type="password")

    if st.button("Connect"):
        if verify_user(email, password):
            st.session_state["logged_in"] = True
            st.session_state["page"] = "Home page"
            st.success("Успешный вход")
            rerun()
        else:
            st.error("Неверный email или пароль")

    st.markdown("---")
    st.write("Нет аккаунта?")
    if st.button("Зарегистрироваться"):
        st.session_state["page"] = "Register"
        rerun()
