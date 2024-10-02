import streamlit as st
from controllers.analisis import get_general_video_performance
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Análisis General de Creativos", page_icon="🗃️")

# Título de la página
st.title("🗃️ Rendimiento General de Creativos")


# Función para calcular el rango de fechas predefinido
def get_date_range(option):
    today = datetime.today()
    start_date = end_date = None

    if option == "Mes actual":
        start_date = today.replace(day=1)  # Primer día del mes actual
        end_date = today  # Hoy
    elif option == "Semana anterior":
        # Calcular el rango de la semana pasada (lunes a domingo)
        start_date = today - timedelta(days=today.weekday() + 7)  # Lunes anterior
        end_date = start_date + timedelta(days=6)  # Domingo anterior
    elif option == "Mes anterior":
        # Calcular el primer y último día del mes anterior
        first_day_of_current_month = today.replace(day=1)
        end_date = first_day_of_current_month - timedelta(
            days=1
        )  # Último día del mes anterior
        start_date = end_date.replace(day=1)  # Primer día del mes anterior
    elif option == "Máximo":
        start_date = None
        end_date = None

    return start_date, end_date


# Selectores de fecha predefinidos
st.write("### Selecciona un rango de fechas predefinido")
date_option = st.selectbox(
    "Opciones de fecha",
    (
        "Seleccionar manualmente",
        "Mes actual",
        "Semana anterior",
        "Mes anterior",
        "Máximo",
    ),
)

# Inicializar fechas en función de la opción seleccionada
if date_option == "Seleccionar manualmente":
    # Selectores de fecha manual
    start_date = st.date_input("Fecha de inicio", value=None)
    end_date = st.date_input("Fecha de fin", value=None)
else:
    # Calcular fechas basadas en la opción predefinida seleccionada
    start_date, end_date = get_date_range(date_option)
    st.write(
        f"Rango de fechas seleccionado: {start_date.strftime('%Y-%m-%d') if start_date else 'Sin inicio'} - {end_date.strftime('%Y-%m-%d') if end_date else 'Sin fin'}"
    )

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
