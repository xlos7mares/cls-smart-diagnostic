import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim
import time
import random # Para simular movimiento en la demo

# --- 1. CONFIGURACIÓN ---
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

talleres = [
    {"nombre": "Taller Central CLS", "lat": -32.316, "lon": -58.083, "tel": "099417716", "dir": "Paysandú Centro"},
    {"nombre": "Auxilio Mecánico Norte", "lat": -32.300, "lon": -58.070, "tel": "098000000", "dir": "Av. Salto"},
]

# --- 3. ESTILOS F1 NEÓN MEJORADOS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;900&display=swap');
    .stApp { background-color: #0b0f19; color: #e0e6ed; }
    .f1-title {
        font-family: 'Exo 2', sans-serif;
        font-weight: 900; font-size: 3.5rem; text-align: center; color: #fff;
        text-transform: uppercase; letter-spacing: 2px;
        text-shadow: 0 0 10px #e63946, 0 0 20px #e63946;
        margin-bottom: 0px;
    }
    .f1-subtitle {
        font-family: 'Exo 2', sans-serif; text-align: center; color: #a8dadc; 
        text-transform: uppercase; margin-top: -10px; margin-bottom: 30px;
    }
    .gauge-container {
        text-align: center; background-color: #161b2a; padding: 20px;
        border-radius: 15px; border: 1px solid #1d3557; margin: 10px;
    }
    .gauge-value {
        font-family: 'Exo 2', sans-serif; font-size: 2.5rem; font-weight: 900;
        color: #00f2ff; text-shadow: 0 0 10px #00f2ff;
    }
    .gauge-label { color: #a8dadc; text-transform: uppercase; font-size: 0.9rem; }
    .stButton>button {
        width: 100%; height: 80px; font-family: 'Exo 2', sans-serif; font-weight: 900;
        font-size: 1.5rem; background-color: #1d3557; color: white;
        border: 2px solid #e63946; border-radius: 15px; text-transform: uppercase;
    }
    .stButton>button:hover { background-color: #e63946; box-shadow: 0 0 20px #e63946; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. INTERFAZ ---
st.markdown("<h1 class='f1-title'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.markdown("<p class='f1-subtitle'>OBD-CLS High Performance Monitoring</p>", unsafe_allow_html=True)

# TELEMETRÍA DE SELECCIÓN
st.markdown("### 📊 BOXES: CONFIGURACIÓN DE UNIDAD")
col_m, col_mod = st.columns(2)
with col_m:
    marca_sel = st.selectbox("MARCA:", [""] + list(datos_autos.keys()))
with col_mod:
    if marca_sel:
        modelo_sel = st.selectbox("MODELO:", datos_autos[marca_sel])
    else:
        st.info("SELECCIONE MARCA")

st.markdown("---")

# DASHBOARD EN VIVO
st.markdown("### 📡 TELEMETRÍA EN TIEMPO REAL")
if st.button("🔄 ACTIVAR SENSORES DE MOTOR"):
    # Espacio para los relojes
    placeholder = st.empty()
    
    # Simulación de lectura de sensores (para la demo con Gustavo)
    for i in range(10): # Lo hace 10 veces para que se vea el movimiento
        with placeholder.container():
            c1, c2, c3 = st.columns(3)
            # Valores simulados que oscilan
            rpm = random.randint(850, 950) # Ralentí
            temp = random.randint(88, 92)  # Temperatura óptima
            presion = round(random.uniform(25.5, 28.2), 1) # PSI de aceite
            
            with c1:
                st.markdown(f"<div class='gauge-container'><div class='gauge-label'>Motor RPM</div><div class='gauge-value'>{rpm}</div></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='gauge-container'><div class='gauge-label'>Temperatura ºC</div><div class='gauge-value'>{temp}º</div></div>", unsafe_allow_html=True)
            with c3:
                st.markdown(f"<div class='gauge-container'><div class='gauge-label'>Presión Aceite (PSI)</div><div class='gauge-value'>{presion}</div></div>", unsafe_allow_html=True)
        time.sleep(0.5)
    st.success("✅ CONEXIÓN ESTABLE CON ECU - DATOS SINCRONIZADOS")

st.markdown("---")

# GPS Y MAPA
st.markdown("### 🛰️ TRACK POSITION: AUXILIO MECÁNICO")
dir_input = st.text_input("UBICACIÓN ACTUAL:", "Paysandú, Uruguay")

try:
    geolocator = Nominatim(user_agent="scuderia_cls_demo", timeout=10)
    location = geolocator.geocode(dir_input)
    puntos = []
    if location:
        puntos.append({"lat": location.latitude, "lon": location.longitude, "name": "TU UNIDAD"})
    for t in talleres:
        puntos.append(t)
    st.map(pd.DataFrame(puntos))
except:
    st.map(pd.DataFrame(talleres))

# BOXES (TALLERES)
for t in talleres:
    with st.expander(f"🚩 BOX DISPONIBLE: {t['nombre']}"):
        st.write(f"📞 RADIO: {t['tel']}")
        wa_link = f"https://wa.me/598{t['tel']}?text=ASISTENCIA: Mi {marca_sel} {modelo_sel} reporta baja presión de aceite."
        st.markdown(f"[📲 CONTACTAR INGENIERO]({wa_link})")

st.sidebar.caption("SCUDERIA CLS - Racing Tech 2026")
