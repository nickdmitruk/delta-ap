import streamlit as st
from app.components import auth

def show():
    st.markdown("### 🆕 Регистрация нового пользователя")

    with st.form("register_form"):
        email = st.text_input("Email для регистрации")
        password = st.text_input("Пароль", type="password")
        password2 = st.text_input("Повторите пароль", type="password")
        register_btn = st.form_submit_button("Зарегистрироваться")

        if register_btn:
            if password != password2:
                st.warning("Пароли не совпадают")
            elif auth.register(email, password):
                st.success("Успешная регистрация! Теперь можно войти.")
                st.session_state["page"] = "Login"
                st.experimental_rerun()
            else:
                st.error("Пользователь с таким email уже существует")

    st.markdown("Уже есть аккаунт? [Войти](#login)")
