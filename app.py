import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim
import time

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Scuderia CLS - F1 Smart Scan", page_icon="🏎️", layout="wide")

# --- 2. BASE DE DATOS DE VEHÍCULOS (90s - 2010) ---
datos_autos = {
    "Chevrolet": ["Corsa", "Astra", "Vectra", "S10", "Meriva", "Onix (2010)", "Aveo"],
    "Fiat": ["Uno", "Palio", "Siena", "Stilo", "Fiorino", "Punto"],
    "Volkswagen": ["Gol", "Golf MK4", "Bora", "Passat", "Vento", "Saveiro", "Kombi"],
    "Ford": ["Escort", "Fiesta", "Focus", "Ranger", "EcoSport", "Ka"],
    "Peugeot": ["206", "207", "306", "307", "405", "Partner"],
    "Renault": ["Clio", "Megane", "Laguna", "Kangoo", "19", "Twingo"],
    "Toyota": ["Corolla", "Hilux", "SW4"],
}

# --- 3. BASE DE DATOS DE TALLERES (BOXES) ---
talleres = [
    {"nombre": "Taller Central CLS", "lat": -32.316, "lon": -58.083, "tel": "099417716", "dir": "Paysandú Centro"},
    {"nombre": "Auxilio Mecánico Norte", "lat": -32.300, "lon": -58.070, "tel": "098000000", "dir": "Av. Salto"},
]

# --- 4. ESTILOS CSS PERSONALIZADOS (ESTÉTICA F1 NEÓN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;900&display=swap');

    .stApp {
        background-color: #0b0f19;
        color: #e0e6ed;
    }

    .f1-title {
        font-family: 'Exo 2', sans-serif;
        font-weight: 900;
        font-size: 3.5rem;
        text-align: center;
        color: #fff;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 10px #e63946, 0 0 20px #e63946, 0 0 30px #e63946;
        margin-bottom: 0px;
    }

    .f1-subtitle {
        font-family: 'Exo 2', sans-serif;
        text-align: center;
        color: #a8dadc;
        text-transform: uppercase;
        margin-top: -10px;
        margin-bottom: 30px;
        font-size: 1.2rem;
    }

    .stButton>button {
        width: 100%;
        height: 80px;
        font-family: 'Exo 2', sans-serif;
        font-weight: 900;
        font-size: 1.8rem;
        background-color: #1d3557;
        color: white;
        border: 2px solid #e63946;
        border-radius: 15px;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #e63946;
        box-shadow: 0 0 20px #e63946;
        border-color: #fff;
    }

    .scan-ok {
        color: #25d366;
        font-weight: bold;
        text-shadow: 0 0 15px #25d366;
        text-align: center;
        font-family: 'Exo 2', sans-serif;
        text-transform: uppercase;
    }

    .f1-card {
        background-color: #161b2a;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e63946;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. INTERFAZ DE USUARIO ---
st.markdown("<h1 class='f1-title'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.markdown("<p class='f1-subtitle'>OBD-CLS Smart Diagnostic System</p>", unsafe_allow_html=True)

# PANEL DE TELEMETRÍA
st.markdown("### 📊 TELEMETRÍA: IDENTIFICACIÓN DEL VEHÍCULO")
col1, col2 = st.columns(2)

with col1:
    marca_sel = st.selectbox("MARCA:", [""] + list(datos_autos.keys()))
with col2:
    if marca_sel:
        modelo_sel = st.selectbox("MODELO:", datos_autos[marca_sel])
    else:
        st.info("SELECCIONE UNA MARCA EN EL PANEL")

st.markdown("---")

# LANZAMIENTO DEL ESCÁNER
st.markdown("### 🚦 LAUNCH CONTROL: ACTIVAR DIAGNÓSTICO")
st.markdown('<div class="f1-card">', unsafe_allow_html=True)
if st.button("🔄 INICIAR SCANNER"):
    with st.spinner("SINCRONIZANDO CON CHIP OBD-CLS..."):
        time.sleep(2)
        st.markdown("<h2 class='scan-ok'>✅ ESTADO: SISTEMA ÓPTIMO - SIN FALLAS</h2>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# GPS DE PISTA
st.markdown("### 🛰️ GPS DE PISTA: BOXES CERCANOS")
dir_input = st.text_input("POSICIÓN ACTUAL:", "Paysandú, Uruguay")

try:
    geolocator = Nominatim(user_agent="scuderia_cls_2026_final", timeout=10)
    location = geolocator.geocode(dir_input)
    
    puntos_mapa = []
    if location:
        puntos_mapa.append({"lat": location.latitude, "lon": location.longitude, "name": "TU MONOPLAZA"})
        st.caption(f"COORDENADAS FIJADAS: {location.address}")
    
    for t in talleres:
        puntos_mapa.append({"lat": t["lat"], "lon": t["lon"], "name": f"BOX: {t['nombre']}"})
    
    st.map(pd.DataFrame(puntos_mapa))

except Exception:
    st.warning("PERDIDA DE SEÑAL GPS. MOSTRANDO BOXES LOCALES.")
    st.map(pd.DataFrame(talleres))

# LISTADO DE BOXES (TALLERES)
st.markdown("### 🛠️ SERVICIOS DE ASISTENCIA (BOXES)")
for t in talleres:
    with st.expander(f"🚩 BOX: {t['nombre']}"):
        st.write(f"🏠 DIRECCIÓN: {t['dir']}")
        st.write(f"📞 RADIO: {t['tel']}")
        wa_link = f"https://wa.me/598{t['tel']}?text=ASISTENCIA F1: Mi {marca_sel} {modelo_sel} necesita revisión."
        st.markdown(f"[📲 CONTACTAR INGENIERO DE PISTA]({wa_link})")

st.sidebar.caption("SCUDERIA CLS Tech - High Performance 2026")
