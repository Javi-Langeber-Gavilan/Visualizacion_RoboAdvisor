import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide")

# Establecemos la columna con contenido centrado
col1, col2, col3 = st.columns([1, 2, 1])  # Esto da un "ancho" ajustable al contenido central (columna 2)

# Columna central (ajustamos su tamaño)
with col2:
    # Título centrado
    st.markdown("<h2 style='text-align: center;'>RESULTADOS - RoboAdvisor</h2>", unsafe_allow_html=True)

    # Texto justificado
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
    <br>En este apartado se presentan los resultados del backtesting realizado para la estrategia del RoboAdvidor
    basado en Algoritmos Genéticos.

    <br>Esta estrategia consiste en la obtención de la frontera eficiente de todo el universo de fondos de inversión y la
    adquisición de la mejor cartera. Esto se realiza en periodos de 6 meses, en los que se analiza el periodo inmediantamente
    anterior para la obtención de la cartera, y el mantenimiento de esa misma cartera durante el periodo. Al finalizar el periodo,
    se vuelve a lanzar el algoritmo genético con los datos del periodo finalizado, y se obtenie una nueva cartera.
                
    <br>El backtesting de esta estrategia ha consistido en la simulación del comportamiento de la cartera generada
    con el uso de este algoritmo 50 veces, a lo largo de todo el periodo comprendido entre el año 2005 y la actualidad,
    y la obtención de los percentiles de las carteras. Se muestra a continuación el Track Record de todas las carteras
    simuladas así como los percentiles 05, 50 y 95. Se muestra más adelante el detalle de cada uno de estos 3 percentiles.
                
    <br>Los resultados obtenidos son los siguientes:
    </div>
    """, unsafe_allow_html=True)


    # TRACK RECORD
    col1, col2, col3 = st.columns([0.5,2.5,0.5])
    with col2:
        st.image("pictures/1_Genetico/0_track_record.png", width=800)
    


    tab1, tab2, tab3 = st.tabs(["Percentil 05", "Percentil 50", "Percentil 95"])

    with tab1:

        st.markdown("""
        En las siguientes páginas se podrán encontrar los resultados obtenidos por el percentil
        05 de todos los RoboAdvisors simulados:
        
        - **Track Record** de la cartera  
        """, unsafe_allow_html=True)

            # TRACK RECORD
        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/1_tr_05.png", width=800)

        # SHARPE
        st.markdown("""
        - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/2_roll_05.png", width=800)

        # DISTRIBUCION RENDIMIENTOS
        st.markdown("""
        - Diagrama de la **distribución de rendimientos** de la cartera.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/3_distr_05.png", width=800)

        # TIME UNDER WATER
        st.markdown("""
        - Diagrama del **Time Under Water** y **Drawdown**. 
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/4_dd_05.png", width=800)

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
        50 de todos los RoboAdvisors simulados:
        
        - **Track Record** de la cartera  
        """, unsafe_allow_html=True)

            # TRACK RECORD
        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/5_tr.png", width=800)

        # SHARPE
        st.markdown("""
        - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/5_roll.png", width=800)

        # DISTRIBUCION RENDIMIENTOS
        st.markdown("""
        - Diagrama de la **distribución de rendimientos** de la cartera.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/5_dist.png", width=800)

        # TIME UNDER WATER
        st.markdown("""
        - Diagrama del **Time Under Water** y **Drawdown**. 
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/5_dd.png", width=800)

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
        95 de todos los RoboAdvisors simulados:
        
        - **Track Record** de la cartera  
        """, unsafe_allow_html=True)

            # TRACK RECORD
        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/95_tr.png", width=800)

        # SHARPE
        st.markdown("""
        - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/95_roll.png", width=800)

        # DISTRIBUCION RENDIMIENTOS
        st.markdown("""
        - Diagrama de la **distribución de rendimientos** de la cartera.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/95_dist.png", width=800)

        # TIME UNDER WATER
        st.markdown("""
        - Diagrama del **Time Under Water** y **Drawdown**. 
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/1_Genetico/95_dd.png", width=800)

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