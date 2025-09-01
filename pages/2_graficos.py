import datetime
import streamlit as st

st.set_page_config(layout="wide", page_title="Mip - Grafico Andamento Leads")

df_leads = st.session_state["df_leads"]
df_reservas = st.session_state["df_reservas"]


# Leads/Situação
col1, col2 = st.columns(2)
col1.title("Leads/Situação")
date_range = col2.date_input( # cria o filtro e pega o range
    label="Data",
    value=(datetime.date(2020, 5, 15), datetime.date.today() - datetime.timedelta(days=1)),
    min_value=datetime.date(2020, 5, 15),
    max_value=datetime.date.today()
)
start, end = date_range # pega o range

df_filtrado = df_leads[(df_leads["ultima_data_conversao"] >= start) & (df_leads["ultima_data_conversao"] <= end)]

# agrupa e conta
dados = (
    df_filtrado.groupby("situacao")
    .size()
    .reset_index(name="Leads")
    # .sort_values("Leads", ascending=False)
)
st.area_chart(data=dados, x="situacao", y="Leads",
              x_label="Situação", y_label="Leads", height=700)