import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

# 1. Crear el buscador de coordenadas (Geocodificador)
geolocator = Nominatim(user_agent="cls_app")

st.subheader("📍 Ubicación del Servicio")
ciudad = st.text_input("Ciudad y Departamento:", "Paysandú, Uruguay")
domicilio = st.text_input("Domicilio y Nro de Casa:")

# Combinamos la dirección para buscarla en el mapa
direccion_completa = f"{domicilio}, {ciudad}"

if domicilio:
    try:
        # 2. Convertir el texto en coordenadas reales
        location = geolocator.geocode(direccion_completa)
        
        if location:
            # 3. Crear un DataFrame con la latitud y longitud encontradas
            df_mapa = pd.DataFrame({
                'lat': [location.latitude],
                'lon': [location.longitude]
            })
            
            # 4. Mostrar el mapa centrado en esa dirección
            st.map(df_mapa)
            st.success(f"Ubicación verificada: {location.address}")
        else:
            st.warning("No pudimos encontrar la ubicación exacta en el mapa. Revisa la dirección.")
            # Mapa por defecto en Paysandú si falla la búsqueda
            st.map(pd.DataFrame({'lat': [-32.31], 'lon': [-58.08]}))
            
    except Exception as e:
        st.error("Error al cargar el mapa dinámico.")
