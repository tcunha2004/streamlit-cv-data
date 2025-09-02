# bibliotecas
import requests
import pandas as pd
import streamlit as st

def get_leads():
    print("Iniciando get_leads...")

    # Parâmetros de autenticação do CV
    headers = {
        "accept": "application/json",
        "email": "thiago.cunha@mip.com.br",
        "token": st.secrets["token"]
    }

    # URL da API de leads
    url_base = "https://mip.cvcrm.com.br/api/cvio/lead"

    # limite de leads por requisicao
    limit = 1000
    offset = 0
    todos_leads = []

    print("Coletando dados da API leads...")

    # loop de requisicoes para pegar todos os leads
    while True:
        params = {
            "limit": str(limit),
            "offset": str(offset)
        }

        # faz a requisicao
        response = requests.get(url_base, headers=headers, params=params)
        dados = response.json()

        # se nao tiver mais leads, para o loop
        if "leads" not in dados or not dados["leads"]:
            break

        # adiciona no array
        todos_leads.extend(dados["leads"])
        offset += limit

        if offset >= dados.get("total", 0):
            break

    print("Dados de leads coletados com sucesso.")

    # Converte em DataFrame
    df = pd.DataFrame(todos_leads)
    df = df[[
        "idlead", "nome", "email", "gestor", "imobiliaria", "corretor", "situacao", "telefone", "data_cad",
        "midia_principal", "documento", "sexo", "estado", "cidade", "bairro", "origem", "ultima_data_conversao",
        "empreendimento", "midias"
    ]]

    # Valor das coluna correto
    df["gestor"] = df["gestor"].map(lambda x: x["nome"] if x["nome"] else None) # pega o "nome" caso haja algum
    df["imobiliaria"] = df["imobiliaria"].map(lambda x: x["nome"] if x["nome"] else None)
    df["corretor"] = df["corretor"].map(lambda x: x["nome"] if x["nome"] else None)
    df["situacao"] = df["situacao"].map(lambda x: x["nome"] if x["nome"] else None)
    df["telefone"] = df["telefone"].map(lambda x: str(x).replace(".0", "") if pd.notnull(x) else None)
    df["data_cad"] = pd.to_datetime(df["data_cad"], errors="coerce")
    df["ultima_data_conversao"] = pd.to_datetime(df["ultima_data_conversao"], errors="coerce")
    df["empreendimento"]= df["empreendimento"].map(lambda x: [item["nome"] for item in x] if isinstance(x, list) else None)

    return df