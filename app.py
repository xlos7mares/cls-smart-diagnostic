import streamlit as st
import scuderia_core
import pandas as pd
import time

st.set_page_config(page_title="Scuderia CLS - Control Global", layout="wide")

# ESTILO SENNA + NEGRO METALIZADO + PUNTO GPS TITILANTE
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stButton>button { background-color: #FDB927; color: #002776; border-radius: 10px; font-weight: bold; width: 100%; }
    .card { background: linear-gradient(145deg, #111, #222); border: 1px solid #009B3A; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    
    /* Efecto punto GPS titilante */
    .gps-dot {
        height: 15px; width: 15px; background-color: #00ff00;
        border-radius: 50%; display: inline-block;
        box-shadow: 0 0 10px #00ff00;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.9); opacity: 0.7; }
        70% { transform: scale(1.2); opacity: 1; box-shadow: 0 0 20px #00ff00; }
        100% { transform: scale(0.9); opacity: 0.7; }
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica para cambiar de cliente (0 a 29)
if 'user_index' not in st.session_state:
    st.session_state.user_index = 0

def siguiente_cliente():
    st.session_state.user_index = (st.session_state.user_index + 1) % 30

# Obtener datos del cliente actual
cliente = scuderia_core.auto_prueba.obtener_cliente(st.session_state.user_index)

# ENCABEZADO
st.title("🏎️ SCUDERIA CLS - TELEMETRÍA GLOBAL")
st.button("⏭️ SIGUIENTE CLIENTE DE PRUEBA (Demo 1-30)", on_click=siguiente_cliente)

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown(f'<div class="card">', unsafe_allow_html=True)
    st.subheader("👤 PERFIL DEL USUARIO")
    st.write(f"**Nombre:** {cliente['nombre']}")
    st.write(f"**Vehículo:** {cliente['auto']}")
    st.write(f"**País:** {cliente['pais']}")
    st.write(f"**Ubicación:** {cliente['ciudad']}")
    st.markdown(f'UBICACIÓN REAL <span class="gps-dot"></span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⛽ SERVICIOS CERCANOS")
    dist = round(random.uniform(1.2, 5.5), 1)
    st.success(f"⛽ Estación ANCAP/YPF abierta a {dist} km")
    st.info("☕ Parador con Baños y Wi-Fi a 500m")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔍 ESCANEAR AHORA"):
        st.warning(f"⚠️ NECESITA: {cliente['repuesto']}")
        st.write("---")
        st.subheader("🛒 COMPARATIVA DE PRECIOS")
        tiendas = scuderia_core.auto_prueba.obtener_casas_repuestos(cliente['repuesto'], cliente['pais'])
        for t in tiendas:
            st.write(f"🏢 **{t['local']}**")
            st.write(f"💰 Precio: {t['moneda']} {t['precio']} | 🌏 Origen: {t['origen']}")
            st.write("---")
        st.button("📄 ENVIAR PDF A MI WHATSAPP")

with col2:
    st.write("### 📍 RASTREO SATELITAL (GPS)")
    # Creamos el mapa con la ubicación del cliente actual
    map_df = pd.DataFrame({'lat': [cliente['lat']], 'lon': [cliente['lon']]})
    st.map(map_df, zoom=12)
    
    st.error("🆘 TALLERES AFILIADOS SCUDERIA CLS (EMERGENCIA)")
    st.write("🚩 **Auxilio Mecánico Paysandú:** 099 000 111")
    st.write("🚩 **Taller Santiago (Chile):** +56 9 8888 7777")
    st.write("🚩 **Servicio Ruta 3 (Argentina):** +54 11 2222 3333")

st.caption(f"Visualizando cliente {st.session_state.user_index + 1} de 30 | Desarrollado por Leonardo Olivera")
