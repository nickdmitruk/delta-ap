import streamlit as st
import os
import base64
from app.core.auth import login_user

st.set_page_config(page_title="Login | DELTA A.P.", layout="wide")

def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def show():
    bg_image = get_base64_image("app/assets/images/login_background.jpg")
    logo_image = get_base64_image("app/assets/logos/delta_main_logo.png")
    icon_image = get_base64_image("app/assets/icons/login_icon.png")

    st.markdown(f"""
        <style>
        html, body, [data-testid="stApp"] {{
            margin: 0 !important;
            padding: 0 !important;
            height: 100vh !important;
            width: 100vw !important;
            overflow: hidden !important;
        }}
        section.main {{
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
        }}
        .block-container {{
            padding: 0rem !important;
        }}
        .full-page {{
            display: flex;
            height: 100vh;
            width: 100vw;
        }}
        .login-left {{
            flex: 1;
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            position: relative;
        }}
        .login-left img {{
            position: absolute;
            top: 2rem;
            left: 2rem;
            width: 120px;
        }}
        .login-right {{
            flex: 1;
            background-color: #1c1c1c;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }}
        .login-box {{
            width: 100%;
            max-width: 400px;
            color: white;
        }}
        .login-box h1 {{
            font-size: 2rem;
            margin-bottom: 1rem;
        }}
        .login-box input {{
            width: 100%;
            margin-bottom: 1rem;
            padding: 0.75rem;
            border: none;
            border-radius: 5px;
        }}
        .login-button {{
            background-color: #A2DD84;
            color: black;
            padding: 0.75rem;
            text-align: center;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
        }}
        .forgot-password {{
            text-align: right;
            color: #A2DD84;
            font-size: 0.9rem;
            margin-top: -0.5rem;
            margin-bottom: 1rem;
        }}
        .tools {{
            text-align: left;
            margin-top: 3rem;
            font-size: 0.85rem;
        }}
        .tools a {{
            color: white;
            text-decoration: underline;
            display: block;
            margin-bottom: 0.5rem;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="full-page">
        <div class="login-left">
            <img src="data:image/png;base64,{logo_image}" alt="Delta Logo">
        </div>
        <div class="login-right">
            <div class="login-box">
                <img src="data:image/png;base64,{icon_image}" width="48">
                <h1>Login to Delta</h1>
                <p>Sign in to get access to your dashboard</p>
                <form action="#" method="post">
                    <input type="text" name="email" placeholder="Email or account ID">
                    <input type="password" name="password" placeholder="Password">
                    <div class="forgot-password">Forgot password?</div>
                    <div class="login-button">Connect</div>
                </form>
                <div style="margin-top: 1rem; font-size: 0.85rem;">
                    Don’t have an account? <a href="#">Register</a>
                </div>
                <div class="tools">
                    <a href="#">Diagnostic tools</a>
                    <a href="#">Reserved settings</a>
                    <a href="#">Update channels</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
