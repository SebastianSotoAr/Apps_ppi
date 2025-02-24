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


def filtra_calificacion(producto, calificacion):
    """
    Filtra un DataFrame basado en la calificación de un producto específico.

    Args:
        producto(str): Nombre de la columna que representa el producto.
        calificacion(str): Calificación a filtrar.

    Returns:
        pd.DataFrame: Subconjunto del DataFrame con las filas que coinciden.

    Raises:
        KeyError: Si la columna especificada no existe en el DataFrame.
        ValueError: Si la calificación no está presente en la columna.
    """

    return datos[datos[producto] == calificacion]


# Guardar el dataset en la variable 'datos'
datos = carga_datos_csv(ruta)

# Título de la app
st.title('Datos de satisfacción')

# Info
st.markdown('Desarrollado por SebastianSotoAr')

# Descripción
st.write('Resumen de los datos')
st.dataframe(datos.head())

# Promedios
st.write('Promedios de las calificaciones')
promedios = datos[[
    'Calificación_Producto',
    'Calificación_Servicio',
    'Calificación_Entrega'
]].mean()
st.dataframe(promedios)
st.write("Los índices con mejor satisfacción son:", promedios.idxmax())
st.write("Los índices con peor satisfacción son:", promedios.idxmin())

# Calificaciones
st.title("Filtrado de calificaciones")
productos = ['Servicio', 'Entrega']
calificaciones = ['Regular', 'Excelente', 'Malo', 'Bueno']
producto = st.selectbox('Seleccione el producto: ', productos)
calificacion = st.selectbox('Seleccione la Calificación', calificaciones)

# Reporte
boton = st.button('Filtrar')
if boton:
    datos_filtrados = filtra_calificacion(producto, calificacion)
    st.dataframe(datos_filtrados)

    datos_final = datos_filtrados.describe()
    st.dataframe(datos_final)

    # Convertir el DataFrame a CSV
    csv = datos_final.to_csv(index=False).encode('utf-8')

    # Crear un botón de descarga
    st.download_button(
        label="📥 Descargar CSV",
        data=csv,
        file_name='datos.csv',
        mime='text/csv'
    )


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Cargar el dataset
url = "https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/refs/heads/main/archivos-datos/matplotlib/3d_plot_data.csv"
df = pd.read_csv(url)

# Mostrar el DataFrame
st.write("### Dataset - Superficie 3D", df.head())

# Convertir las columnas en arrays
X = df['X_Surface'].values
Y = df['Y_Surface'].values
Z = df['Z_Surface'].values

# Crear una cuadrícula (necesario para plot_surface)
# Asumimos que los datos están en formato plano y necesitamos una malla
num_points = int(np.sqrt(len(X)))  # Supone que X, Y, Z forman una cuadrícula cuadrada
X_grid = X.reshape((num_points, num_points))
Y_grid = Y.reshape((num_points, num_points))
Z_grid = Z.reshape((num_points, num_points))

# Crear la figura y el gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Gráfico de superficie
surf = ax.plot_surface(X_grid, Y_grid, Z_grid, cmap='viridis', edgecolor='k')

# Añadir barra de color
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Configuración de los ejes
ax.set_title('Gráfico de Superficie 3D - Matplotlib')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
