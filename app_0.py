import pandas as pd
import streamlit as st

# Guardar en la variable 'ruta' la url del dataset
ruta = "https://raw.githubusercontent.com/gabrielawad/\
programacion-para-ingenieria/refs/heads/main/archivos-datos/pandas/\
encuestas_satisfaccion.csv"

# Cargar el dataset a partir de la ruta establecida
def carga_datos_csv(url):
    """
    Carga un archivo CSV desde una URL y lo devuelve como un DataFrame de
    Pandas.

    Args:
        url(str): URL del archivo CSV.

    Returns:
        pd.DataFrame: DataFrame cargado desde la URL.
    """
    data = pd.read_csv(url)

    return data


# Guardar el dataset en la variable 'datos'
datos = carga_datos_csv(ruta)

# Título de la app
st.title('Datos de satisfacción')

# Info
st.markdown('Desarrollado por SebastianSotoAr')

# Descripción
st.write('Resumen de los datos')
st.dataframe(datos)
