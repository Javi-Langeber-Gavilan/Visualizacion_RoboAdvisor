import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="TFM Javier Langeber Gavilán",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    # Título principal
    st.markdown("<h1 style='text-align: center;'>Desarrollo y Análisis de un RoboAdvisor basado en Algoritmos Genéticos</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Máster Universitario en Ingeniería Industrial - Universidad Politécnica de Madrid</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Trabajo de Fin de Master</h3>", unsafe_allow_html=True)

    # Imagen opcional
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.image("pictures/INTRO/logo-UPM.png", width=650, caption="UPM Logo")


    texto_intro = """
    <div style='text-align: justify; font-size: 16px;'>

    Este proyecto presenta el desarrollo, prueba y comparación de un <b>RoboAdvisor</b> 
    basado en un <b>Algoritmo Genético</b> para la selección de carteras de inversión eficientes.<br><br>

    El RoboAdvisor propuesto se compara con distintas estrategias de referencia, incluyendo 
    carteras generadas aleatoriamente, carteras compuestas por los mejores fondos en ventanas 
    temporales desplazadas (<i>rolling windows</i>), un benchmark sintético y una estrategia 
    de inversión <i>Buy & Hold</i>.<br><br>

    El análisis de resultados se aborda mediante un estudio exhaustivo de diversas métricas financieras: 
    evolución temporal de rentabilidades, volatilidades y ratios de Sharpe, así como el análisis del 
    <i>Maximum Drawdown (DD)</i>, el <i>Time Under Water (TUW)</i>, la distribución de rendimientos y la visualización 
    del histórico de rentabilidades (<i><b>Track Record</b></i>). Además, se examinan estas métricas aplicando 
    ventanas temporales móviles para capturar la dinámica temporal de cada estrategia.<br><br>

    La web aquí presentada se centra exclusivamente en el análisis comparativo de las estrategias de gestión de carteras. 
    Quedan recogidos en la memoria del trabajo el detalle del procesamiento de datos, el diseño e implementación 
    del algoritmo genético, las técnicas empleadas para la visualización de resultados y el desarrollo de los métodos 
    para la generación de datos sintéticos. No obstante, esta plataforma incluye los resultados obtenidos a partir 
    de dichos datos sintéticos para su evaluación en el contexto de robustez de las carteras.<br><br>

    La solución de visualización desarrollada permite comparar de forma intuitiva e interactiva los distintos enfoques 
    de gestión planteados, facilitando el análisis crítico de los resultados obtenidos a lo largo del estudio.

    </div>
    """

    st.markdown(texto_intro, unsafe_allow_html=True)


    # Objetivos del proyecto
    with st.expander("🎯 Objetivos del Proyecto"):
        st.markdown("""
        - Obtención automatizada de los Valores Liquidatios (NAVs) de los Fondos de Inversión presentes en [Morningstar](https://www.morningstar.es).
        - Diseño de un Algoritmo Genético para la gestión de carteras.
        - Generación de un RoboAdvisor mediante el uso del Algoritmo Genético creado.
        - Desarrollo de diferetnes técnicas de gestión de carteras para la comparación del RoboAdvisor.
        - Análisis del comportamiento histórico de las diferetnes estrategias de gestión de carteras.
        - Desarrollo y comparación de diferentes técnicas de generación de datos sintéticas para la creación de escenarios.
        - Construcción de una interfaz visual para la presentación de resultados.
        """)

    st.markdown("---")

    tab1, tab2 = st.tabs(["📈 Resultados", "🧠 Técncias"])




    with tab1:
        st.markdown("""
        En las siguientes páginas se podrán encontrar los siguientes resultados para
        cada una de las técnicas de gestión de carteras empleadas:
        
        - Diagrama del **Track Record** de la cartera  
        """, unsafe_allow_html=True)

            # TRACK RECORD
        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/INTRO/intro_track_record.png", width=800)

        # SHARPE
        st.markdown("""
        - Diagrama de la evolución temporal del **ratio de Sharpe**, **Rentabilidades** y **Volatilidades**.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/INTRO/intro_sharpe.png", width=800)

        # DISTRIBUCION RENDIMIENTOS
        st.markdown("""
        - Diagrama de la **distribución de rendimientos** de la cartera.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/INTRO/intro_returns.png", width=800)

        # TIME UNDER WATER
        st.markdown("""
        - Diagrama del **Time Under Water** y **Drawdown**. 
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            st.image("pictures/INTRO/intro_tuw.png", width=800)

        # CUADRO RATIOS FINANCIEROS
        st.markdown("""
        - Cuadro con el resumen de los **ratios financieros** para diferentes ventanas temporales.
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.5,2.5,0.5])
        with col2:
            df = pd.read_pickle('data/spx.pkl')
            st.dataframe(df)

    with tab2:
        st.markdown("""
        En este proyecto se han empleado diversas técnicas y herramientas avanzadas de desarrollo, computación y análisis de datos. Entre las principales se encuentran:

        - Desarrollo de código en **Python** orientado a la modelización financiera y optimización de carteras.
        - Empleo de **Algoritmos Genéticos** para la selección eficiente de carteras de inversión.
        - Aplicación de modelos de **Deep Learning Generativo (VAE)** para la generación de escenarios sintéticos.
        - Análisis y explotación de **APIs financieras** para la descarga automatizada de datos históricos (Morningstar, yfinance, etc.).
        - Procesamiento de datos HTML y JSON para la **extracción estructurada de información** desde webs financieras.
        - Programación de tareas periódicas con **crontabs** para la automatización de procesos y obtención diaria de datos.
        - **Visualización web interactiva** con Streamlit para presentar los resultados de forma accesible y clara.
        - Despliegue de la solución en la nube mediante **AWS EC2 y S3**, asegurando disponibilidad y escalabilidad.
        - Empleo de buenas prácticas en la **organización del código, separación de módulos y documentación**.
        - Uso de librerías especializadas como **NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow/Keras, DEAP, Streamlit**, entre otras.
        """)


# Créditos
st.markdown("---")
st.caption("Autor: Javier Langeber Gavilán | Máster Universitario en Ingeniería Industrial | Universidad Politécnica de Madrid")