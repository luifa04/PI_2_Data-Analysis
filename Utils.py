import pandas as pd
from datetime import datetime, time

def resumen_columnas(dataframe):
    # Obtener la cantidad de datos, el porcentaje de nulos, la cantidad de nulos, la cantidad de valores distintos y el tipo de datos para cada columna
    resumen = pd.DataFrame({
        'Columna': dataframe.columns,
        'Cantidad de Datos': dataframe.count(),
        'Cantidad de Nulos': dataframe.isnull().sum(),
        'Porcentaje de Nulos': dataframe.isnull().mean() * 100,
        'Cantidad de Valores Distintos': dataframe.nunique(),
        'Tipo de Datos': dataframe.dtypes
    }).reset_index(drop=True)

    return resumen


def tipos_de_variables(dataframe):
    resultados = {}
    
    for columna in dataframe.columns:
        tipos = dataframe[columna].apply(type).unique()
        resultados[columna] = tipos.tolist()
    
    return resultados


def convertir_a_time(x):
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    return x