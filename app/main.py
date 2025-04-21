import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.style.colors import BG_COLOR, ACCENT_GREEN
from PIL import Image
import plotly.express as px
import pandas as pd

# Настройка страницы
st.set_page_config(
    page_title="DELTA A.P.",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Квантовая платформа макроаналитики и визуализации рынков."
    }
)

logo_path = "app/assets/logos/delta_main_logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=180)

# Стилизация
st.markdown(f"""
    <style>
        body, .stApp {{
            background-color: {BG_COLOR};
            font-family: 'Century Gothic', sans-serif;
            color: white;
        }}
    </style>
""", unsafe_allow_html=True)

st.title("🧠 DELTA A.P.")
st.markdown("Добро пожаловать в квантовую аналитическую платформу!")

# График
df = pd.DataFrame({
    "Дата": pd.date_range("2023-01-01", periods=10),
    "S&P500": [3900, 3920, 3915, 3950, 3975, 3960, 3990, 4000, 4025, 4040]
})

fig = px.line(df, x="Дата", y="S&P500", title="S&P500 динамика")
fig.update_layout(
    paper_bgcolor="#181818",
    plot_bgcolor="#181818",
    font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True)
