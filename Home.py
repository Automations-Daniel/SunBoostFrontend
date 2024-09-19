import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.sidebar.success("Navega por nuestro menú.")

# Título y descripción principal
st.markdown(
    "<h1 style='text-align: center;'>Análisis de Datos Disponibles</h1>",
    unsafe_allow_html=True,
)

# Mostrar imagen
img = "https://storage.googleapis.com/msgsndr/OZRtxP6T4EfAVabICsQJ/media/63af6f2c408c0b729901e2b0.png"
# Centro y redimensiono la imagen usando HTML y CSS
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; background-color: black; padding: 10px;">
        <img src="{img}" width="400">
    </div>
    """,
    unsafe_allow_html=True,
)

# Descripción de los análisis disponibles
st.write(
    '''
En esta plataforma encontrarás análisis detallados sobre el desempeño de tus campañas de marketing y creativos.
Ahora también puedes recibir alertas y acceder a un análisis general de tus campañas. 

Podrás explorar los siguientes tipos de análisis:

- **Análisis General**: Obtén una visión global del rendimiento de todas tus campañas y creativos.
- **Alertas**: Recibe notificaciones sobre eventos importantes o anomalías detectadas en tus campañas en Slack.
- **Análisis por Cierres**: Examina cómo tus creativos han contribuido a la conversión de leads en cierres.
- **Análisis por Citas**: Evalúa la efectividad de tus creativos en la generación de citas con clientes potenciales.
- **Análisis de Calidad**: Profundiza en la calidad de los leads generados y cómo se distribuyen a través de diferentes etapas.

Navega por nuestro menú para acceder a estos análisis y optimizar el rendimiento de tus campañas.
'''
)


# Botón de llamada a la acción
if st.button("Ir a la sección de análisis general"):
    st.switch_page("pages/1_🗃️_ANALISIS GENERAL.py")

# Botón de llamada a la acción
if st.button("Ir a la sección de análisis por cliente"):
    st.switch_page("pages/2_🗃️_ANALISIS POR CLIENTE.py")

# Sección de contacto
st.markdown("### ¿Tienes alguna pregunta?")
st.write(
    "Nuestro equipo de atención al cliente está siempre listo para ayudarte. [Contáctanos](mailto:automations@sunboostcrm.com)"
)

# Pie de página
st.markdown(
    """
---
**SunBoostCRM** - Agencia premium en generación de leads de Home Improvement & Eficiencia energética
"""
)
