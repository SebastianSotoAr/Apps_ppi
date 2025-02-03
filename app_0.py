"""
Aplicación en Streamlit para análisis de deforestación
"""

import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

def cargar_datos():
    """Carga los datos desde un archivo CSV."""
    return pd.read_csv("https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/refs/heads/main/archivos-datos/aplicaciones/deforestacion.csv")

def graficar_mapa(df, variable):
    """Genera un mapa interactivo de la variable seleccionada."""
    fig, ax = plt.subplots()
    scatter = ax.scatter(df["Longitud"], df["Latitud"], c=df[variable], s=df["Superficie_Deforestada"], cmap="viridis", alpha=0.6)
    plt.colorbar(scatter, label=variable)
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.set_title("Mapa de Deforestación")
    st.pyplot(fig)

def graficar_torta(df):
    """Genera un gráfico de torta por tipo de vegetación."""
    fig, ax = plt.subplots()
    df.groupby("Tipo_Vegetacion")["Superficie_Deforestada"].sum().plot.pie(ax=ax, autopct='%1.1f%%', startangle=90, cmap="viridis")
    ax.set_ylabel("")
    ax.set_title("Distribución de Superficie Deforestada por Tipo de Vegetación")
    st.pyplot(fig)

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
    graficar_mapa(datos, variable_mapa)
    
    st.subheader("Gráfico de torta por tipo de vegetación")
    graficar_torta(datos)
    
    st.subheader("Mapa personalizado")
    seleccion_variables = st.multiselect("Selecciona hasta 4 variables:", datos.columns[1:])
    rangos = [st.slider(f"Rango para {v}", float(datos[v].min()), float(datos[v].max()), (float(datos[v].min()), float(datos[v].max()))) for v in seleccion_variables]
    datos_filtrados = filtrar_datos(datos, seleccion_variables, rangos)
    graficar_mapa(datos_filtrados, seleccion_variables[0] if seleccion_variables else "Superficie_Deforestada")

if __name__ == "__main__":
    main()
