import datetime
from numpy import average
import streamlit as st

st.set_page_config(layout="wide", page_title="Mip - Métricas")

def dados_metrica_leads_mes():
    df_leads = st.session_state["df_leads"]
    df_reservas = st.session_state["df_reservas"]
    # -----------------------------------------------------------------------------------
    # Media de Leads por mes
    ano = datetime.date.today().year
    mes = datetime.date.today().month
    leads_meses = list()

    for m in range(1, mes+1):
        df_filtrado_mes = df_leads[
        (df_leads["ultima_data_conversao"].dt.month == m) &
        (df_leads["ultima_data_conversao"].dt.year  == ano)
        ]
        leads_meses.append(len(df_filtrado_mes))

    media_leads_por_mes_ano = average(leads_meses) # !


    hoje = datetime.date.today()

    df_filtrado_desse_mes = df_leads[
        (df_leads["ultima_data_conversao"].dt.month == hoje.month) &
        (df_leads["ultima_data_conversao"].dt.year  == hoje.year)
    ]

    total_leads_desse_mes = len(df_filtrado_desse_mes) # !

    porcentagem_desse_mes = (100*total_leads_desse_mes) / media_leads_por_mes_ano # !
    delta = porcentagem_desse_mes - 100 # !

    return [total_leads_desse_mes, delta]