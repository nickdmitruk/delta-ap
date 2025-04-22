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
        html, body, [data-testid="stApp"], .main, .block-container {{
            margin: 0;
            padding: 0;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            font-family: 'Gotham', sans-serif;
        }}
        .full-page {{
            display: flex;
            height: 100vh;
            width: 100vw;
            background-color: #262626;
        }}
        .login-left {{
            width: 60%;
            height: calc(100vh - 100px);
            margin: 35px 0 35px 35px;
            border-radius: 24px;
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            position: relative;
            overflow: hidden;
        }}
        .login-left img.logo {{
            position: absolute;
            top: 30px;
            left: 30px;
            width: 120px;
        }}
        .login-right {{
            flex: 1;
            background-color: #262626;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 2rem;
        }}
        .login-box {{
            width: 100%;
            max-width: 400px;
            color: white;
            text-align: left;
            margin: 0 auto;
        }}
        .login-box h1 {{
            font-size: 2rem;
            font-weight: 500;
            margin: 0.25rem 0;
        }}
        .login-box p {{
            font-weight: 300;
            font-size: 0.95rem;
            color: #868686;
            margin: 0 0 1.5rem 0;
        }}
        .login-box input {{
            width: 100%;
            margin-bottom: 1rem;
            padding: 0.75rem;
            border: none;
            border-radius: 5px;
            background-color: #1E1E1E;
            color: white;
        }}
        .login-button {{
            background-color: #A2DD84;
            color: black;
            padding: 0.75rem;
            text-align: center;
            font-weight: 300;
            border-radius: 5px;
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
        .register-section {{
            margin-top: 1rem;
            font-size: 0.85rem;
            text-align: center;
        }}
        .register-section span {{
            color: #868686;
            font-weight: 300;
        }}
        .register-section a {{
            color: white;
            font-weight: 500;
            text-decoration: none;
            margin-left: 4px;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="full-page">
        <div class="login-left">
            <img src="data:image/png;base64,{logo_image}" class="logo" alt="Delta Logo">
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
                <div class="register-section">
                    <span>Don’t have an account?</span>
                    <a href="#">Register</a>
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