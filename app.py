import streamlit as st
import pandas as pd
import time
import urllib.parse

# --- CONFIGURACIÓN ESTÉTICA SCUDERIA ---
st.set_page_config(page_title="CLS Scuderia Pro - 2026", layout="wide")

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
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIÓN PARA GENERAR LINKS REALES DE MERCADO LIBRE URUGUAY ---
def link_ml(repuesto, auto):
    query = f"{repuesto} {auto}"
    # Formato de búsqueda real para ML Uruguay
    return f"https://listado.mercadolibre.com.uy/{urllib.parse.quote(query)}#D[A:{urllib.parse.quote(query)}]"

# --- BASE DE DATOS DE SIMULACIÓN MEJORADA (10 CASOS) ---
datos_simulados = [
    {
        "auto": "Chevrolet Corsa", "falla": "P0130 - Sensor de Oxígeno", "fecha": "08/01/2026", "hora": "23:15",
        "depto": "Canelones", "pueblo": "Pando", "calle": "Ruta 8 Km 24.500", "lat": -34.72, "lon": -55.95,
        "repuesto": "Sensor de Oxígeno", "precio_est": 1850, "mano_obra": 1200,
        "talleres": [{"nombre": "Taller Gustavo Diaz (Nocturno)", "tel": "099 417 716", "tipo": "Nocturno"}]
    },
    {
        "auto": "VW Gol G5", "falla": "P0300 - Bobina de Encendido", "fecha": "08/01/2026", "hora": "10:00",
        "depto": "Montevideo", "pueblo": "Sayago", "calle": "Av. Millán y Propios", "lat": -34.85, "lon": -56.19,
        "repuesto": "Bobina de Encendido", "precio_est": 2400, "mano_obra": 800,
        "talleres": [{"nombre": "Mecánica Gustavo Central", "tel": "099 417 716", "tipo": "Diurno"}]
    },
    {
        "auto": "Fiat Uno Fire", "falla": "P0115 - Sensor Temperatura", "fecha": "09/01/2026", "hora": "02:45",
        "depto": "Maldonado", "pueblo": "San Carlos", "calle": "Ruta 39 Km 15", "lat": -34.79, "lon": -54.91,
        "repuesto": "Sensor Temperatura Agua", "precio_est": 950, "mano_obra": 1500,
        "talleres": [{"nombre": "Auxilio Gustavo Este (24h)", "tel": "099 417 716", "tipo": "Nocturno"}]
    }
]

# --- CONTROL DE ESTADO ---
if 'paso' not in st.session_state: st.session_state.paso = 0
def siguiente(): st.session_state.paso = (st.session_state.paso + 1) % len(datos_simulados)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/36/Scuderia_Ferrari_logo.svg/1200px-Scuderia_Ferrari_logo.svg.png", width=120)
    st.title("🏁 SCUDERIA CLS")
    if st.button("🚀 SIMULAR SIGUIENTE VEHÍCULO"): siguiente()
    st.write("---")
    st.info(f"Admin Logged: **Gustavo Diaz**")

# --- CUERPO PRINCIPAL ---
caso = datos_simulados[st.session_state.paso]
es_noche = int(caso['hora'].split(':')[0]) >= 20 or int(caso['hora'].split(':')[0]) <= 6

st.title("🏎️ CLS SMART DIAGNOSTIC")

col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🔍 Telemetría en Tiempo Real")
    st.write(f"📅 **Fecha:** {caso['fecha']} | ⌚ **Hora:** {caso['hora']}")
    st.write(f"📍 **Ubicación:** {caso['depto']}, {caso['pueblo']}")
    st.write(f"🛣️ **Referencia:** {caso['calle']}")
    
    if st.button("🧬 EJECUTAR ANÁLISIS SCUDERIA"):
        with st.spinner("Escaneando protocolos..."):
            time.sleep(1)
            st.error(f"❌ FALLA DETECTADA: {caso['falla']}")
        
        st.write("### 🛠️ Desglose de Costos")
        col_r, col_m = st.columns(2)
        col_r.metric("Repuesto (Aprox)", f"${caso['precio_est']} UYU")
        col_m.metric("Mano de Obra", f"${caso['mano_obra']} UYU")
        
        st.link_button(f"🛒 VER {caso['repuesto'].upper()} EN MERCADO LIBRE", link_ml(caso['repuesto'], caso['auto']))

with col2:
    st.write("### 📍 Ubicación GPS")
    map_data = pd.DataFrame({'lat': [caso['lat']], 'lon': [caso['lon']]})
    st.map(map_data, zoom=13)
    
    tipo_t = "🌙 AUXILIO NOCTURNO DISPONIBLE" if es_noche else "☀️ TALLERES HORARIO CENTRAL"
    st.subheader(tipo_t)
    for t in caso['talleres']:
        with st.expander(f"📍 {t['nombre']}"):
            st.write(f"📞 Contacto: {t['tel']}")
            st.write("✅ Taller verificado por el sistema CLS.")

st.write("---")
msg = f"Reporte SCUDERIA CLS: {caso['auto']} - Falla {caso['falla']}. Ubicado en {caso['calle']}. Presupuesto estimado: ${caso['precio_est'] + caso['mano_obra']} UYU."
st.link_button("📩 ENVIAR INFORME DE EMERGENCIA AL CLIENTE", f"https://wa.me/?text={urllib.parse.quote(msg)}", type="primary")
