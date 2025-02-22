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

# Resive números
valor = st.number_input("Introduce el valor:", format="%.2f")
if valor:
    st.write(f'Guardo: {valor}')

# Resive texto
texto = st.text_input('Introduce el texto')

# Botón
boton = st.button("Botón")

# Evento
if boton:
    st.write('Escucho el evento')

# Sidebar
menu1 = ['Item 1.1.', 'Item 1.2.', 'Item 1.3.']
opcion1 = st.sidebar.selectbox('Menú 1:', menu1)
menu2 = ['Item 2.1.', 'Item 2.2.', 'Item 2.3.']
opcion2 = st.sidebar.selectbox('Menú 2:', menu2)
menu3 = ['Item 3.1.', 'Item 3.2.', 'Item 3.3.']
opcion3 = st.sidebar.selectbox('Menú 3:', menu3)
