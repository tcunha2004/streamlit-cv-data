import streamlit as st
import pandas as pd
from .convert_str_obj import convert_str_to_obj

def get_leads():
    df = pd.read_csv("dev/csv/leads.csv")
    df = convert_str_to_obj(df)

    df.set_index("idlead", inplace=True)

    df = df[[
        "nome", "email", "gestor", "imobiliaria", "corretor", "situacao", "telefone", "data_cad",
        "midia_principal", "documento", "sexo", "estado", "cidade", "bairro", "origem", "ultima_data_conversao",
        "empreendimento", "midias"
    ]]

    # Valor das coluna correto
    df["gestor"] = df["gestor"].map(lambda x: x["nome"] if x["nome"] else None) # pega o "nome" caso haja algum
    df["imobiliaria"] = df["imobiliaria"].map(lambda x: x["nome"] if x["nome"] else None)
    df["corretor"] = df["corretor"].map(lambda x: x["nome"] if x["nome"] else None)
    df["situacao"] = df["situacao"].map(lambda x: x["nome"] if x["nome"] else None)
    df["telefone"] = df["telefone"].map(lambda x: str(x).replace(".0", "") if pd.notnull(x) else None)
    df["data_cad"] = pd.to_datetime(df["data_cad"], errors="coerce").dt.date
    df["ultima_data_conversao"] = pd.to_datetime(df["ultima_data_conversao"], errors="coerce").dt.date
    df["empreendimento"]= df["empreendimento"].map(lambda x: [item["nome"] for item in x] if isinstance(x, list) else None)

    return df