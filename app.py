import streamlit as st
import scuderia_core
import time

# Configuración y Estilo F1
st.set_page_config(page_title="Scuderia CLS", page_icon="🏎️")

st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: white; }
    .stButton>button { 
        background-color: #e60000; color: white; 
        border-radius: 10px; font-weight: bold; width: 100%;
    }
    h1 { color: #e60000; border-bottom: 2px solid #e60000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏎️ SCUDERIA CLS - SMART SCAN")
st.markdown("### Desarrollador de Software: Leonardo Olivera")
st.info("Protocolo: OBD-II Universal (Compatible 2000-2026)")

# Función de escaneo corregida
def ejecutar_escaneo(nombre, cat):
    with st.status(f"Escaneando {nombre}...", expanded=True) as s:
        time.sleep(1)
        # LLAMADA CORREGIDA AQUÍ:
        res = scuderia_core.auto_prueba.motor_diagnostico(cat)
        s.update(label=f"{nombre} Analizado", state="complete")
    st.success(res)

st.write("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("🔧 Motor"): ejecutar_escaneo("Motor", "Motor")
    if st.button("⚡ Electricidad"): ejecutar_escaneo("Sistema Eléctrico", "Electricidad")

with col2:
    if st.button("🌡️ Sensores"): ejecutar_escaneo("Sensores", "Sensores")
    if st.button("❄️ Aire Acondicionado"): ejecutar_escaneo("Climatización", "Aire")

st.write("---")
if st.button("🚨 ESCANEO TOTAL DEL VEHÍCULO"):
    st.balloons()
    for c in ["Motor", "Sensores", "Electricidad", "Aire"]:
        st.write(f"**{c}:** {scuderia_core.auto_prueba.motor_diagnostico(c)}")
