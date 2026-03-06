import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim
import time

# --- 1. CONFIGURACIÓN E IMPORTACIONES (ESTO EVITA EL NAMEERROR) ---
st.set_page_config(page_title="Scuderia CLS - Smart Scan", page_icon="🏎️")

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
]

# --- 4. DISEÑO DE LA APP ---
st.markdown("<h1 style='text-align: center; color: #e63946;'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.write("---")

# SELECCIÓN DE AUTO
st.subheader("🚗 Identificación del Vehículo")
col1, col2 = st.columns(2)

with col1:
    marca_sel = st.selectbox("Marca:", [""] + list(datos_autos.keys()))
with col2:
    if marca_sel:
        modelo_sel = st.selectbox("Modelo:", datos_autos[marca_sel])
    else:
        st.info("Elegí una marca")

# SIMULACIÓN DE ESCANEO
st.markdown("---")
if st.button("🔄 INICIAR ESCANEO DESDE CHIP"):
    with st.spinner("Conectando con Chip OBD-CLS..."):
        time.sleep(2)
        st.success("✅ SISTEMA ESCANEADO: Sin fallas detectadas.")

# --- 5. SECCIÓN DEL MAPA (CON PROTECCIÓN DE ERRORES) ---
st.markdown("---")
st.subheader("📍 Tu Ubicación y Talleres Cercanos")
direccion_usuario = st.text_input("Ingresá tu dirección actual:", "Paysandú, Uruguay")

try:
    # Usamos un timeout largo para evitar que la app se trabe
    geolocator = Nominatim(user_agent="scuderia_cls_v2", timeout=10)
    location = geolocator.geocode(direccion_usuario)

    puntos_mapa = []
    if location:
        puntos_mapa.append({"lat": location.latitude, "lon": location.longitude, "name": "Tu posición"})
        st.caption(f"Dirección detectada: {location.address}")
    
    # Agregamos los talleres al mapa
    for t in talleres:
        puntos_mapa.append({"lat": t["lat"], "lon": t["lon"], "name": t["nombre"]})
    
    # Mostrar mapa
    st.map(pd.DataFrame(puntos_mapa))

except Exception:
    st.warning("El servicio de mapas está lento. Mostrando talleres en zona central.")
    st.map(pd.DataFrame(talleres))

# LISTADO DE TALLERES DE EMERGENCIA
st.write("🛠️ **Talleres Disponibles:**")
for t in talleres:
    with st.expander(f"📍 {t['nombre']}"):
        st.write(f"🏠 Dirección: {t['dir']}")
        st.write(f"📞 Contacto: {t['tel']}")
        link_wa = f"https://wa.me/598{t['tel']}?text=Necesito auxilio para un {marca_sel} {modelo_sel}"
        st.markdown(f"[📲 Enviar mensaje de auxilio]({link_wa})")

st.sidebar.caption("Scuderia CLS Tech 2026")
