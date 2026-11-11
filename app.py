from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SciPy from Zero", page_icon="🧪", layout="wide")

# Remove Streamlit's default top padding so the app fills the page
st.markdown(
    "<style>.block-container {padding-top: 1rem; padding-bottom: 0;}</style>",
    unsafe_allow_html=True,
)

# Load the app (HTML + CSS + JavaScript, with Python and SciPy running in the browser via Pyodide)
html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")

components.html(html, height=1100, scrolling=True)
