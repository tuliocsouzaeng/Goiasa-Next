import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px


if not st.session_state.get("authenticated", False):
    st.warning("Você precisa fazer login para acessar esta página.")
    st.switch_page("index.py")  # Redireciona para a tela de login

st.title("Tanques")

# Dados
tanques = pd.read_csv("data/tanques.csv", sep=";", encoding='utf-8')

# Seção expansível para filtros
with st.expander("Abrir Filtros"):
    setor_selecionado = st.multiselect("Selecione o Setor", tanques["SETOR"].dropna().unique().tolist())
    material_selecionado = st.multiselect("Selecione o Material", tanques["MATERIAL"].dropna().unique().tolist())
    criticidade_selecionada = st.multiselect("Selecione a Criticidade", tanques["CRITICIDADE"].dropna().unique().tolist())
    equipamento_selecionado = st.multiselect("Selecione o Equipamento", tanques["TAG"].dropna().unique().tolist())


st.subheader("Detalhes dos Equipamentos Filtrados")
st.dataframe(tanques, height=400)