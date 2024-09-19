import streamlit as st
from controllers.analisis import get_general_video_performance
import pandas as pd

st.set_page_config(page_title="Análisis General de Creativos", page_icon="🗃️")

# Título de la página
st.title("🗃️ Rendimiento General de Creativos")


# Función para borrar la caché de análisis general
def clear_cache():
    get_general_video_performance.clear()


# Función para cargar los datos del análisis general
def load_general_performance():
    return pd.DataFrame(get_general_video_performance())


# Estado de la aplicación para controlar la actualización de datos
if "reload_general_performance" not in st.session_state:
    st.session_state.reload_general_performance = False

# Botón para actualizar datos, ahora está al final de la página
if st.button("Actualizar análisis general"):
    clear_cache()  # Limpiar la caché
    st.session_state.reload_general_performance = (
        True  # Cambiar estado para forzar la recarga
    )
    general_performance = (
        load_general_performance()
    )  # Cargar datos inmediatamente tras limpiar la caché

# Decidir si cargar el DataFrame desde la caché o recargar desde el servidor
else:
    general_performance = load_general_performance()

# Mostrar los datos si están disponibles
if general_performance.empty:
    st.warning("No hay datos de análisis general disponibles.")
else:
    st.dataframe(general_performance)
