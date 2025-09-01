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
    nome_lead = df_leads["nome"]
    st.sidebar.selectbox(label="Nome do Lead", options=nome_lead, index=None, placeholder="Escolha uma opção")
    email_lead = df_leads["email"]
    st.sidebar.selectbox(label="Email do Lead", options=email_lead, index=None, placeholder="Escolha uma opção")
    gestor_lead = df_leads["gestor"].value_counts().index
    st.sidebar.selectbox(label="Gestor", options=gestor_lead, index=None, placeholder="Escolha uma opção")
    imobiliaria_lead = df_leads["imobiliaria"].value_counts().index
    st.sidebar.selectbox(label="Imobiliária", options=imobiliaria_lead, index=None, placeholder="Escolha uma opção")
    corretor_lead = df_leads["corretor"].value_counts().index
    st.sidebar.selectbox(label="Corretor", options=corretor_lead, index=None, placeholder="Escolha uma opção")
    situacao_lead = df_leads["situacao"].value_counts().index
    st.sidebar.selectbox(label="Situação", options=situacao_lead, index=None, placeholder="Escolha uma opção")
    telefone_lead = df_leads["telefone"]
    st.sidebar.selectbox(label="Telefone", options=telefone_lead, index=None, placeholder="Escolha uma opção")
    data_cad_lead = df_leads["data_cad"]
    st.sidebar.selectbox(label="Data de Cadastro", options=data_cad_lead, index=None, placeholder="Escolha uma opção")
    midia_principal_lead = df_leads["midia_principal"].value_counts().index
    st.sidebar.selectbox(label="Mídia Principal", options=midia_principal_lead, index=None, placeholder="Escolha uma opção")
    documento_lead = df_leads["documento"]
    st.sidebar.selectbox(label="Documento", options=documento_lead, index=None, placeholder="Escolha uma opção")
    sexo_lead = df_leads["sexo"].value_counts().index
    st.sidebar.selectbox(label="Sexo", options=sexo_lead, index=None, placeholder="Escolha uma opção")
    estado_lead = df_leads["estado"].value_counts().index
    st.sidebar.selectbox(label="Estado", options=estado_lead, index=None, placeholder="Escolha uma opção")
    cidade_lead = df_leads["cidade"].value_counts().index
    st.sidebar.selectbox(label="Cidade", options=cidade_lead, index=None, placeholder="Escolha uma opção")
    bairro_lead = df_leads["bairro"].value_counts().index
    st.sidebar.selectbox(label="Bairro", options=bairro_lead, index=None, placeholder="Escolha uma opção")
    origem_lead = df_leads["origem"].value_counts().index
    st.sidebar.selectbox(label="Origem", options=origem_lead, index=None, placeholder="Escolha uma opção")
    ultima_data_conversao_lead = df_leads["ultima_data_conversao"]
    st.sidebar.selectbox(label="Última Data de Conversão", options=ultima_data_conversao_lead, index=None, placeholder="Escolha uma opção")
    empreendimento_lead = df_leads["empreendimento"].value_counts().index
    st.sidebar.selectbox(label="Empreendimento", options=empreendimento_lead, index=None, placeholder="Escolha uma opção")
    midias_lead = df_leads["midias"].value_counts().index
    st.sidebar.selectbox(label="Mídias", options=midias_lead, index=None, placeholder="Escolha uma opção")

# Filtros Reserva
col3, col4 = st.sidebar.columns(2) # colunas + toggle
col3.subheader("Reservas")
active_ = col4.toggle(label="", value=False, key=2)

if active_:
    vendida_reserva = df_reservas["vendida"].value_counts().index
    st.sidebar.selectbox(label="Vendida", options=vendida_reserva, index=None, placeholder="Escolha uma opção")
    data_reserva = df_reservas["data"]
    st.sidebar.selectbox(label="Data", options=data_reserva, index=None, placeholder="Escolha uma opção")
    data_venda_reserva = df_reservas["data_venda"]
    st.sidebar.selectbox(label="Data de Venda", options=data_venda_reserva, index=None, placeholder="Escolha uma opção")
    situacao_reserva = df_reservas["situacao_situacao"].value_counts().index
    st.sidebar.selectbox(label="Situação", options=situacao_reserva, index=None, placeholder="Escolha uma opção")
    idlead_reserva = df_reservas["idlead"].map(lambda x: str(x).replace(".0", ""))
    st.sidebar.selectbox(label="ID Lead", options=idlead_reserva, index=None, placeholder="Escolha uma opção")
    unidade_empreendimento_reserva = df_reservas["unidade_empreendimento"].value_counts().index
    st.sidebar.selectbox(label="Unidade Empreendimento", options=unidade_empreendimento_reserva, index=None, placeholder="Escolha uma opção")
    unidade_tipo_reserva = df_reservas["unidade_tipo"].value_counts().index
    st.sidebar.selectbox(label="Unidade Tipo", options=unidade_tipo_reserva, index=None, placeholder="Escolha uma opção")
    titular_nome_reserva = df_reservas["titular_nome"]
    st.sidebar.selectbox(label="Titular Nome", options=titular_nome_reserva, index=None, placeholder="Escolha uma opção")
    titular_nascimento_reserva = df_reservas["titular_nascimento"]
    st.sidebar.selectbox(label="Titular Nascimento", options=titular_nascimento_reserva, index=None, placeholder="Escolha uma opção")
    titular_sexo_reserva = df_reservas["titular_sexo"].value_counts().index
    st.sidebar.selectbox(label="Titular Sexo", options=titular_sexo_reserva, index=None, placeholder="Escolha uma opção")
    titular_como_ficou_sabendo_reserva = df_reservas["titular_como_ficou_sabendo"].value_counts().index
    st.sidebar.selectbox(label="Como Ficou Sabendo", options=titular_como_ficou_sabendo_reserva, index=None, placeholder="Escolha uma opção")
    corretor_corretor_reserva = df_reservas["corretor_corretor"].value_counts().index
    st.sidebar.selectbox(label="Corretor", options=corretor_corretor_reserva, index=None, placeholder="Escolha uma opção")
    corretor_imobiliaria_reserva = df_reservas["corretor_imobiliaria"].value_counts().index
    st.sidebar.selectbox(label="Imobiliária", options=corretor_imobiliaria_reserva, index=None, placeholder="Escolha uma opção")
    condicoes_valor_contrato_reserva = df_reservas["condicoes_valor_contrato"]
    st.sidebar.selectbox(label="Valor do Contrato", options=condicoes_valor_contrato_reserva, index=None, placeholder="Escolha uma opção")
    
# --------------------------------------------

# Main
st.title("Tabelas de Leads/Reservas")
st.subheader("Tabela de Leads")
st.dataframe(df_leads)
st.subheader("Tabela de Reservas")
st.dataframe(df_reservas)

