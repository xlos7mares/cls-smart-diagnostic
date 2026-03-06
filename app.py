import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Scuderia CLS - Scanner", page_icon="🏎️", layout="centered")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main-title { color: #e63946; text-align: center; font-weight: bold; }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-weight: bold;
        background-color: #1d3557;
        color: white;
        border-radius: 10px;
    }
    .btn-wa {
        display: block;
        width: 100%;
        padding: 20px;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        text-decoration: none;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>Sistema de Diagnóstico y Escaneo Automotriz</b></p>", unsafe_allow_html=True)

# --- FORMULARIO DE DIAGNÓSTICO ---
with st.form("diagnostico_form"):
    st.subheader("📋 Datos del Vehículo")
    cliente = st.text_input("Nombre del Cliente:")
    vehiculo = st.text_input("Marca y Modelo (Ej: Chevrolet Onix):")
    anio = st.number_input("Año del vehículo:", min_value=1990, max_value=2026, value=2010)
    
    st.markdown("---")
    st.subheader("🔍 Informe del Escaneo")
    fallas = st.text_area("Códigos de falla detectados (DTC):", placeholder="P0300, P0171...")
    observaciones = st.text_area("Observaciones técnicas:")
    
    st.markdown("---")
    st.subheader("📍 Ubicación del Diagnóstico")
    ciudad = st.text_input("Ciudad:", "Paysandú, Uruguay")
    direccion = st.text_input("Dirección exacta (Calle y Nro):")

    # --- LÓGICA DINÁMICA DEL MAPA ---
    if direccion:
        try:
            geolocator = Nominatim(user_agent="scuderia_cls_app")
            ubicacion_completa = f"{direccion}, {ciudad}"
            location = geolocator.geocode(ubicacion_completa)
            
            if location:
                df_mapa = pd.DataFrame({'lat': [location.latitude], 'lon': [location.longitude]})
                st.map(df_mapa)
                st.caption(f"📍 Confirmado: {location.address}")
            else:
                st.warning("Dirección no encontrada. Se muestra punto general de la ciudad.")
                st.map(pd.DataFrame({'lat': [-32.31], 'lon': [-58.08]}))
        except:
            st.error("Error al cargar el mapa.")

    enviar = st.form_submit_button("✅ GENERAR REPORTE DE ESCANEO")

# --- ENVÍO DE RESULTADOS ---
if enviar:
    if cliente and vehiculo and direccion:
        st.balloons()
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        # Resumen para enviar por WhatsApp
        resumen_scan = (
            f"🏎️ *REPORTE SCUDERIA CLS*\n\n"
            f"📅 *Fecha:* {fecha_actual}\n"
            f"👤 *Cliente:* {cliente}\n"
            f"🚗 *Vehículo:* {vehiculo} ({anio})\n"
            f"⚠️ *Fallas:* {fallas}\n"
            f"📝 *Obs:* {observaciones}\n"
            f"📍 *Ubicación:* {direccion}, {ciudad}"
        )
        
        url_wa = f"https://wa.me/59899417716?text={urllib.parse.quote(resumen_scan)}"
        
        st.success("¡Reporte generado con éxito!")
        st.markdown(f"""
            <div style="background-color: #f1f8e9; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #2e7d32;">
                <h3>📊 REPORTE LISTO</h3>
                <p>Hacé clic abajo para enviar el informe al cliente o guardarlo en tu WhatsApp:</p>
                <a href="{url_wa}" target="_blank" class="btn-wa">
                    📲 ENVIAR REPORTE POR WHATSAPP
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Por favor, completa los datos del cliente, el vehículo y la ubicación.")

st.sidebar.caption("Scuderia CLS Tech 2026")
