import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Scuderia CLS - Smart Scan", page_icon="🏎️")

# --- BASE DE DATOS DE VEHÍCULOS (90s - 2010) ---
datos_autos = {
    "Chevrolet": ["Corsa", "Astra", "Vectra", "S10", "Meriva", "Onix (2010)", "Aveo"],
    "Fiat": ["Uno", "Palio", "Siena", "Stilo", "Fiorino", "Punto"],
    "Volkswagen": ["Gol", "Golf MK4", "Bora", "Passat", "Vento", "Saveiro", "Kombi"],
    "Ford": ["Escort", "Fiesta", "Focus", "Ranger", "EcoSport", "Ka"],
    "Peugeot": ["206", "207", "306", "307", "405", "Partner"],
    "Renault": ["Clio", "Megane", "Laguna", "Kangoo", "19", "Twingo"],
    "Toyota": ["Corolla", "Hilux", "SW4"],
}

# --- BASE DE DATOS DE TALLERES AFILIADOS ---
talleres = [
    {"nombre": "Taller Central CLS", "lat": -32.316, "lon": -58.083, "tel": "099417716", "dir": "Paysandú Centro"},
    {"nombre": "Auxilio Mecánico Norte", "lat": -32.300, "lon": -58.070, "tel": "098000000", "dir": "Av. Salto"},
]

# --- ESTILOS ---
st.markdown("""
    <style>
    .reporte-ok { background-color: #d4edda; padding: 20px; border-radius: 10px; border: 1px solid #c3e6cb; color: #155724; }
    .reporte-falla { background-color: #f8d7da; padding: 20px; border-radius: 10px; border: 1px solid #f5c6cb; color: #721c24; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏎️ SCUDERIA CLS: Smart Scan")
st.write("Diagnóstico en tiempo real vía Chip OBD-CLS")

# --- 1. SELECCIÓN DINÁMICA DE VEHÍCULO ---
st.subheader("🚗 Identificación del Vehículo")
marca_sel = st.selectbox("Seleccione la Marca:", [""] + list(datos_autos.keys()))

if marca_sel:
    modelo_sel = st.selectbox("Seleccione el Modelo:", datos_autos[marca_sel])
else:
    st.info("Seleccione una marca para ver los modelos.")

anio_sel = st.slider("Año del vehículo:", 1990, 2010, 2005)

# --- 2. SIMULACIÓN DE ESCANEO DEL CHIP ---
st.markdown("---")
st.subheader("📡 Estado del Escaneo")
if st.button("🔄 INICIAR ESCANEO DESDE CHIP"):
    with st.spinner("Comunicando con el módulo OBD-CLS..."):
        # Aquí iría la conexión real con el hardware
        import time
        time.sleep(2)
        
        # Simulación de resultado (puedes cambiar esto por lógica real)
        tiene_falla = False # Cambiar a True para probar el otro estado
        
        if not tiene_falla:
            st.markdown("""
                <div class="reporte-ok">
                    <h3>✅ SISTEMA SIN FALLAS</h3>
                    <p>Todos los sensores (Inyección, ABS, Airbag) reportan valores normales.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="reporte-falla">
                    <h3>⚠️ FALLA DETECTADA</h3>
                    <p>Código P0300: Detectada falla de encendido en cilindros.</p>
                </div>
            """, unsafe_allow_html=True)

# --- 3. MAPA Y TALLERES ---
st.markdown("---")
st.subheader("📍 Tu Ubicación y Talleres Cercanos")
direccion = st.text_input("Dirección actual (o dejar vacío para GPS):", "Paysandú, Uruguay")

geolocator = Nominatim(user_agent="scuderia_cls")
location = geolocator.geocode(direccion)

if location:
    # Crear datos para el mapa: Tu ubicación + Talleres
    puntos = []
    puntos.append({"lat": location.latitude, "lon": location.longitude, "nombre": "Tu Ubicación", "tipo": "usuario"})
    for t in talleres:
        puntos.append(t)
    
    df_puntos = pd.DataFrame(puntos)
    st.map(df_puntos)

    # Listado de Talleres
    st.write("🛠️ **Talleres de Emergencia Afiliados:**")
    for t in talleres:
        with st.expander(f"📍 {t['nombre']}"):
            st.write(f"🏠 Dirección: {t['dir']}")
            st.write(f"📞 Celular: {t['tel']}")
            wa_taller = f"https://wa.me/598{t['tel']}?text=Necesito auxilio mecánico para un {marca_sel} {modelo_sel}"
            st.markdown(f"[📲 Contactar Taller]( {wa_taller} )")

st.sidebar.caption("Scuderia CLS - Innovación Automotriz 2026")
