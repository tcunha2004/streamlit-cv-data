import datetime
import streamlit as st

st.set_page_config(layout="wide", page_title="Mip - Métricas")

df_leads = st.session_state["df_leads"]
df_reservas = st.session_state["df_reservas"]

hoje = datetime.date.today()

df_filtrado = df_leads[
    (df_leads["ultima_data_conversao"].dt.month == hoje.month) &
    (df_leads["ultima_data_conversao"].dt.year  == hoje.year)
]

st.write(len(df_filtrado))