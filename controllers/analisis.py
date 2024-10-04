import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"
CLIENTS_ENDPOINT = "/data/clients/"
GENERAL_ANALYSIS_ENDPOINT = "/data/general/video-performance"


@st.cache_data
def get_clients():
    response = requests.get(API_URL + CLIENTS_ENDPOINT)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error al obtener la lista de clientes: {response.status_code}")
        return []


def get_closed_data(client_name, start_date=None, end_date=None):
    params = {"start_date": start_date, "end_date": end_date}
    response = requests.get(f"{API_URL}/data/closed/{client_name}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error al obtener datos de cierres: {response.status_code}")
        return []


def get_appointments_data(client_name, start_date=None, end_date=None):
    params = {"start_date": start_date, "end_date": end_date}
    response = requests.get(f"{API_URL}/data/appointments/{client_name}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error al obtener datos de citas: {response.status_code}")
        return []


# Función ajustada para analizar la calidad con las fechas opcionales
def get_quality_data(client_name, start_date=None, end_date=None):
    # Agregar las fechas como parámetros opcionales
    params = {"start_date": start_date, "end_date": end_date}
    response = requests.get(f"{API_URL}/data/quality/{client_name}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error al obtener datos de calidad: {response.status_code}")
        return []


@st.cache_data
def get_general_video_performance(start_date=None, end_date=None):
    params = {"start_date": start_date, "end_date": end_date}
    response = requests.get(f"{API_URL}{GENERAL_ANALYSIS_ENDPOINT}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(
            f"Error al obtener el análisis general de rendimiento de videos: {response.status_code}"
        )
        return []
