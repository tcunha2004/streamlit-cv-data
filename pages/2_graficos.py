import datetime
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", page_title="Mip - Grafico Andamento Leads")

df_leads = st.session_state["df_leads"]
df_reservas = st.session_state["df_reservas"]

# --------------------------------------------------------------

# Leads/Mês
col1_, col2_ = st.columns(2)
col1_.title("Leads/Mês")
date_range_ = col2_.date_input(
    key=1,
    label="Data",
    value=(datetime.date(2020, 5, 15), datetime.date.today() - datetime.timedelta(days=1)),
    min_value=datetime.date(2020, 5, 15),
    max_value=datetime.date.today()
)
start_, end_ = date_range_

# filtra pelo range
df_filtrado_ = df_leads[
    (pd.to_datetime(df_leads["ultima_data_conversao"]).dt.date >= start_) &
    (pd.to_datetime(df_leads["ultima_data_conversao"]).dt.date <= end_)
]

# cria coluna mês (primeiro dia do mês) e etiqueta amigável
dados_ = (
    df_filtrado_
    .assign(
        mes=lambda d: pd.to_datetime(d["ultima_data_conversao"]).dt.to_period("M").dt.to_timestamp(),
        mes_label=lambda d: pd.to_datetime(d["ultima_data_conversao"]).dt.strftime("%Y-%m-%d")  
    )
    .groupby("mes", as_index=False)
    .size()
    .rename(columns={"size": "Leads"})
    .sort_values("mes")
)

# opcional: se preferir o rótulo texto no eixo X, use x="mes_label"
st.bar_chart(
    data=dados_,
    x="mes",              # eixo X como data mensal (fica bonito e ordenado)
    y="Leads",
    x_label="Mês",
    y_label="Leads",
    height=500,
    stack=True
)

#---------------------------------------------------------------------------------------------------------------------

# Leads/Situação
col1, col2 = st.columns(2)
col1.title("Leads/Situação")
date_range = col2.date_input( # cria o filtro e pega o range
    key=2,
    label="Data",
    value=(datetime.date(2020, 5, 15), datetime.date.today() - datetime.timedelta(days=1)),
    min_value=datetime.date(2020, 5, 15),
    max_value=datetime.date.today()
)
start, end = date_range # pega o range

df_filtrado = df_leads[(df_leads["ultima_data_conversao"].dt.date >= start) & (df_leads["ultima_data_conversao"].dt.date <= end)]

# agrupa e conta
dados = (
    df_filtrado.groupby("situacao")
    .size()
    .reset_index(name="Leads")
)
st.bar_chart(
    data=dados, 
    x="situacao", 
    y="Leads",
    x_label="Situação", 
    y_label="Leads", 
    height=650, 
    stack=True
)