import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- CONFIGURACIÓN ESTÉTICA SCUDERIA ---
st.set_page_config(page_title="CLS Scuderia Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #1a1a1a; border-right: 3px solid #FFEB00; }
    .stButton>button { 
        width: 100%; border-radius: 5px; height: 3.5em; 
        background-color: #FF2800; color: white; border: 2px solid #FFEB00;
        font-weight: bold; font-size: 18px; text-transform: uppercase;
    }
    h1, h2, h3 { color: #FFEB00; font-family: 'Arial Black'; text-shadow: 2px 2px #FF2800; }
    .stExpander { background-color: #1a1a1a; border: 1px solid #FF2800; }
    .css-1offfwp { background-color: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE SIMULACIÓN MEJORADA ---
# Simulamos 10 casos con ubicación, fecha, repuestos y talleres nocturnos/diurnos
datos_simulados = [
    {
        "auto": "Chevrolet Corsa (2008)", 
        "falla": "P0130 - Sensor de Oxígeno", 
        "fecha": "08/01/2026", "hora": "23:15",
        "depto": "Canelones", "pueblo": "Pando", "calle": "Ruta 8 Km 24.500",
        "lat": -34.72, "lon": -55.95,
        "repuesto_link": "https://www.mercadolibre.com.uy/sensor-oxigeno-chevrolet-corsa-gm-original",
        "precio_repuesto": 1850, "mano_obra": 1200,
        "talleres": [
            {"nombre": "Taller Gustavo Diaz (Emergencia 24h)", "tel": "099 417 716", "tipo": "Nocturno"},
            {"nombre": "Auxilio Pando Nocturno", "tel": "098 000 111", "tipo": "Nocturno"}
        ]
    },
    {
        "auto": "Ford Fiesta (2011)", 
        "falla": "P0204 - Inyector Cilindro 4", 
        "fecha": "08/01/2026", "hora": "14:30",
        "depto": "Montevideo", "pueblo": "Pocitos", "calle": "Av. Brasil 2500",
        "lat": -34.91, "lon": -56.15,
        "repuesto_link": "https://www.mercadolibre.com.uy/inyector-nafta-ford-fiesta-kinetic-original",
        "precio_repuesto": 4500, "mano_obra": 2500,
        "talleres": [
            {"nombre": "Mecánica Gustavo Central", "tel": "099 417 716", "tipo": "Diurno"},
            {"nombre": "Inyección Montevideo", "tel": "091 222 333", "tipo": "Diurno"}
        ]
    }
]

# --- CONTROL DE ESTADO ---
if 'paso' not in st.session_state: st.session_state.paso = 0
def siguiente(): st.session_state.paso = (st.session_state.paso + 1) % len(datos_simulados)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/36/Scuderia_Ferrari_logo.svg/1200px-Scuderia_Ferrari_logo.svg.png", width=120)
    st.title("🏁 SCUDERIA CLS")
    st.write(f"👤 **Admin:** Gustavo Diaz")
    if st.button("🚀 SIMULAR SIGUIENTE AUTO"): siguiente()
    st.write("---")
    st.caption("Arquitectura de Alta Disponibilidad")

# --- CUERPO PRINCIPAL ---
caso = datos_simulados[st.session_state.paso]
es_noche = int(caso['hora'].split(':')[0]) >= 20 or int(caso['hora'].split(':')[0]) <= 6

st.title("🏎️ CLS SMART DIAGNOSTIC")

col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🔍 Reporte de Telemetría")
    st.write(f"📅 **Fecha:** {caso['fecha']} | ⌚ **Hora:** {caso['hora']}")
    st.write(f"📍 **Ubicación:** {caso['depto']}, {caso['pueblo']}")
    st.write(f"🛣️ **Referencia:** {caso['calle']}")
    
    if st.button("🧬 EJECUTAR ESCANEO SCUDERIA"):
        with st.spinner("Analizando protocolos OBD2..."):
            time.sleep(1.5)
            st.error(f"❌ FALLA: {caso['falla']}")
        
        st.write("### 🛠️ Costos Estimados")
        st.info(f"📦 **Repuesto (ML):** ${caso['precio_repuesto']} UYU")
        st.info(f"👨‍🔧 **Mano de Obra:** ${caso['mano_obra']} UYU")
        st.link_button("🛒 VER REPUESTO EN MERCADO LIBRE", caso['repuesto_link'])

with col2:
    st.write("### 📍 Mapa de Auxilio")
    map_data = pd.DataFrame({'lat': [caso['lat']], 'lon': [caso['lon']]})
    st.map(map_data, zoom=13)
    
    st.write("---")
    tipo_turno = "🌙 TALLERES DE EMERGENCIA NOCTURNA" if es_noche else "☀️ TALLERES HORARIO CENTRAL"
    st.subheader(tipo_turno)
    
    for t in caso['talleres']:
        with st.expander(f"📍 {t['nombre']}"):
            st.write(f"📞 Contacto: {t['tel']}")
            st.button(f"Pedir Grúa a {t['nombre']}", key=t['nombre'])

st.write("---")
msg = f"Reporte CLS - {caso['auto']}: Falla {caso['falla']} detectada en {caso['calle']}. Taller recomendado: {caso['talleres'][0]['nombre']}."
st.link_button("📩 ENVIAR INFORME DE EMERGENCIA AL CLIENTE", f"https://wa.me/?text={msg}", type="primary")
