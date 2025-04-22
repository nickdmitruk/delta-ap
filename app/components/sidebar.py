import streamlit as st

def show():
    with st.sidebar:
        st.image("app/assets/logos/delta_main_logo.png", width=150)
        st.markdown("### Навигация")

        page = st.radio("Страницы", [
            "Home page",
            "Chart analysis",
            "Macroeconomics",
            "Option analysis",
            "Quantitative analysis",
            "Portfolio",
            "Settings"
        ], key="sidebar_page")

        # Записываем выбор в session_state
        st.session_state["page"] = page

        st.markdown("---")
        if st.button("🚪 Выйти"):
            st.session_state["logged_in"] = False
            st.session_state["page"] = "Login"
            st.experimental_rerun()
