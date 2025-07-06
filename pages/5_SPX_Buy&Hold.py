import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(layout="wide")

# Establecemos la columna con contenido centrado
col1, col2, col3 = st.columns([1, 2, 1])  # Esto da un "ancho" ajustable al contenido central (columna 2)

# Columna central (ajustamos su tamaño)
with col2:
    # Título centrado
    st.markdown("<h2 style='text-align: center;'>RESULTADOS - S&P 500 Index Buy & Hold Portfolio</h2>", unsafe_allow_html=True)

    # Texto justificado
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
    <br>En este apartado se presentan los resultados del backtesting realizado para la estrategia consitente en la compra y 
    mantenimeinto de un fondo de inversión indexado al índice bursátil americano S&P 500.

    <br>Esta estrategia consiste en la compra y mantenimiento de una cartera con un único fondo de inversión indexado al índice
    bursátil S&P 500 (también denominado SPX), que contiene las 500 acciones de mayor capitalización bursátil del mercado de valores
    de los Estados Unidos de América.
                
    <br>El backtesting de esta estrategia ha consistido en la creación y mantenimiento de esta cartera, durante el periodo que transucrre
    desde el año 2005 hasta la actualidad.
                
    <br>Los resultados obtenidos son los siguientes:
    </div>
    """, unsafe_allow_html=True)

        # TRACK RECORD
    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/5_BnH/spx_tr.png", width=800)

    # SHARPE
    st.markdown("""
    - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/5_BnH/spx_roll.png", width=800)

    # DISTRIBUCION RENDIMIENTOS
    st.markdown("""
    - Diagrama de la **distribución de rendimientos** de la cartera.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/5_BnH/spx_dist.png", width=800)

    # TIME UNDER WATER
    st.markdown("""
    - Diagrama del **Time Under Water** y **Drawdown**. 
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/5_BnH/spx_dd.png", width=800)

    # CUADRO RATIOS FINANCIEROS
    st.markdown("""
    - Cuadro con el resumen de los **ratios financieros** para diferentes ventanas temporales.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
            df = pd.read_pickle('data/spx.pkl')
            st.dataframe(df)


# Créditos
st.markdown("---")
st.caption("Autor: Javier Langeber Gavilán | Máster Universitario en Ingeniería Industrial | Universidad Politécnica de Madrid")