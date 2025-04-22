import streamlit as st
import json
import os
import hashlib
from streamlit.runtime.scriptrunner import get_script_run_ctx, RerunException

def rerun():
    raise RerunException(get_script_run_ctx())

def save_user(email, password):
    users = {}
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            users = json.load(file)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[email] = hashed_password

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def show():
    st.markdown("## 📝 Регистрация в DELTA A.P.")

    email = st.text_input("Email")
    password = st.text_input("Пароль", type="password")
    password2 = st.text_input("Повторите пароль", type="password")

    if st.button("Зарегистрироваться"):
        if password != password2:
            st.warning("Пароли не совпадают")
        elif email.strip() == "" or password.strip() == "":
            st.warning("Заполните все поля")
        else:
            save_user(email, password)
            st.success("Аккаунт создан. Теперь войдите.")
            st.session_state["page"] = "Login"
            rerun()

    st.markdown("---")
    st.write("Уже есть аккаунт?")
    if st.button("Вернуться к входу"):
        st.session_state["page"] = "Login"
        rerun()
