import streamlit as st
from controllers.analisis import get_general_video_performance
import pandas as pd

st.set_page_config(page_title="Análisis General de Creativos", page_icon="🗃️")

# Título de la página
st.title("🗃️ Rendimiento General de Creativos")

# Selectores de fecha opcionales
st.write("### Filtrar por rango de fechas (opcional)")
start_date = st.date_input("Fecha de inicio", value=None)
end_date = st.date_input("Fecha de fin", value=None)

# Convertir las fechas seleccionadas a formato string para enviarlas al backend
start_date_str = start_date.strftime("%Y-%m-%d") if start_date else None
end_date_str = end_date.strftime("%Y-%m-%d") if end_date else None


# Función para borrar la caché de análisis general
def clear_cache():
    get_general_video_performance.clear()


# Función para cargar los datos del análisis general con las fechas opcionales
def load_general_performance(start_date=None, end_date=None):
    return pd.DataFrame(get_general_video_performance(start_date, end_date))


# Estado de la aplicación para controlar la actualización de datos
if "reload_general_performance" not in st.session_state:
    st.session_state.reload_general_performance = False

# Botón para actualizar datos, ahora está al final de la página
if st.button("Actualizar análisis general"):
    clear_cache()  # Limpiar la caché
    st.session_state.reload_general_performance = (
        True  # Cambiar estado para forzar la recarga
    )
    general_performance = load_general_performance(
        start_date_str, end_date_str
    )  # Cargar datos inmediatamente tras limpiar la caché

# Decidir si cargar el DataFrame desde la caché o recargar desde el servidor
else:
    general_performance = load_general_performance(start_date_str, end_date_str)

# Mostrar los datos si están disponibles
if general_performance.empty:
    st.warning("No hay datos de análisis general disponibles.")
else:
    st.dataframe(general_performance)
