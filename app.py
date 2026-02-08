import streamlit as st
import scuderia_core
import pandas as pd
import time
import random

st.set_page_config(page_title="Scuderia CLS PRO", layout="wide")

# Estilo Senna Negro Metalizado
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stButton>button { background-color: #FDB927; color: #002776; border-radius: 10px; font-weight: bold; width: 100%; }
    .card { background: linear-gradient(145deg, #111, #222); border-left: 5px solid #FDB927; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .report-box { border: 1px solid #009B3A; padding: 10px; border-radius: 5px; margin-top: 5px; background-color: #001a0a; }
    </style>
    """, unsafe_allow_html=True)

if 'u_idx' not in st.session_state: st.session_state.u_idx = 0

cliente = scuderia_core.auto_prueba.obtener_cliente(st.session_state.u_idx)

# ENCABEZADO
st.title("🏎️ SCUDERIA CLS - CONTROL TOTAL")
st.subheader("Desarrollador de Software: Leonardo Olivera")

col_a, col_b = st.columns([1, 1.5])

with col_a:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"👤 **Cliente:** {cliente['nombre']}")
    st.write(f"🚗 **Vehículo:** {cliente['auto']}")
    st.write(f"📍 **Lugar:** {cliente['ciudad']}, {cliente['pais']}")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⏭️ CAMBIAR DE CLIENTE (1-30)"):
        st.session_state.u_idx = (st.session_state.u_idx + 1) % 30
        st.rerun()

    st.write("---")
    if st.button("🚨 EJECUTAR ESCANEO MOLECULAR COMPLETO"):
        with st.status("Analizando todos los sistemas...", expanded=True) as s:
            time.sleep(1.5)
            reporte = scuderia_core.auto_prueba.generar_escaneo_completo(cliente['motor_tipo'])
            
            for sistema, resultado in reporte.items():
                st.markdown(f"**{sistema}:**")
                st.info(resultado)
                # Si hay falla, mostrar comparativa
                if "⚠️" in resultado or "❌" in resultado:
                    st.write("🔍 *Comparativa de Repuestos:*")
                    precios = scuderia_core.auto_prueba.obtener_precios_repuesto(resultado, cliente['pais'])
                    for p in precios:
                        st.write(f"- {p['casa']}: {p['moneda']} {p['precio']} ({p['orig']})")
            
            s.update(label="Análisis Finalizado", state="complete")
        st.balloons()
        st.button("📩 Enviar este Reporte a mi WhatsApp")

with col_b:
    st.write("### 🛰️ RASTREO GPS Y ASISTENCIA")
    map_df = pd.DataFrame({'lat': [cliente['lat']], 'lon': [cliente['lon']]})
    st.map(map_df, zoom=11)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.error("🆘 ASISTENCIA SCUDERIA CLS")
    st.write(f"⛽ Estación más cercana a 2.4 km")
    st.write(f"🔧 Taller Afiliado en {cliente['pais']}: +598 99 123 456")
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("Arquitectura en la Nube - Agilidad y Disponibilidad")
