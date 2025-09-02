import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Mip - Tabelas + Leads")
# --------------------------------------------
# Real Mode
from auto.leads import get_leads
from auto.reservas import get_reservas

@st.cache_data(ttl=7200) # atualiza a cada 2 horas
def load_data():
    df_leads = get_leads()
    df_reservas = get_reservas()
    return [df_leads, df_reservas]

df_leads, df_reservas = load_data()
# --------------------------------------------
# Dev Mode
# from dev.info.get_leads_dev import get_leads
# from dev.info.get_reservas_dev import get_reservas

# df_leads = get_leads()
# df_reservas = get_reservas()
# --------------------------------------------
#Session State

st.session_state["df_leads"] = df_leads
st.session_state["df_reservas"] = df_reservas

# --------------------------------------------
# FILTROS
st.sidebar.header("Filtros")

# Filtros Lead
col1, col2 = st.sidebar.columns(2) # colunas + toggle
col1.subheader("Leads")
active = col2.toggle(label="", value=False, key=1)

if active:
    # Initialize filtered_df_leads with the original dataframe
    filtered_df_leads = df_leads.copy()

    # Filters for Leads
    nome_lead_selected = st.sidebar.selectbox(label="Nome do Lead", options=df_leads["nome"].unique(), placeholder="Escolha uma opção", index=None)
    if nome_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["nome"] == nome_lead_selected]

    email_lead_selected = st.sidebar.selectbox(label="Email do Lead", options=df_leads["email"].unique(), index=None, placeholder="Escolha uma opção")
    if email_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["email"] == email_lead_selected]

    gestor_lead_selected = st.sidebar.selectbox(label="Gestor", options=df_leads["gestor"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if gestor_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["gestor"] == gestor_lead_selected]

    imobiliaria_lead_selected = st.sidebar.selectbox(label="Imobiliária", options=df_leads["imobiliaria"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if imobiliaria_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["imobiliaria"] == imobiliaria_lead_selected]

    corretor_lead_selected = st.sidebar.selectbox(label="Corretor", options=df_leads["corretor"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if corretor_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["corretor"] == corretor_lead_selected]

    situacao_lead_selected = st.sidebar.selectbox(label="Situação", options=df_leads["situacao"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if situacao_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["situacao"] == situacao_lead_selected]

    telefone_lead_selected = st.sidebar.selectbox(label="Telefone", options=df_leads["telefone"].unique(), index=None, placeholder="Escolha uma opção")
    if telefone_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["telefone"] == telefone_lead_selected]

    data_cad_lead_selected = st.sidebar.selectbox(label="Data de Cadastro", options=df_leads["data_cad"].unique(), index=None, placeholder="Escolha uma opção")
    if data_cad_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["data_cad"] == data_cad_lead_selected]

    midia_principal_lead_selected = st.sidebar.selectbox(label="Mídia Principal", options=df_leads["midia_principal"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if midia_principal_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["midia_principal"] == midia_principal_lead_selected]

    documento_lead_selected = st.sidebar.selectbox(label="Documento", options=df_leads["documento"].unique(), index=None, placeholder="Escolha uma opção")
    if documento_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["documento"] == documento_lead_selected]

    sexo_lead_selected = st.sidebar.selectbox(label="Sexo", options=df_leads["sexo"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if sexo_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["sexo"] == sexo_lead_selected]

    estado_lead_selected = st.sidebar.selectbox(label="Estado", options=df_leads["estado"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if estado_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["estado"] == estado_lead_selected]

    cidade_lead_selected = st.sidebar.selectbox(label="Cidade", options=df_leads["cidade"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if cidade_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["cidade"] == cidade_lead_selected]

    bairro_lead_selected = st.sidebar.selectbox(label="Bairro", options=df_leads["bairro"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if bairro_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["bairro"] == bairro_lead_selected]

    origem_lead_selected = st.sidebar.selectbox(label="Origem", options=df_leads["origem"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if origem_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["origem"] == origem_lead_selected]

    ultima_data_conversao_lead_selected = st.sidebar.selectbox(label="Última Data de Conversão", options=df_leads["ultima_data_conversao"].unique(), index=None, placeholder="Escolha uma opção")
    if ultima_data_conversao_lead_selected:
        filtered_df_leads = filtered_df_leads[filtered_df_leads["ultima_data_conversao"] == ultima_data_conversao_lead_selected]

    # empreendimento_lead_selected = st.sidebar.selectbox(label="Empreendimento", options=df_leads["empreendimento"].value_counts().index, index=None, placeholder="Escolha uma opção")
    # if empreendimento_lead_selected:
    #     filtered_df_leads = filtered_df_leads[filtered_df_leads["empreendimento"] == empreendimento_lead_selected]

    # midias_lead_selected = st.sidebar.selectbox(label="Mídias", options=df_leads["midias"].value_counts().index, index=None, placeholder="Escolha uma opção")
    # if midias_lead_selected:
    #     filtered_df_leads = filtered_df_leads[filtered_df_leads["midias"] == midias_lead_selected]
else:
    filtered_df_leads = df_leads.copy() # Ensure filtered_df_leads is defined even if not active

st.session_state["df_leads"] = filtered_df_leads

# Filtros Reserva
col3, col4 = st.sidebar.columns(2) # colunas + toggle
col3.subheader("Reservas")
active_ = col4.toggle(label="", value=False, key=2)

if active_:
    # Initialize filtered_df_reservas with the original dataframe
    filtered_df_reservas = df_reservas.copy()

    # Filters for Reservas
    vendida_reserva_selected = st.sidebar.selectbox(label="Vendida", options=df_reservas["vendida"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if vendida_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["vendida"] == vendida_reserva_selected]

    data_reserva_selected = st.sidebar.selectbox(label="Data", options=df_reservas["data"].unique(), index=None, placeholder="Escolha uma opção")
    if data_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["data"] == data_reserva_selected]

    data_venda_reserva_selected = st.sidebar.selectbox(label="Data de Venda", options=df_reservas["data_venda"].unique(), index=None, placeholder="Escolha uma opção")
    if data_venda_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["data_venda"] == data_venda_reserva_selected]

    situacao_reserva_selected = st.sidebar.selectbox(label="Situação", options=df_reservas["situacao_situacao"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if situacao_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["situacao_situacao"] == situacao_reserva_selected]

    idlead_reserva_selected = st.sidebar.selectbox(label="ID Lead", options=df_reservas["idlead"].map(lambda x: str(x).replace(".0", "")).unique(), index=None, placeholder="Escolha uma opção")
    if idlead_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["idlead"].map(lambda x: str(x).replace(".0", "")) == idlead_reserva_selected]

    unidade_empreendimento_reserva_selected = st.sidebar.selectbox(label="Unidade Empreendimento", options=df_reservas["unidade_empreendimento"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if unidade_empreendimento_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["unidade_empreendimento"] == unidade_empreendimento_reserva_selected]

    unidade_tipo_reserva_selected = st.sidebar.selectbox(label="Unidade Tipo", options=df_reservas["unidade_tipo"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if unidade_tipo_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["unidade_tipo"] == unidade_tipo_reserva_selected]

    titular_nome_reserva_selected = st.sidebar.selectbox(label="Titular Nome", options=df_reservas["titular_nome"].unique(), index=None, placeholder="Escolha uma opção")
    if titular_nome_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["titular_nome"] == titular_nome_reserva_selected]

    titular_nascimento_reserva_selected = st.sidebar.selectbox(label="Titular Nascimento", options=df_reservas["titular_nascimento"].unique(), index=None, placeholder="Escolha uma opção")
    if titular_nascimento_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["titular_nascimento"] == titular_nascimento_reserva_selected]

    titular_sexo_reserva_selected = st.sidebar.selectbox(label="Titular Sexo", options=df_reservas["titular_sexo"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if titular_sexo_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["titular_sexo"] == titular_sexo_reserva_selected]

    titular_como_ficou_sabendo_reserva_selected = st.sidebar.selectbox(label="Como Ficou Sabendo", options=df_reservas["titular_como_ficou_sabendo"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if titular_como_ficou_sabendo_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["titular_como_ficou_sabendo"] == titular_como_ficou_sabendo_reserva_selected]

    corretor_corretor_reserva_selected = st.sidebar.selectbox(label="Corretor", options=df_reservas["corretor_corretor"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if corretor_corretor_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["corretor_corretor"] == corretor_corretor_reserva_selected]

    corretor_imobiliaria_reserva_selected = st.sidebar.selectbox(label="Imobiliária", options=df_reservas["corretor_imobiliaria"].value_counts().index, index=None, placeholder="Escolha uma opção")
    if corretor_imobiliaria_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["corretor_imobiliaria"] == corretor_imobiliaria_reserva_selected]

    condicoes_valor_contrato_reserva_selected = st.sidebar.selectbox(label="Valor do Contrato", options=df_reservas["condicoes_valor_contrato"].unique(), index=None, placeholder="Escolha uma opção")
    if condicoes_valor_contrato_reserva_selected:
        filtered_df_reservas = filtered_df_reservas[filtered_df_reservas["condicoes_valor_contrato"] == condicoes_valor_contrato_reserva_selected]
else:
    filtered_df_reservas = df_reservas.copy() # Ensure filtered_df_reservas is defined even if not active

st.session_state["df_reservas"] = filtered_df_reservas

# --------------------------------------------
# Main
from metrics.metrica_leads_mes import dados_metrica_leads_mes

total_leads_desse_mes, delta = dados_metrica_leads_mes()

col1, col2 = st.columns(2)
col1.title("Tabelas de Leads/Reservas")
col2.metric(label="Leads do Mês / Média", value=total_leads_desse_mes, delta=f"{delta:.2f}%")
st.subheader("Tabela de Leads")
st.dataframe(filtered_df_leads)
st.subheader("Tabela de Reservas")
st.dataframe(filtered_df_reservas)

