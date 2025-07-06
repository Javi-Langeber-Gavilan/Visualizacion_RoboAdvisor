import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide")

# Establecemos la columna con contenido centrado
col1, col2, col3 = st.columns([1, 2, 1])  # Esto da un "ancho" ajustable al contenido central (columna 2)

# Columna central (ajustamos su tamaño)
with col2:
    # Título centrado
    st.markdown("<h2 style='text-align: center;'>Créditos</h2>", unsafe_allow_html=True)

    # Texto justificado
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
    <br>Esta web, su contenido, estructura, desarrollo técnico y los resultados presentados 
    han sido realizados en su totalidad por Javier Langeber Gavilán, en el marco del Trabajo Fin de Máster (TFM) del Máster 
    Universitario en Ingeniería Industrial de la Universidad Politécnica de Madrid<br><br><br>""", unsafe_allow_html=True)
                

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.image("pictures/6_Credits/JAVI.jpg", width=300)

    st.markdown("""           
    <br><br>El proyecto ha sido desarrollado de forma individual con fines académicos, siguiendo los estándares metodológicos 
    y éticos exigidos por el programa, y tiene como objetivo principal el desarrollo y análsis de los resultados obtenidos por
    un RoboAdvisor cuyo motor de cálculo está compuesto por un algoritmo genético.
    </div>
    """, unsafe_allow_html=True)