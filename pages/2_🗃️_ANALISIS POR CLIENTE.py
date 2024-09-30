import streamlit as st
from controllers.analisis import *
import pandas as pd

st.set_page_config(page_title="Analisis de Creativos por Cliente", page_icon="🗃️")

# Título de la página
st.title("🗃️ Rendimiento de Creativos Por Cliente")

# Crear un menú en el sidebar
st.sidebar.title("Menú")
menu_option = st.sidebar.selectbox(
    "Selecciona una opción",
    ("Analizar Creativos por Cierres", "Analizar Creativos por Citas"),
)
# Obtener la lista de clientes
clientes = get_clients()
if clientes:
    cliente_seleccionado = st.selectbox("Selecciona un cliente", clientes)

    # Selectores de fecha opcionales
    st.write("### Filtrar por rango de fechas (opcional)")
    start_date = st.date_input("Fecha de inicio", value=None)
    end_date = st.date_input("Fecha de fin", value=None)

    # Convertir las fechas seleccionadas a formato string para enviarlas al backend
    start_date_str = start_date.strftime("%Y-%m-%d") if start_date else None
    end_date_str = end_date.strftime("%Y-%m-%d") if end_date else None

    # Lógica para mostrar datos según la opción seleccionada
    if menu_option == "Analizar Creativos por Cierres":
        st.write(f"Analizando creativos por cierres para {cliente_seleccionado}")
        datos_cierres = get_closed_data(
            cliente_seleccionado, start_date_str, end_date_str
        )
        df_cierres = pd.DataFrame(datos_cierres) if datos_cierres else pd.DataFrame()
        if df_cierres.empty:
            st.warning("No hay vídeos que analizar.")
        else:
            df_cierres["Tasa de Cierre"] = df_cierres["Tasa de Cierre"].map(
                "{:.2f}%".format
            )
            st.dataframe(df_cierres)
            # Selectbox para seleccionar el video y analizar calidad
            video_seleccionado = st.selectbox(
                "Selecciona un video para analizar su calidad",
                df_cierres["Video ID"].unique(),
            )
            if st.button("Analizar calidad"):
                # Enviar las fechas como parámetros opcionales al analizar la calidad
                calidad_datos = get_quality_data(
                    cliente_seleccionado,
                    video_seleccionado,
                    start_date_str,
                    end_date_str,
                )
                if calidad_datos:
                    df_calidad = pd.DataFrame(calidad_datos)
                    # Aplicar el formato de porcentaje a la columna "Porcentaje"
                    df_calidad["Porcentaje"] = df_calidad["Porcentaje"].map(
                        "{:.2f}%".format
                    )
                    st.dataframe(df_calidad)

    elif menu_option == "Analizar Creativos por Citas":
        st.write(f"Analizando creativos por citas para {cliente_seleccionado}")
        datos_citas = get_appointments_data(
            cliente_seleccionado, start_date_str, end_date_str
        )
        df_citas = pd.DataFrame(datos_citas) if datos_citas else pd.DataFrame()
        if df_citas.empty:
            st.warning("No hay vídeos que analizar.")
        else:
            df_citas["Tasa de Citas"] = df_citas["Tasa de Citas"].map("{:.2f}%".format)
            st.dataframe(df_citas)
            # Selectbox para seleccionar el video y analizar calidad
            video_seleccionado = st.selectbox(
                "Selecciona un video para analizar su calidad",
                df_citas["Video ID"].unique(),
            )
            if st.button("Analizar calidad"):
                calidad_datos = get_quality_data(
                    cliente_seleccionado,
                    video_seleccionado,
                    start_date_str,
                    end_date_str,
                )
                if calidad_datos:
                    df_calidad = pd.DataFrame(calidad_datos)
                    # Aplicar el formato de porcentaje a la columna "Porcentaje"
                    df_calidad["Porcentaje"] = df_calidad["Porcentaje"].map(
                        "{:.2f}%".format
                    )
                    st.dataframe(df_calidad)
