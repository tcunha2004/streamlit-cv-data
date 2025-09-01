import streamlit as st
import pandas as pd
from .convert_str_obj import convert_str_to_obj

def get_reservas():
    df = pd.read_csv("dev/csv/reservas.csv")
    df = convert_str_to_obj(df)
    
    df_exploded = df.explode("leads_associados", ignore_index=True)

    df_leads = pd.json_normalize(df_exploded["leads_associados"]).reset_index(drop=True)
    
    df_final = df_exploded.drop(columns=["leads_associados"]).reset_index(drop=True)

    df = pd.concat([df_final, df_leads], axis=1)
    df.set_index("idproposta_cv", inplace=True)

    df = df[[
        "vendida", "data", "data_venda", "situacao_situacao", "idlead",
        "unidade_empreendimento","unidade_tipo", "titular_nome", "titular_nascimento","titular_sexo",
        "titular_como_ficou_sabendo", "corretor_corretor", "corretor_imobiliaria", "condicoes_valor_contrato"
    ]]

    # Valor das coluna correto
    df["data"] = pd.to_datetime(df["data"]).dt.date
    df["data_venda"] = pd.to_datetime(df["data_venda"]).dt.date

    return df