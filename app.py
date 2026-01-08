import streamlit as st
import pandas as pd
import time

# --- CONFIGURACIÓN ESTÉTICA SCUDERIA ---
st.set_page_config(page_title="CLS Scuderia - Professional Diagnostic", layout="wide")

# Estilo Ferrari: Fondo Negro, Rojo Carrera y Amarillo Módena
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

# --- BASE DE DATOS DE SIMULACIÓN (10 CASOS) ---
# Coordenadas aproximadas de Uruguay para el mapa
datos_simulados = [
    {
        "auto": "Chevrolet Corsa (2008)", 
        "falla": "P0130 - Sensor de Oxígeno", 
        "lat": -34.88, "lon": -56.16, # Montevideo
        "talleres": [
            {"nombre": "Taller Gustavo Diaz Centro", "tel": "099 417 716", "dir": "Av. Italia 1234"},
            {"nombre": "Mecánica La Paz", "tel": "098 111 222", "dir": "Ruta 5 km 20"},
            {"nombre": "Electrónica Sayago", "tel": "091 333 444", "dir": "Propios 456"},
            {"nombre": "Inyección Prado", "tel": "094 555 666", "dir": "Millán 789"},
            {"nombre": "Servicio Técnico Sur", "tel": "092 777 888", "dir": "Rambla 101"}
        ]
    },
    {
        "auto": "Fiat Uno (2004)", 
        "falla": "P0300 - Fallo de Encendido", 
        "lat": -34.72, "lon": -56.21, # Las Piedras
        "talleres": [
            {"nombre": "Mecánica Gustavo Las Piedras", "tel": "099 417 716", "dir": "Ruta 48"},
            {"nombre": "Taller El Canario", "tel": "099 000 111", "dir": "Calle Principal 5"},
            {"nombre": "Repuestos Don Luis", "tel": "095 222 333", "dir": "Av. Artigas 44"},
            {"nombre": "Inyección Norte", "tel": "097 444 555", "dir": "Guaná 32"},
            {"nombre": "Taller Piedras Blancas", "tel": "093 666 777", "dir": "Ruta 67"}
        ]
    }
    # (Se pueden seguir sumando hasta 10 casos iguales)
]

# --- CONTROL DE ESTADO (SESSION STATE) ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0

def siguiente_vehiculo():
    st.session_state.paso = (st.session_state.paso + 1) % len(datos_simulados)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/36/Scuderia_Ferrari_logo.svg/1200px-Scuderia_Ferrari_logo.svg.png", width=120)
    st.title("🏁 GESTIÓN CLS")
    st.write(f"👤 **Administrador:** Gustavo Diaz")
    st.write("---")
    if st.button("🚀 SIMULADOR: SIGUIENTE VEHÍCULO"):
        siguiente_vehiculo()
    
    st.write("---")
    st.caption("Arquitectura Escalable 2026")

# --- CUERPO PRINCIPAL ---
caso = datos_simulados[st.session_state.paso]

st.title("🏎️ CLS SMART DIAGNOSTIC")
st.subheader(f"Vehículo en Proceso: {caso['auto']}")

col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🔍 Análisis de Motor")
    if st.button("🧬 INICIAR ESCANEO SCUDERIA"):
        with st.spinner("Procesando telemetría..."):
            time.sleep(1.5)
            st.error(f"❌ FALLA DETECTADA: {caso['falla']}")
            
        st.write("### 🏥 Red de Talleres Afiliados")
        for t in caso['talleres']:
            with st.expander(f"📍 {t['nombre']}"):
                st.write(f"📞 Teléfono: {t['tel']}")
                st.write(f"🏠 Dirección: {t['dir']}")
                st.button(f"Agendar en {t['nombre']}", key=t['nombre'])

with col2:
    st.write("### 📍 Ubicación GPS GPS")
    # Crear un mapa con la ubicación del auto y los talleres
    map_data = pd.DataFrame({'lat': [caso['lat']], 'lon': [caso['lon']]})
    st.map(map_data, zoom=12)
    st.info(f"El vehículo se encuentra detenido cerca de las coordenadas: {caso['lat']}, {caso['lon']}")

st.write("---")
mensaje_cliente = f"Resumen SCUDERIA CLS: Se detectó falla {caso['falla']} en su {caso['auto']}. Vea los talleres más cercanos en el link."
st.link_button("📩 ENVIAR DIAGNÓSTICO AL CLIENTE", f"https://wa.me/?text={mensaje_cliente}", type="primary")

st.caption("Propiedad Intelectual de Leonardo Olivera | Basado en Estándares de Rendimiento y Seguridad.")
