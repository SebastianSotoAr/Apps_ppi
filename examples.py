import streamlit as st

# Título de la app
st.title('Este es el Titulo')

# Info
st.markdown('Esto es información importante de la App')

# Descripción
st.write('Este es texto')

# Opciones de categoría
categorias = [
    'Categoría 1',
    'Categoría 2',
    'Categoría 3'
]

# Selección de categoría
categoria = st.selectbox("Elige una categoría:", categorias)
