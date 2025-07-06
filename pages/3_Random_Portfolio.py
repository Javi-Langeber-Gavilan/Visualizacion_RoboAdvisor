import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide")

# Establecemos la columna con contenido centrado
col1, col2, col3 = st.columns([1, 2, 1])  # Esto da un "ancho" ajustable al contenido central (columna 2)

# Columna central (ajustamos su tamaño)
with col2:
    # Título centrado
    st.markdown("<h2 style='text-align: center;'>RESULTADOS - Random Portfolio</h2>", unsafe_allow_html=True)

    # Texto justificado
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
    <br>En este apartado se presentan los resultados del backtesting realizado para el Test de Aleatoriedad del estudio realizado.

    <br>Esta estrategia consiste en la simulación de "n" carteras aleatorias, cada una de ellas formada por un número aleatorio de 
    fondos de inversión elegido aleatoriamente. Estas carteras se mantienen durante periodos de 6 meses, tras los cuales, se vuelven a hacer
    de manera nuevamente aleatoria. El objetivo es analizar los posibles rendimiento sobtenidos por inversores aleatorios en el entorno
    y universo de inversión disponible para el RoboAdvisor.
                
    <br>El backtesting de esta estrategia ha consistido en la generación de 1.000.000 de carteras aleatorias y su análisis durante el periodo
    comprendido entre el año 2005 y la actualidad. Debido al gran número de carteras generadas, se presenta a continuación el Track Record de los
    deciles de todas ellas, y se muestra más adelante el análsis para los percentiles 10, 50 y 90  por separado.
                
    <br>Los resultados obtenidos son los siguientes:
    </div>
    """, unsafe_allow_html=True)


    # TRACK RECORD
    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/3_Random/tr.png", width=800)
    


    tab1, tab2, tab3 = st.tabs(["Percentil 10", "Percentil 50", "Percentil 90"])

    with tab1:

        st.markdown("""
        En las siguientes páginas se podrán encontrar los resultados obtenidos por el percentil
        10 de todas las carteras aleatorias de inversión analizadas:
        
        - **Track Record** de la cartera  
        """, unsafe_allow_html=True)

            # TRACK RECORD
        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/10_tr.png", width=800)

        # SHARPE
        st.markdown("""
        - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/10_roll.png", width=800)

        # DISTRIBUCION RENDIMIENTOS
        st.markdown("""
        - Diagrama de la **distribución de rendimientos** de la cartera.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/10_dist.png", width=800)

        # TIME UNDER WATER
        st.markdown("""
        - Diagrama del **Time Under Water** y **Drawdown**. 
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/10_dd.png", width=800)

        # CUADRO RATIOS FINANCIEROS
        st.markdown("""
        - Cuadro con el resumen de los **ratios financieros** para diferentes ventanas temporales.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.markdown("TABLA")
            # st.image("pictures/INTRO/intro_track_record.png", width=800)



    
    with tab2:

        st.markdown("""
        En las siguientes páginas se podrán encontrar los resultados obtenidos por el percentil
        50 de todas las carteras aleatorias de inversión analizadas:
        
        - **Track Record** de la cartera  
        """, unsafe_allow_html=True)

            # TRACK RECORD
        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/50_tr.png", width=800)

        # SHARPE
        st.markdown("""
        - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/50_roll.png", width=800)

        # DISTRIBUCION RENDIMIENTOS
        st.markdown("""
        - Diagrama de la **distribución de rendimientos** de la cartera.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/50_dist.png", width=800)

        # TIME UNDER WATER
        st.markdown("""
        - Diagrama del **Time Under Water** y **Drawdown**. 
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/50_dd.png", width=800)

        # CUADRO RATIOS FINANCIEROS
        st.markdown("""
        - Cuadro con el resumen de los **ratios financieros** para diferentes ventanas temporales.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.markdown("TABLA")
            # st.image("pictures/INTRO/intro_track_record.png", width=800)





    with tab3:

        st.markdown("""
        En las siguientes páginas se podrán encontrar los resultados obtenidos por el percentil
        90 de todas las carteras aleatorias de inversión analizadas:
        
        - **Track Record** de la cartera  
        """, unsafe_allow_html=True)

            # TRACK RECORD
        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/90_tr.png", width=800)

        # SHARPE
        st.markdown("""
        - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/90_roll.png", width=800)

        # DISTRIBUCION RENDIMIENTOS
        st.markdown("""
        - Diagrama de la **distribución de rendimientos** de la cartera.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/90_dist.png", width=800)

        # TIME UNDER WATER
        st.markdown("""
        - Diagrama del **Time Under Water** y **Drawdown**. 
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/3_Random/90_dd.png", width=800)

        # CUADRO RATIOS FINANCIEROS
        st.markdown("""
        - Cuadro con el resumen de los **ratios financieros** para diferentes ventanas temporales.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.markdown("TABLA")
            # st.image("pictures/INTRO/intro_track_record.png", width=800)


# Créditos
st.markdown("---")
st.caption("Autor: Javier Langeber Gavilán | Máster Universitario en Ingeniería Industrial | Universidad Politécnica de Madrid")