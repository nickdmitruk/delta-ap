import streamlit as st
from app.components import auth

def show():
    st.markdown("### 🔐 Login to DELTA A.P.")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Пароль", type="password")
        login_btn = st.form_submit_button("Connect")

        if login_btn:
            if auth.login(email, password):
                st.success("Добро пожаловать в DELTA A.P.")
                st.session_state["logged_in"] = True
                st.session_state["user_email"] = email
                st.session_state["page"] = "Home page"
                st.experimental_rerun()
            else:
                st.error("Неверный email или пароль")

    st.markdown("Нет аккаунта? [Зарегистрироваться](#register)")
