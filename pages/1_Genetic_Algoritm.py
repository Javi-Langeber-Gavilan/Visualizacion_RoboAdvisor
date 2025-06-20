import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide")

# Establecemos la columna con contenido centrado
col1, col2, col3 = st.columns([1, 2, 1])  # Esto da un "ancho" ajustable al contenido central (columna 2)

# Columna central (ajustamos su tamaño)
with col2:
    # Título centrado
    st.markdown("<h1 style='text-align: center;'>Título del Proyecto</h1>", unsafe_allow_html=True)

    # Texto justificado
    st.markdown("""
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
    """, unsafe_allow_html=True)
