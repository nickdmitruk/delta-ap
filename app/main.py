import sys
import os
st.set_page_config(page_title="DELTA A.P.", layout="wide")
sys.path.append(os.path.abspath("app"))

import streamlit as st

# Импорт страниц
from app.pages.login import login
from app.pages.register import register
from app.pages.dashboard import dashboard
from app.pages.charts.charts import show as show_charts
from app.pages.macro.macro import show as show_macro
from app.pages.options.options import show as show_options
from app.pages.quant.quant import show as show_quant
from app.pages.portfolio.portfolio import show as show_portfolio
from app.pages.settings.settings import show as show_settings

# Импорт бокового меню
from app.components import sidebar

# Настройка страницы
st.set_page_config(page_title="DELTA A.P.", layout="wide")

# Инициализация session_state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "Login"

# Показ страницы в зависимости от состояния входа
if not st.session_state["logged_in"]:
    if st.session_state["page"] == "Register":
        register.show()
    else:
        login.show()
else:
    sidebar.show()
    page = st.session_state["page"]

    if page == "Home page":
        dashboard.show()
    elif page == "Chart analysis":
        show_charts()
    elif page == "Macroeconomics":
        show_macro()
    elif page == "Option analysis":
        show_options()
    elif page == "Quantitative analysis":
        show_quant()
    elif page == "Portfolio":
        show_portfolio()
    elif page == "Settings":
        show_settings()

