import streamlit as st
from app.pages.login.login_buttons import (
    connect_button,
    register_button,
    diagnostic_tools_button,
    reserved_settings_button,
    update_channels_button,
)

# Настройки страницы — обязательно в самом начале!
st.set_page_config(page_title="Login | DELTA A.P.", layout="wide")

# Убираем меню и футер Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Основной CSS и структура
st.markdown("""
    <style>
        html, body, [data-testid="stApp"] {
            height: 100%;
            margin: 0;
            background-color: #262626;
            overflow: hidden;
        }
        .container {
            display: flex;
            height: 100vh;
            width: 100vw;
        }
        .left-side {
            flex: 1;
            padding: 50px;
        }
        .right-side {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
        }
        .input {
            width: 300px;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #1E1E1E;
            border: none;
            color: white;
            font-size: 16px;
            border-radius: 5px;
        }
        .button {
            width: 300px;
            background-color: #A2DD84;
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            margin-top: 10px;
            cursor: pointer;
        }
        .small-links {
            font-size: 13px;
            color: #868686;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="container">
        <div class="left-side">
            <img src="app/assets/logos/delta_main_logo.png" width="120"/>
            <img src="app/assets/images/login_background.jpg" width="100%" style="border-radius: 20px; margin-top: 20px;"/>
        </div>
        <div class="right-side">
            <img src="app/assets/icons/login_icon.png" width="48"/>
            <h1 style="font-family: Gotham Medium;">Login to Delta</h1>
            <p style="color: #868686;">Sign in to get access to your dashboard</p>
""", unsafe_allow_html=True)

# Поля логина
email = st.text_input("Email or account ID", key="email_input")
password = st.text_input("Password", type="password", key="password_input")

# Кнопка Connect
connect_button(email, password)

# Register
register_button()

# Ссылки внизу
st.markdown("""
    <div style="text-align: left; font-size: 13px; margin-top: 30px;">
""", unsafe_allow_html=True)

diagnostic_tools_button()
reserved_settings_button()
update_channels_button()

st.markdown("</div></div></div>", unsafe_allow_html=True)
