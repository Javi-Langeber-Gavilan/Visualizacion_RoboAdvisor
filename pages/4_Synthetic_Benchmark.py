import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(layout="wide")

# Establecemos la columna con contenido centrado
col1, col2, col3 = st.columns([1, 2, 1])  # Esto da un "ancho" ajustable al contenido central (columna 2)

# Columna central (ajustamos su tamaño)
with col2:
    # Título centrado
    st.markdown("<h2 style='text-align: center;'>RESULTADOS - Equally Weighted Portfolio</h2>", unsafe_allow_html=True)

    # Texto justificado
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
    <br>En este apartado se presentan los resultados del backtesting realizado para la estrategia del índice Equally Weighted realizada
    para este estudio.

    <br>Esta estrategia consiste en la generación en periodos rolados de 6 meses consistente en la utilización de todos los fondos disponibles
    en el universo de inversión con pesos iguales. De este modo, se crea un índice sintético para el análisis del comportamiento del universo
    de inversión en su totalidad, utilizando todos los fondos disponibles para cada periodo.
                
    <br>El backtesting de esta estrategia ha consistido en la creación de este índice sintético y su análisis en el periodo comprendido entre
    el año 2005 y la actualidad.
                
    <br>Los resultados obtenidos son los siguientes:
    </div>
    """, unsafe_allow_html=True)

        # TRACK RECORD
    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/2_Rolling/roll_tr.png", width=800)

    # SHARPE
    st.markdown("""
    - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/4_Benchmark/ew_roll.png", width=800)

    # DISTRIBUCION RENDIMIENTOS
    st.markdown("""
    - Diagrama de la **distribución de rendimientos** de la cartera.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/4_Benchmark/ew_dist.png", width=800)

    # TIME UNDER WATER
    st.markdown("""
    - Diagrama del **Time Under Water** y **Drawdown**. 
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/4_Benchmark/ew_dd.png", width=800)

    # CUADRO RATIOS FINANCIEROS
    st.markdown("""
    - Cuadro con el resumen de los **ratios financieros** para diferentes ventanas temporales.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
            df = pd.read_pickle('data/ew.pkl')
            st.dataframe(df)


# Créditos
st.markdown("---")
st.caption("Autor: Javier Langeber Gavilán | Máster Universitario en Ingeniería Industrial | Universidad Politécnica de Madrid")