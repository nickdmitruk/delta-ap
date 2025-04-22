import streamlit as st
from app.pages.login import login
from app.pages.register import register
from app.pages.dashboard import dashboard  # временно заглушка

st.set_page_config(page_title="DELTA A.P.", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "Login"

# --- Переход по страницам ---
if not st.session_state["logged_in"]:
    if st.session_state["page"] == "Register":
        register.show()
    else:
        login.show()
else:
    dashboard.show()
