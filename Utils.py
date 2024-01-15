import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def resumen_columnas(dataframe):
    """
    Genera un resumen de las columnas de un DataFrame, incluyendo la cantidad de datos,
    el porcentaje de nulos, la cantidad de nulos, la cantidad de valores distintos,
    y el tipo de datos para cada columna.

    Parameters:
        dataframe (pd.DataFrame): El DataFrame del cual se desea obtener el resumen.

    Returns:
        pd.DataFrame: Un DataFrame que contiene el resumen de las columnas.
    """

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
    """
    Retorna un diccionario que contiene los tipos de variables presentes en cada columna del DataFrame.

    Parameters:
        dataframe (pd.DataFrame): El DataFrame del cual se desea obtener los tipos de variables.

    Returns:
        dict: Un diccionario donde las claves son los nombres de las columnas y los valores son listas
              de los tipos de variables presentes en cada columna.
    """
    resultados = {}  
    
    for columna in dataframe.columns:
        # Obtener tipos de variables únicos en la columna
        tipos = dataframe[columna].apply(type).unique()  
        resultados[columna] = tipos.tolist()  
    
    return resultados


def convertir_a_time(x):
    """
    Convierte un valor en formato de cadena (str) o datetime a un objeto de tiempo (time).

    Parameters:
        x (str, datetime, u otro): El valor a convertir.

    Returns:
        time or None: Si la conversión es exitosa, retorna el objeto de tiempo resultante.
                     Si no es posible realizar la conversión, retorna None.
    """
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    
    return x

def imputa_valor_mas_frecuente(df, columna):
    """
    Imputa el valor más frecuente en las filas donde el valor de una columna específica es 'SD'.

    Parameters:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en la que se realizará la imputación.

    Returns:
        None: La función modifica el DataFrame inplace.
    """
    valor_mas_frecuente = df[columna].mode()[0]

    print("Muestra antes de la imputación:")
    print(df[df[columna] == 'SD'].head())

    # Imputar el valor más frecuente en las filas donde el valor de la columna es 'SD'
    df.loc[df[columna] == 'SD', columna] = valor_mas_frecuente

    print("\nMuestra después de la imputación:")
    print(df[df[columna] == valor_mas_frecuente].head())


def imputar_edad_promedio_por_sexo(df):
    """
    Imputa la edad promedio correspondiente al género en el DataFrame, reemplazando los valores 'SD' con el promedio respectivo.

    Parameters:
        df (pd.DataFrame): El DataFrame que contiene los datos.

    Returns:
        None: La función modifica el DataFrame inplace.
    """
    # Reemplazar "SD" con NaN en la columna 'Edad'
    df['Edad'] = df['Edad'].replace('SD', pd.NA)

    # Calcular el promedio de edad para cada grupo de género
    promedio_por_genero = df.groupby('Sexo')['Edad'].mean()

    # Imprimir la edad promedio por género
    print(f'La edad promedio de Femenino es {round(promedio_por_genero["FEMENINO"])} y de Masculino es {round(promedio_por_genero["MASCULINO"])}')

    # Llenar los valores NaN en la columna 'Edad' utilizando el promedio correspondiente al género
    df['Edad'] = df.apply(lambda row: promedio_por_genero[row['Sexo']] if pd.isna(row['Edad']) else row['Edad'], axis=1)

    # Convertir la columna 'Edad' a entero
    df['Edad'] = df['Edad'].astype(int)


def top_10_valores_repetidos(df, columna):
    """
    Muestra los diez valores más repetidos en una columna específica del DataFrame.

    Parameters:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en la que se desea encontrar los valores más repetidos.

    Returns:
        None: La función imprime el resultado en la consola.
    """
    # Calcular la frecuencia de cada valor en la columna
    frecuencias = df[columna].value_counts()

    # Seleccionar los top 10 valores más repetidos
    top_10 = frecuencias.head(10)

    print(f"Top 10 de valores más repetidos en la columna '{columna}':")
    print(top_10)


def grafico_distribucion_mensual_por_ano(df):
    """
    Crea un gráfico de distribución mensual de la cantidad de víctimas a lo largo de los años.

    Parameters:
        df (pd.DataFrame): El DataFrame que contiene los datos.

    Returns:
        None: La función muestra el gráfico en la pantalla.
    """
    # Se obtiene una lista de años únicos
    años = df['Año'].unique()

    # Se define el número de filas y columnas para la cuadrícula de subgráficos
    n_filas = 3
    n_columnas = 2

    # Se crea una figura con subgráficos en una cuadrícula de 2x3
    fig, axes = plt.subplots(n_filas, n_columnas, figsize=(14, 8))

    # Se itera a través de los años y crea un gráfico por año
    for i, year in enumerate(años):
        fila = i // n_columnas
        columna = i % n_columnas
        
        # Se filtran los datos para el año actual y agrupa por mes
        data_mensual = (df[df['Año'] == year]
                        .groupby('Mes')
                        .agg({'Cantidad víctimas':'sum'}))
        
        # Se configura el subgráfico actual
        ax = axes[fila, columna]
        data_mensual.plot(ax=ax, kind='line')
        ax.set_title('Año ' + str(year))
        ax.set_xlabel('Mes')
        ax.set_ylabel('Cantidad de Víctimas')
        ax.legend_ = None
        
    plt.tight_layout()
    plt.show()

def cantidad_total_accidentes_por_mes(df):
    """
    Crea un gráfico de barras que muestra la cantidad total de accidentes por mes, sin distinción de año.

    Parameters:
        df (pd.DataFrame): El DataFrame que contiene los datos.

    Returns:
        None: La función muestra el gráfico en la pantalla.
    """
    df['Mes'] = df['Mes']

    plt.figure(figsize=(12, 6))
    sns.countplot(x='Mes', data=df, palette='viridis')
    plt.title('Cantidad Total de Accidentes por Mes (sin distinción de año)')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Accidentes')
    plt.xticks(rotation=45, ha='right')
    plt.show()



def accidentes_por_dia_semana(df):
    """
    Analiza y visualiza la cantidad de accidentes por día de la semana, junto con datos resumen.

    Parameters:
        df (pd.DataFrame): El DataFrame que contiene los datos.

    Returns:
        None: La función muestra el gráfico en la pantalla y imprime datos resumen.
    """
    # Se convierte la columna 'Fecha' a tipo de dato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Día semana'] = df['Fecha'].dt.dayofweek

    # Se mapea el número del día de la semana a su nombre
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    df['Nombre día'] = df['Día semana'].map(lambda x: dias_semana[x])

    # Se cuenta la cantidad de accidentes por día de la semana
    data = df.groupby('Nombre día').agg({'Cantidad víctimas': 'sum'}).reset_index()

    plt.figure(figsize=(6, 3))
    ax = sns.barplot(x='Nombre día', y='Cantidad víctimas', data=data, order=dias_semana, palette='viridis')

    ax.set_title('Cantidad de Accidentes por Día de la Semana')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Cantidad de Accidentes')
    plt.xticks(rotation=45)

    print(f'El día de la semana con menor cantidad de víctimas tiene {data.min()[1]} víctimas')
    print(f'El día de la semana con mayor cantidad de víctimas tiene {data.max()[1]} víctimas')
    print(f'La diferencia porcentual es de {round((data.max()[1] - data.min()[1]) / data.min()[1] * 100, 2)}%')

    plt.show()

def crea_categoria_momento_dia(hora):
  """
  Devuelve la categoría de tiempo correspondiente a la hora proporcionada.

  Parameters:
    hora: La hora a clasificar.

  Returns:
    La categoría de tiempo correspondiente.
  """
  if hora.hour >= 6 and hora.hour <= 10:
    return "Mañana"
  elif hora.hour >= 11 and hora.hour <= 13:
    return "Medio día"
  elif hora.hour >= 14 and hora.hour <= 18:
    return "Tarde"
  elif hora.hour >= 19 and hora.hour <= 23:
    return "Noche"
  else:
    return "Madrugada"
  

def cantidad_accidentes_por_categoria_tiempo(df):
    '''
    Calcula la cantidad de accidentes por categoría de tiempo y muestra un gráfico de barras.

    Esta función toma un DataFrame que contiene una columna 'Hora' y utiliza la función
    'crea_categoria_momento_dia' para crear la columna 'Categoria tiempo'. Luego, cuenta
    la cantidad de accidentes por cada categoría de tiempo, calcula los porcentajes y
    genera un gráfico de barras que muestra la distribución de accidentes por categoría de tiempo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la información de los accidentes.

    Returns:
        None
    '''
    # Convertir la columna 'Hora' a formato datetime
    df['Hora'] = pd.to_datetime(df['Hora'], errors='coerce')

    # Se filtran las filas con valores nulos en la columna 'Hora'
    df = df.dropna(subset=['Hora'])

    # Se aplica la función crea_categoria_momento_dia para crear la columna 'Categoria tiempo'
    df['Categoria tiempo'] = df['Hora'].apply(crea_categoria_momento_dia)

    # Se cuenta la cantidad de accidentes por categoría de tiempo
    data = df['Categoria tiempo'].value_counts().reset_index()
    data.columns = ['Categoria tiempo', 'Cantidad accidentes']

    # Se calculan los porcentajes
    total_accidentes = data['Cantidad accidentes'].sum()
    data['Porcentaje'] = (data['Cantidad accidentes'] / total_accidentes) * 100
    
    colores = sns.color_palette("pastel", n_colors=len(data))
    plt.figure(figsize=(8, 4))
    ax = sns.barplot(x='Categoria tiempo', y='Cantidad accidentes', data=data, palette=colores)

    ax.set_title('Cantidad de Accidentes por Categoría de Tiempo')
    ax.set_xlabel('Categoría de Tiempo')
    ax.set_ylabel('Cantidad de Accidentes')

    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad accidentes"]}', (index, row["Cantidad accidentes"]), ha='center', va='bottom')

    plt.show()


def cantidad_accidentes_por_horas_del_dia(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por hora del día.

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico de barras.
    '''
    # Se extrae la hora del día de la columna 'hora'
    df['Hora del día'] = df['Hora'].apply(lambda x: x.hour)

    # Se cuenta la cantidad de accidentes por hora del día
    data = df['Hora del día'].value_counts().reset_index()
    data.columns = ['Hora del día', 'Cantidad de accidentes']

    # Se ordena los datos por hora del día
    data = data.sort_values(by='Hora del día')

    # Se crea el gráfico de barras con una paleta de colores
    colores = sns.color_palette("husl", n_colors=len(data))
    plt.figure(figsize=(12, 4))
    ax = sns.barplot(x='Hora del día', y='Cantidad de accidentes', data=data, palette=colores)

    ax.set_title('Cantidad de Accidentes por Hora del Día')
    ax.set_xlabel('Hora del día')
    ax.set_ylabel('Cantidad de accidentes')

    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (row["Hora del día"], row["Cantidad de accidentes"]), ha='center', va='bottom')

    plt.show()


def cantidad_accidentes_semana_fin_de_semana(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por tipo de día (semana o fin de semana).

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico de barras.
    '''
    # Se convierte la columna 'fecha' a tipo de dato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Dia semana'] = df['Fecha'].dt.dayofweek
    
    # Se crea una columna 'tipo_dia' para diferenciar entre semana y fin de semana
    df['Tipo de día'] = df['Dia semana'].apply(lambda x: 'Fin de Semana' if x >= 5 else 'Semana')
    
    # Se cuenta la cantidad de accidentes por tipo de día
    data = df['Tipo de día'].value_counts().reset_index()
    data.columns = ['Tipo de día', 'Cantidad de accidentes']
    
    # Se crea el gráfico de barras con una paleta de colores
    colores = sns.color_palette("Set2", n_colors=len(data))
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='Tipo de día', y='Cantidad de accidentes', data=data, palette=colores)
    
    ax.set_title('Cantidad de accidentes por tipo de día')
    ax.set_xlabel('Tipo de día')
    ax.set_ylabel('Cantidad de accidentes')
    
    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (index, row["Cantidad de accidentes"]), ha='center', va='bottom')
    
    plt.show()


def distribucion_edad(df):
    '''
    Genera un gráfico con un histograma y un boxplot que muestran la distribución de la edad de los involucrados en los accidentes.

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico con un histograma y un boxplot.
    '''
    # Se crea una figura con un solo eje x compartido
    fig, ax = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
    
    # Se grafica el histograma de la edad
    sns.histplot(df['Edad'], kde=True, ax=ax[0])
    ax[0].set_title('Histograma de Edad') ; ax[0].set_ylabel('Frecuencia')
    
    # Se grafica el boxplot de la edad
    sns.boxplot(x=df['Edad'], ax=ax[1])
    ax[1].set_title('Boxplot de Edad') ; ax[1].set_xlabel('Edad')
    
    plt.tight_layout()
    plt.show()



def distribucion_edad_por_anio(df):
    '''
    Genera un gráfico de boxplot que muestra la distribución de la edad de las víctimas de accidentes por año.

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico de boxplot.
    '''
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Año', y='Edad', data=df, palette='viridis') 
    
    plt.title('Boxplot de Edades de Víctimas por Año')
    plt.xlabel('Año')
    plt.ylabel('Edad de las Víctimas')
    
    plt.show()


def cantidades_accidentes_por_anio_y_sexo(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por año y sexo.

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico de barras.
    '''
    plt.figure(figsize=(12, 4))
    sns.barplot(x='Año', y='Edad', hue='Sexo', data=df,)
    
    plt.title('Cantidad de Accidentes por Año y Sexo')
    plt.xlabel('Año') ; plt.ylabel('Edad de las víctimas') ; plt.legend(title='Sexo')

    plt.show()

def edad_y_rol_victimas(df):
    '''
    Genera un gráfico de la distribución de la edad de las víctimas por rol.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    plt.figure(figsize=(10, 6))
    sns.boxplot(y='Rol', x='Edad', data=df, palette='viridis') 
    
    plt.title('Edades por Condición')
    plt.xlabel('Edad de las Víctimas')
    plt.ylabel('Rol')

    plt.show()


def distribucion_edad_por_victima(df):
    '''
    Genera un gráfico de la distribución de la edad de las víctimas por tipo de vehículo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    plt.figure(figsize=(14, 6))
    sns.boxplot(x='Víctima', y='Edad', data=df, palette='viridis')  
    
    plt.title('Boxplot de Edades de Víctimas por tipo de vehículo que usaba')
    plt.xlabel('Tipo de vehiculo')
    plt.ylabel('Edad de las Víctimas')
    
    plt.show()


def cantidad_victimas_sexo_rol_victima(df):
    '''
    Genera un resumen de la cantidad de víctimas por sexo, rol y tipo de vehículo en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Gráficos de barras que muestran la cantidad de víctimas por sexo, rol y tipo de vehículo en orden descendente.
    * DataFrames que muestran la cantidad y el porcentaje de víctimas por sexo, rol y tipo de vehículo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    colores_por_defecto = sns.color_palette()
    colores_invertidos = [colores_por_defecto[1], colores_por_defecto[0]]

    # Se crea el gráfico
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Gráfico 1: Sexo
    sns.countplot(data=df, x='Sexo', ax=axes[0], palette=colores_invertidos)
    axes[0].set_title('Cantidad de víctimas por sexo') ; axes[0].set_ylabel('Cantidad de víctimas')

    # Gráfico 2: Rol
    df_rol = df.groupby(['Rol', 'Sexo']).size().unstack(fill_value=0)
    df_rol.plot(kind='bar', stacked=True, ax=axes[1], color=colores_invertidos)
    axes[1].set_title('Cantidad de víctimas por rol') ; axes[1].set_ylabel('Cantidad de víctimas') ; axes[1].tick_params(axis='x', rotation=45)
    axes[1].legend().set_visible(False)

    # Gráfico 3: Tipo de vehículo
    df_victima = df.groupby(['Víctima', 'Sexo']).size().unstack(fill_value=0)
    df_victima.plot(kind='bar', stacked=True, ax=axes[2], color=colores_invertidos)
    axes[2].set_title('Cantidad de víctimas por tipo de vehículo') ; axes[2].set_ylabel('Cantidad de víctimas') ; axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend().set_visible(False)

    plt.show()



def cantidad_victimas_participantes(df):
    '''
    Genera un resumen de la cantidad de víctimas por número de participantes en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por número de participantes en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas por número de participantes.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se ordenan los datos por 'Participantes' en orden descendente por cantidad
    ordenado = df['Participantes'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'Cantidad': 'participantes'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 4))
    n
    colores = sns.color_palette("viridis", len(ordenado))

    # Se crea el gráfico de barras con colores
    ax = sns.barplot(data=ordenado, x='Participantes', y='count', order=ordenado['Participantes'], palette=colores)
    ax.set_title('Cantidad de víctimas por participantes')
    ax.set_ylabel('Cantidad de víctimas')
    # Rotar las etiquetas del eje x a 45 grados
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()


def cantidad_acusados(df):
    '''
    Genera un resumen de la cantidad de acusados en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de acusados en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de acusados.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se ordenan los datos por 'Acusado' en orden descendente por cantidad
    ordenado = df['Acusado'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'Cantidad': 'Acusado'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 4))
    
    colores = sns.color_palette("viridis", len(ordenado))

    ax = sns.barplot(data=ordenado, x='Acusado', y='count', order=ordenado['Acusado'], palette=colores)
    ax.set_title('Cantidad de acusados en los hechos') ; ax.set_ylabel('Cantidad de acusados') 
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()

def accidentes_tipo_de_calle(df):
    '''
    Genera un resumen de los accidentes de tráfico por tipo de calle y cruce.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por tipo de calle.
    * Un gráfico de barras que muestra la cantidad de víctimas en cruces.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas por tipo de calle.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas en cruces.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    paleta_colores = sns.color_palette("viridis")

    # Se crea el gráfico
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    sns.countplot(data=df, x='Tipo de calle', ax=axes[0], palette=paleta_colores)
    axes[0].set_title('Cantidad de víctimas por tipo de calle') ; axes[0].set_ylabel('Cantidad de víctimas')

    sns.countplot(data=df, x='Cruce', ax=axes[1], palette=paleta_colores)
    axes[1].set_title('Cantidad de víctimas en cruces') ; axes[1].set_ylabel('Cantidad de víctimas')

    plt.show()






