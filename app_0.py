"""
Aplicación en Streamlit para análisis de deforestación
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import geopandas as gpd
from sklearn.cluster import KMeans

def cargar_datos():
    """Carga los datos desde un archivo CSV."""
    return pd.read_csv("datos_deforestacion.csv")

def graficar_mapa(df, variable):
    """Genera un mapa interactivo de la variable seleccionada."""
    return px.scatter_mapbox(
        df,
        lat="Latitud",
        lon="Longitud",
        color=variable,
        size="Superficie_Deforestada",
        mapbox_style="open-street-map"
    )

def graficar_torta(df):
    """Genera un gráfico de torta por tipo de vegetación."""
    return px.pie(df, names="Tipo_Vegetacion", values="Superficie_Deforestada")

def clusterear(df):
    """Aplica KMeans para agrupar superficies deforestadas."""
    modelo = KMeans(n_clusters=3, random_state=42, n_init=10).fit(df[["Latitud", "Longitud"]])
    df["Cluster"] = modelo.labels_
    return px.scatter_mapbox(
        df,
        lat="Latitud",
        lon="Longitud",
        color="Cluster",
        mapbox_style="carto-positron"
    )

def filtrar_datos(df, variables, rangos):
    """Filtra los datos según variables y rangos seleccionados por el usuario."""
    condiciones = [df[var].between(r[0], r[1]) for var, r in zip(variables, rangos)]
    return df[np.logical_and.reduce(condiciones)]

def main():
    """Función principal para ejecutar la app en Streamlit."""
    st.title("Análisis de Deforestación")
    datos = cargar_datos()
    
    st.subheader("Mapa de deforestación")
    variable_mapa = st.selectbox("Selecciona una variable para el mapa:", datos.columns[3:])
    st.plotly_chart(graficar_mapa(datos, variable_mapa))
    
    st.subheader("Gráfico de torta por tipo de vegetación")
    st.plotly_chart(graficar_torta(datos))
    
    st.subheader("Análisis de Clúster")
    st.plotly_chart(clusterear(datos))
    
    st.subheader("Mapa personalizado")
    seleccion_variables = st.multiselect("Selecciona hasta 4 variables:", datos.columns[1:])
    rangos = [st.slider(f"Rango para {v}", float(datos[v].min()), float(datos[v].max()), (float(datos[v].min()), float(datos[v].max()))) for v in seleccion_variables]
    datos_filtrados = filtrar_datos(datos, seleccion_variables, rangos)
    st.plotly_chart(graficar_mapa(datos_filtrados, seleccion_variables[0] if seleccion_variables else "Superficie_Deforestada"))

if __name__ == "__main__":
    main()
