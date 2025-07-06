import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(layout="wide")

# Establecemos la columna con contenido centrado
col1, col2, col3 = st.columns([1, 2, 1])  # Esto da un "ancho" ajustable al contenido central (columna 2)

# Columna central (ajustamos su tamaño)
with col2:
    # Título centrado
    st.markdown("<h2 style='text-align: center;'>RESULTADOS - Best Rolling Funds Portfolio</h2>", unsafe_allow_html=True)

    # Texto justificado
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
    <br>En este apartado se presentan los resultados del backtesting realizado para la estrategia de los mejores fondos rolados.
                
    <br>Esta estrategia, enfocada en el momentum del mercado, consiste en la indexación de la cartera a los "n" mejores fondos
    en cuanto a rentabilidad absoluta, de un periodo analizado anterior. En este caso, se analizan los periodos en ventanas roladas
    de 6 messes y se crea la cartera con los 10 mejores fondos del periodo anterior. 
                
    <br>El backtesting de esta estrategia ha consistido en la simulación de esta cartera durante el periodo comprendido entre 2005 y la actualidad.
                
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
        st.image("pictures/2_Rolling/roll_roll.png", width=800)

    # DISTRIBUCION RENDIMIENTOS
    st.markdown("""
    - Diagrama de la **distribución de rendimientos** de la cartera.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/2_Rolling/roll_dist.png", width=800)

    # TIME UNDER WATER
    st.markdown("""
    - Diagrama del **Time Under Water** y **Drawdown**. 
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/2_Rolling/roll_dd.png", width=800)

    # CUADRO RATIOS FINANCIEROS
    st.markdown("""
    - Cuadro con el resumen de los **ratios financieros** para diferentes ventanas temporales.
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
            df1 = pd.read_pickle('data/best_funds.pkl')
            st.dataframe(df1)


# Créditos
st.markdown("---")
st.caption("Autor: Javier Langeber Gavilán | Máster Universitario en Ingeniería Industrial | Universidad Politécnica de Madrid")