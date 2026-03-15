import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim
import time
import random
import obd 

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Scuderia CLS - Full Database", page_icon="🏎️", layout="wide")

# --- 2. BASE DE DATOS EXTENDIDA (MERCADO URUGUAY / MERCOSUR) ---
# Esta lista cubre la gran mayoría de vehículos compatibles con Vgate iCar2
datos_autos = {
    "Chevrolet": ["Corsa", "Astra", "Vectra", "S10", "Meriva", "Onix", "Aveo", "Cruze", "Captiva", "Spark", "Prisma", "Montana"],
    "Fiat": ["Uno", "Palio", "Siena", "Stilo", "Fiorino", "Punto", "Marea", "Idea", "Strada", "Cronos", "Argo", "Mobi"],
    "Volkswagen": ["Gol", "Golf", "Bora", "Passat", "Vento", "Saveiro", "Kombi", "Suran", "Fox", "Up!", "Amarok", "Polo"],
    "Hyundai": ["i10", "i20", "i30", "Accent", "Elantra", "Tucson", "Santa Fe", "HB20", "Creta", "H1", "Atos"],
    "Ford": ["Escort", "Fiesta", "Focus", "Ranger", "EcoSport", "Ka", "Mondeo", "Explorer", "F-100"],
    "Toyota": ["Corolla", "Hilux", "SW4", "Etios", "Yaris", "Rav4", "Celica", "Prius"],
    "Peugeot": ["106", "206", "207", "208", "306", "307", "308", "405", "406", "407", "408", "Partner", "3008"],
    "Renault": ["Clio", "Megane", "Laguna", "Kangoo", "19", "Twingo", "Logan", "Sandero", "Duster", "Oroch", "Kwid", "Fluence"],
    "Nissan": ["Sentra", "Tiida", "March", "Versa", "Frontier", "Kicks", "X-Trail", "Pathfinder"],
    "Honda": ["Civic", "City", "Fit", "HR-V", "CR-V", "Accord"],
    "Suzuki": ["Swift", "Celerio", "Alto", "Vitara", "Grand Vitara", "Jimny", "Baleno"],
    "Citroën": ["C3", "C4", "C5", "Berlingo", "Saxo", "Xsara", "Picasso"],
    "Kia": ["Rio", "Picanto", "Cerato", "Sportage", "Sorento", "K2700"],
    "Mitsubishi": ["L200", "Lancer", "Montero", "Mirage", "Outlander"],
    "BMW": ["Serie 1", "Serie 3", "Serie 5", "X1", "X3", "X5"],
    "Mercedes-Benz": ["Clase A", "Clase C", "Clase E", "Sprinter", "Vito"],
    "Audi": ["A1", "A3", "A4", "A6", "Q3", "Q5"]
}

talleres = [
    {"nombre": "Taller Central CLS", "lat": -32.316, "lon": -58.083, "tel": "099417716", "dir": "Paysandú Centro"},
    {"nombre": "Auxilio Mecánico Norte", "lat": -32.300, "lon": -58.070, "tel": "098000000", "dir": "Av. Salto"},
]

# --- 3. ESTILOS CSS F1 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;900&display=swap');
    .stApp { background-color: #0b0f19; color: #e0e6ed; }
    .f1-title {
        font-family: 'Exo 2', sans-serif; font-weight: 900; font-size: 3.5rem; 
        text-align: center; color: #fff; text-transform: uppercase;
        text-shadow: 0 0 10px #e63946, 0 0 20px #e63946; margin-bottom: 0px;
    }
    .gauge-container {
        text-align: center; background-color: #161b2a; padding: 20px;
        border-radius: 15px; border: 1px solid #e63946; margin: 5px;
    }
    .gauge-value {
        font-family: 'Exo 2', sans-serif; font-size: 2.5rem; font-weight: 900;
        color: #00f2ff; text-shadow: 0 0 10px #00f2ff;
    }
    .stButton>button {
        width: 100%; height: 70px; font-weight: 900; font-size: 1.5rem;
        background-color: #1d3557; color: white; border: 2px solid #e63946; border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='f1-title'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#a8dadc; text-transform:uppercase;'>Base de Datos Global de Diagnóstico</p>", unsafe_allow_html=True)

# --- PANEL DE SELECCIÓN ---
col_db1, col_db2 = st.columns(2)
with col_db1:
    # Ordenamos las marcas alfabéticamente para que sea fácil de encontrar
    marcas_ordenadas = sorted(list(datos_autos.keys()))
    marca_sel = st.selectbox("SELECCIONE MARCA:", [""] + marcas_ordenadas)
with col_db2:
    if marca_sel:
        modelo_sel = st.selectbox("SELECCIONE MODELO:", sorted(datos_autos[marca_sel]))
    else:
        st.info("Esperando selección de marca...")

st.markdown("---")

# --- TELEMETRÍA Y GRÁFICOS ---
if st.button("🔄 INICIAR ESCANEO DE SISTEMAS"):
    placeholder_gauges = st.empty()
    placeholder_chart = st.empty()
    historial_rpm = []
    
    for i in range(20):
        # Simulación de telemetría
        rpm = random.randint(850, 3500) if i > 3 else random.randint(850, 950)
        temp = random.randint(88, 92)
        presion = round(random.uniform(25.0, 32.0), 1)
        historial_rpm.append(rpm)
        
        with placeholder_gauges.container():
            c1, c2, c3 = st.columns(3)
            c1.markdown(f"<div class='gauge-container'><div style='color:#a8dadc'>RPM</div><div class='gauge-value'>{rpm}</div></div>", unsafe_allow_html=True)
            c2.markdown(f"<div class='gauge-container'><div style='color:#a8dadc'>MOTOR ºC</div><div class='gauge-value'>{temp}º</div></div>", unsafe_allow_html=True)
            c3.markdown(f"<div class='gauge-container'><div style='color:#a8dadc'>ACEITE PSI</div><div class='gauge-value'>{presion}</div></div>", unsafe_allow_html=True)
        
        placeholder_chart.line_chart(historial_rpm)
        time.sleep(0.3)
    st.success(f"Análisis finalizado para {marca_sel} {modelo_sel}")

st.markdown("---")

# --- MAPA ---
st.subheader("📍 Posición de Carrera y Boxes")
dir_input = st.text_input("Ubicación:", "Paysandú, Uruguay")
try:
    geolocator = Nominatim(user_agent="scuderia_cls_full_db", timeout=10)
    location = geolocator.geocode(dir_input)
    puntos = [{"lat": t["lat"], "lon": t["lon"]} for t in talleres]
    if location: puntos.append({"lat": location.latitude, "lon": location.longitude})
    st.map(pd.DataFrame(puntos))
except:
    st.map(pd.DataFrame(talleres))

# CONTACTO TALLERES
for t in talleres:
    with st.expander(f"🚩 BOX: {t['nombre']}"):
        st.write(f"📞 Radio: {t['tel']}")
        wa_link = f"https://wa.me/598{t['tel']}?text=ASISTENCIA F1: Mi {marca_sel} {modelo_sel} requiere soporte técnico."
        st.markdown(f"[📲 CONTACTAR INGENIERO]({wa_link})")

st.sidebar.caption("SCUDERIA CLS 2026 - Vgate iCar2 Compatible")
