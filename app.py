"""RadSafe pilot host: serves the self-contained RadSafe game inside Streamlit."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="RadSafe", page_icon="🛡️", layout="wide",
                   initial_sidebar_state="collapsed")
st.markdown(
    "<style>#MainMenu,footer,header{visibility:hidden}"
    ".block-container{padding:0!important;max-width:100%!important}</style>",
    unsafe_allow_html=True,
)

# Optional pilot access gate. Set PILOT_PASSWORD in Streamlit secrets to enable.
# This is a convenience gate for a pilot, NOT production authentication.
try:
    pw = st.secrets.get("PILOT_PASSWORD")
except Exception:
    pw = None
if pw and st.text_input("Pilot access code", type="password") != pw:
    st.info("Enter the pilot access code to continue.")
    st.stop()

html = (Path(__file__).parent / "radsafe.html").read_text(encoding="utf-8")
components.html(html, height=1100, scrolling=True)
