import streamlit as st
import scuderia_core
import pandas as pd
import time
import random  # <--- ESTO CORRIGE EL ERROR NAMEERROR

# Estética Senna + Negro Metalizado
st.set_page_config(page_title="Scuderia CLS - Senna Edition", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stButton>button { 
        background-color: #FDB927; color: #002776; 
        border: 2px solid #009B3A; font-weight: bold; border-radius: 15px;
    }
    .card { 
        background: linear-gradient(145deg, #111, #222); 
        border-left: 5px solid #FDB927; padding: 20px; border-radius: 10px; margin-bottom: 15px;
    }
    .gps-dot {
        height: 12px; width: 12px; background-color: #00ff00;
        border-radius: 50%; display: inline-block;
        box-shadow: 0 0 10px #00ff00;
        animation: pulse 1.5s infinite;
        margin-right: 10px;
    }
    @keyframes pulse {
        0% { transform: scale(0.9); opacity: 0.7; }
        70% { transform: scale(1.2); opacity: 1; box-shadow: 0 0 20px #00ff00; }
        100% { transform: scale(0.9); opacity: 0.7; }
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de navegación de clientes
if 'user_index' not in st.session_state:
    st.session_state.user_index = 0

def siguiente_cliente():
    st.session_state.user_index = (st.session_state.user_index + 1) % 30

# Obtener datos
cliente = scuderia_core.auto_prueba.obtener_cliente(st.session_state.user_index)

# ENCABEZADO SOLICITADO
st.title("🏎️ SCUDERIA CLS - SISTEMA GLOBAL")
st.subheader("Desarrollador de Software: Leonardo Olivera")

if st.button("⏭️ VER SIGUIENTE CLIENTE (Simulación 1 de 30)"):
    siguiente_cliente()
    st.rerun()

st.write("---")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'### <span class="gps-dot"></span> ESTADO ACTUAL', unsafe_allow_html=True)
    st.write(f"**Usuario:** {cliente['nombre']}")
    st.write(f"**Vehículo:** {cliente['auto']}")
    st.write(f"**Ubicación:** {cliente['ciudad']}, {cliente['pais']}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card" style="border-left: 5px solid #009B3A;">', unsafe_allow_html=True)
    st.write("### ⛽ SERVICIOS DE RUTA")
    dist = round(random.uniform(1.2, 5.5), 1)
    st.info(f"⛽ Estación de servicio abierta a {dist} km (Baños y Cafetería)")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🏁 INICIAR ESCANEO MOLECULAR"):
        with st.status("Sincronizando con satélite...", expanded=False):
            time.sleep(1)
            st.write("Analizando códigos OBD-II...")
            time.sleep(1)
        
        st.warning(f"⚠️ REPORTE: Necesita cambio de {cliente['repuesto']}")
        
        st.write("#### 🛒 COMPARATIVA DE PRECIOS AFILIADOS")
        tiendas = scuderia_core.auto_prueba.obtener_casas_repuestos(cliente['repuesto'], cliente['pais'])
        for t in tiendas:
            bandera = "🇺🇾" if cliente['pais'] == "Uruguay" else "🇦🇷" if cliente['pais'] == "Argentina" else "🇨🇱"
            st.markdown(f"""
            **{t['local']}** {bandera} Precio: {t['moneda']} {t['precio']} | *Origen: {t['origen']}*
            """)
        
        st.button("📄 ENVIAR REPORTE PDF A MI CELULAR")

with col2:
    st.write("### 📍 LOCALIZACIÓN GPS EN TIEMPO REAL")
    # Mapa que cambia según el cliente
    map_df = pd.DataFrame({'lat': [cliente['lat']], 'lon': [cliente['lon']]})
    st.map(map_df, zoom=12)
    
    st.markdown('<div style="background-color: #330000; padding: 15px; border-radius: 10px; border: 1px solid red;">', unsafe_allow_html=True)
    st.error("🆘 TALLERES AFILIADOS DE EMERGENCIA SCUDERIA CLS")
    st.write("📞 **Auxilio 24hs:** 0800-SCUDERIA")
    st.write(f"📞 **Taller local más cercano en {cliente['pais']}:** +598 99 000 000")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("Tecnología Ayrton Senna Legacy | Agilidad y Disponibilidad 2026")
