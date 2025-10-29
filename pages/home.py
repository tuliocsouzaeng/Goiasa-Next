import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

if not st.session_state.get("authenticated", False):
    st.warning("Você precisa fazer login para acessar esta página.")
    st.switch_page("index.py")  # Redireciona para a tela de login


st.title("Página Inicial")