import ast
import pandas as pd

def convert_str_to_obj(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte automaticamente colunas que tenham strings representando
    listas/dicionários em objetos Python reais.
    """
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith(("[", "{")) else x
        )
    return df