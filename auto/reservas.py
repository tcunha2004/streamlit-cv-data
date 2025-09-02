# bibliotecas
import requests
import pandas as pd
import streamlit as st

def get_reservas():

    print("Iniciando get_reservas...")

    # Cabeçalhos de autenticação do CV
    headers = {
        "accept": "application/json",
        "email": "thiago.cunha@mip.com.br",
        "token": st.secrets["token"]
    }

    # URL da API de reservas -> situacao: todas - 500 registros - a partir de 01/01/2024
    url = "https://mip.cvcrm.com.br/api/cvio/reserva?situacao=todas&registros_por_pagina=500&a_partir_de=01%2F01%2F2024"

    # Requisição
    response = requests.get(url, headers=headers)
    dados = response.json() # pega em json

    print("Dados de leads coletados com sucesso.")

    # Converte o json em uma lista de objetos
    reservas = list(dados.values())

    # Converte para DataFrame
    df = pd.json_normalize(reservas, sep='_')
    
    df_exploded = df.explode("leads_associados", ignore_index=True)

    df_leads = pd.json_normalize(df_exploded["leads_associados"]).reset_index(drop=True)
    
    df_final = df_exploded.drop(columns=["leads_associados"]).reset_index(drop=True)

    df = pd.concat([df_final, df_leads], axis=1)

    df = df[[
        "idproposta_cv", "vendida", "data", "data_venda", "situacao_situacao", "idlead",
        "unidade_empreendimento","unidade_tipo", "titular_nome", "titular_nascimento","titular_sexo",
        "titular_como_ficou_sabendo", "corretor_corretor", "corretor_imobiliaria", "condicoes_valor_contrato"
    ]]

    # Valor das coluna correto
    df["data"] = pd.to_datetime(df["data"]).dt.date
    df["data_venda"] = pd.to_datetime(df["data_venda"]).dt.date

    return df