import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim
import time

# --- 1. CONFIGURACIÓN E IMPORTACIONES ---
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

# --- 3. BASE DE DATOS DE TALLERES (PAYSANDÚ) ---
talleres = [
    {"nombre": "Taller Central CLS", "lat": -32.316, "lon": -58.083, "tel": "099417716", "dir": "Paysandú Centro"},
    {"nombre": "Auxilio Mecánico Norte", "lat": -32.300, "lon": -58.070, "tel": "098000000", "dir": "Av. Salto"},
}

# --- 4. ESTILOS CSS PERSONALIZADOS (ESTÉTICA F1) ---
st.markdown("""
    <style>
    /* Importar fuente estilo Tech/Racing de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;900&display=swap');

    /* Fondo y texto general */
    .stApp {
        background-color: #0b0f19; /* Azul muy oscuro tipo fibra de carbono */
        color: #e0e6ed;
    }

    /* Título Principal con efecto Neón Fluorescente */
    .f1-title {
        font-family: 'Exo 2', sans-serif;
        font-weight: 900;
        font-size: 4rem;
        text-align: center;
        color: #fff;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 
            0 0 5px #fff,
            0 0 10px #fff,
            0 0 20px #e63946, /* Rojo F1 */
            0 0 30px #e63946,
            0 0 40px #e63946;
        margin-bottom: 0;
    }

    .f1-subtitle {
        font-family: 'Exo 2', sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        text-align: center;
        color: #a8dadc;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: -10px;
        margin-bottom: 30px;
    }

    /* Subtítulos de sección tipo Panel de Control */
    .stMarkdown h2, .stMarkdown h3 {
        font-family: 'Exo 2', sans-serif;
        color: #fff;
        text-transform: uppercase;
        border-bottom: 2px solid #e63946;
        padding-bottom: 5px;
        margin-top: 20px;
    }

    /* Tarjetas de estado de escaneo */
    .f1-card {
        background-color: #161b2a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #1d3557;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    /* Efecto Neón para resultados de escaneo */
    .scan-ok {
        color: #25d366; /* Verde Fluorescente WA */
        font-weight: bold;
        text-shadow: 0 0 10px #25d366;
    }
    .scan-falla {
        color: #e63946; /* Rojo F1 */
        font-weight: bold;
        text-shadow: 0 0 10px #e63946;
    }

    /* Botones estilo F1 (Anchos, Tech) */
    .stButton>button {
        width: 100%;
        height: 70px;
        font-family: 'Exo 2', sans-serif;
        font-weight: 900;
        font-size: 1.5rem;
        background-color: #1d3557; /* Azul oscuro */
        color: white;
        border: 2px solid #e63946; /* Borde rojo */
        border-radius: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #e63946; /* Fondo rojo en hover */
        border-color: white;
        box-shadow: 0 0 15px #e63946;
    }

    /* Iconos automotrices en inputs */
    .stTextInput>div>div>input {
        background-color: #161b2a;
        color: white;
        border: 1px solid #1d3557;
    }

    </style>
    """, unsafe_allow_html=True)

# --- 5. DISEÑO DE LA APP (CON ESTÉTICA F1) ---
# Título y Subtítulo estilo F1 Neón
st.markdown("<h1 class='f1-title'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.markdown("<p class='f1-subtitle'>Powered by OBD-CLS Smart Tech</p>", unsafe_allow_html=True)
st.write("---")

# SELECCIÓN DE AUTO (Tipo Panel de Boxes)
st.markdown("<h3>📊 Telemetría: Identificación del Vehículo</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    marca_sel = st.selectbox("Marca:", [""] + list(datos_autos.keys()))
with col2:
    if marca_sel:
        modelo_sel = st.selectbox("Modelo:", datos_autos[marca_sel])
    else:
        st.info("Elegí una marca para cargar telemetría")

# SIMULACIÓN DE ESCANEO (Botón Launch Control)
st.markdown("---")
st.markdown("<h3>🚦 Launch Control: Diagnóstico Activo</h3>", unsafe_allow_html=True)
st.markdown('<div class="f1-card">', unsafe_allow_html=True) # Inicio Tarjeta
if st.button("🔄 INICIAR ESCANEO CHIP OBD-CLS"):
    with st.spinner("Comunicando con la ECU..."):
        time.sleep(2)
        st.markdown("<h2 class='scan-ok'>✅ SISTEMA OK. Sin fallas detectadas en el ciclo actual.</h2>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True) # Fin Tarjeta

# --- 6. SECCIÓN DEL MAPA (Tipo GPS de Pista) ---
st.markdown("---")
st.markdown("<h3>🛰️ GPS: Track Position y Boxes de Emergencia</h3>", unsafe_allow_html=True)
direccion_usuario = st.text_input("Ingresá tu ubicación actual:", "Paysandú, Uruguay")

try:
    geolocator = Nominatim(user_agent="scuderia_cls_v3", timeout=10)
    location = geolocator.geocode(direccion_usuario)

    puntos_mapa = []
    if location:
        # Tu ubicación con icono de auto
        puntos_mapa.append({"lat": location.latitude, "lon": location.longitude, "name": "Tu posición (Auto 1)"})
        st.caption(f"Posición confirmada: {location.address}")
    
    # Agregamos los talleres (Icono de Boxes)
    for t in talleres:
        puntos_mapa.append({"lat": t["lat"], "lon": t["lon"], "name": f"Boxes CLS: {t['nombre']}"})
    
    # Mostrar mapa
    st.map(pd.DataFrame(puntos_mapa))

except Exception:
    st.warning("Señal de GPS débil. Mostrando boxes predeterminados en Paysandú.")
    st.map(pd.DataFrame(talleres))

# LISTADO DE TALLERES (Boxes)
st.write("🛠️ **Zonas de Boxes Disponibles (Talleres Afiliados):**")
for t in talleres:
    with st.expander(f"📍 BOX: {t['nombre']}"):
        st.write(f"🏠 Ubicación: {t['dir']}")
        st.write(f"📞 Radio: {t['tel']}")
        link_wa = f"https://wa.me/598{t['tel']}?text=Necesito auxilio para un {marca_sel} {modelo_sel}"
        st.markdown(f"[📲 Contactar Box de Emergencia]({link_wa})")

st.sidebar.caption("Scuderia CLS - High Performance Tech 2026")
