import streamlit as st
import time

# Configuracion de la pagina:

st.set_page_config(page_title="Demo de Streamlit", page_icon=":)", layout="wide")

# Escritura:

st.title("Demo completa de componenetes de streamlit")
st.header("Elementos básicos:")

# Elemenetos de texto: 

st.subheader("Texto Enriquecido")
st.text("Texto simple")
st.markdown("**Negrita** y *Cursiva*")
st.code("print('Hola mundo')", language="python")

# Widgets:

st.subheader("Widgets interactivos")
if st.button("Haz click aqui"):
    st.success("Boton presionado")

opcion = st.selectbox("selecciona una opcion", ["A,B,C"])
st.write(f"Valor seleccionado : {opcion}")
ingredientes = st.multiselect("Selecciona los ingredientes",["Avena","Huevos","Pollo","Frutas","Verdura"])
st.write(ingredientes)

# Slider:

st.subheader("Slider")
valor = st.slider("Selecciona un valor:", 0,100,25)
st.write(f"Has seleccionado {valor}")

# INPUT:

st.subheader("Inputs")
nombre = st.text_input("Como te llamas?")
edad = st.number_input("Cuantos años tienes?")
st.write(f"{nombre} tiene {edad} años.")

# Elementos multimedia:

st.subheader("Elementos multimedia")
st.image("url", caption="Imagen de la web")
st.audio("url")
st.video("url")

# Estados:

st.subheader("Estados:")
if "contador" not in st.session_state:
    st.session_state.contador = 0

incrementar = st.button("Incrementar contador")

if incrementar:
    st.session_state.contador +=1

st.write(f"Contador = {st.session_state.contador}")


# Barra de progreso:

st.subheader("Barra de progreso:")
progreso = st.progress(0)
for porcentaje in range(0,101,50):
    time.sleep(1)
    progreso.progress(porcentaje)

# Disños y contenedores:

st.subheader("Diseños y contenedores")
col1, col2 = st.columns(2)

with col1:
    st.info("Esta es la columna 1")
with col2:
    st.warning("Esta es la columna 2")

with st.expander("Haz click para espandir: "):
    st.write("Aqui puedes ocultar o mostrar el contenedor")

col3, col4 = st.columns(2)
with col3:
    st.info("dale")
with col4:
    st.warning("dale mas")

# Menu

