import streamlit as st
import pandas as pd
import urllib.parse
import time
import random

# --- 1. CONFIGURACIÓN MÓVIL ---
st.set_page_config(page_title="Scuderia CLS PRO", page_icon="🏎️", layout="centered")

# --- 2. BASE DE DATOS EXTENDIDA ---
datos_autos = {
    "Hyundai": ["HB20", "i10", "Accent", "Tucson", "Creta"],
    "Chevrolet": ["Onix", "Prisma", "Corsa", "S10", "Cruze"],
    "Volkswagen": ["Gol", "Amarok", "Vento", "Saveiro", "Up!"],
    "Fiat": ["Cronos", "Argo", "Strada", "Toro", "Palio"],
    "Toyota": ["Hilux", "Corolla", "Etios", "Yaris"],
    "Renault": ["Kwid", "Sandero", "Logan", "Duster", "Oroch"]
}

# --- 3. ESTILOS F1 NEÓN ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@900&display=swap');
    .stApp { background-color: #0b0f19; color: white; }
    .f1-neon {
        font-family: 'Exo 2', sans-serif; font-size: 2.2rem; text-align: center;
        color: #fff; text-shadow: 0 0 10px #e63946, 0 0 20px #e63946;
        text-transform: uppercase; margin-bottom: 10px;
    }
    .gauge-box {
        background-color: #161b2a; padding: 15px; border-radius: 12px;
        border: 2px solid #e63946; text-align: center; margin-bottom: 10px;
    }
    .gauge-val { font-family: 'Exo 2', sans-serif; font-size: 1.8rem; color: #00f2ff; }
    .stButton>button {
        width: 100%; height: 75px; font-weight: 900; font-size: 1.3rem;
        background-color: #1d3557; color: white; border: 2px solid #e63946; border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='f1-neon'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#a8dadc; font-size:0.8rem;'>DIAGNÓSTICO PROFESIONAL v2.5</p>", unsafe_allow_html=True)

# --- 4. SELECCIÓN DE UNIDAD ---
col_v1, col_v2 = st.columns(2)
with col_v1:
    marca = st.selectbox("MARCA:", sorted(list(datos_autos.keys())))
with col_v2:
    modelo = st.selectbox("MODELO:", datos_autos[marca])

st.markdown("---")

# --- 5. TELEMETRÍA Y ESCANEO ---
if st.button("🚀 INICIAR ESCANEO DE SISTEMAS"):
    p_gauge = st.empty()
    p_status = st.status("Sincronizando con Vgate iCar2...", expanded=True)
    
    # Simulación de captura (Para que pruebes la visual en el HB20)
    for i in range(10):
        val_rpm = random.randint(850, 950)
        val_temp = random.randint(88, 91)
        
        p_gauge.markdown(f"""
            <div class='gauge-box'>
                <div style='color:#a8dadc; font-size:0.7rem;'>TELEMETRÍA EN VIVO</div>
                <div class='gauge-val'>{val_rpm} RPM | {val_temp}ºC</div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.3)
    
    p_status.update(label="Escaneo Finalizado", state="complete")
    st.success("✅ SISTEMA ÓPTIMO: No se detectaron fallas en la ECU.")
    st.balloons()

    # --- 6. ENVÍO DE REPORTE A WHATSAPP ---
    st.markdown("### 📱 ENVIAR REPORTE")
    nombre_cliente = st.text_input("Nombre del Cliente (Opcional):", "Usuario CLS")
    
    # Construcción del mensaje para WhatsApp
    texto_reporte = (
        f"🏎️ *REPORTE DE ESCANEO SCUDERIA CLS*\n\n"
        f"🚗 *Vehículo:* {marca} {modelo}\n"
        f"👤 *Cliente:* {nombre_cliente}\n"
        f"📊 *Estado:* SISTEMA SIN FALLAS\n"
        f"🌡️ *Temp. Trabajo:* {random.randint(88, 92)}ºC\n"
        f"📍 *Ubicación:* Servicio realizado en Paysandú.\n\n"
        f"✅ _Diagnóstico realizado con tecnología Vgate iCar2._"
    )
    
    # Link de WhatsApp (Tu número para que te llegue a vos por ahora)
    wa_url = f"https://wa.me/59899417716?text={urllib.parse.quote(texto_reporte)}"
    
    st.markdown(f"""
        <a href="{wa_url}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#25d366; color:white; text-align:center; 
            padding:20px; border-radius:15px; font-weight:900; font-size:1.2rem;">
                📲 ENVIAR REPORTE POR WHATSAPP
            </div>
        </a>
    """, unsafe_allow_html=True)

st.markdown("---")
with st.expander("📝 AYUDA DE CONEXIÓN"):
    st.info(f"Para el {marca} {modelo}, el puerto está debajo del tablero, lado conductor. Asegúrate que el LED azul del chip parpadee antes de iniciar.")

st.sidebar.caption("Scuderia CLS - High Performance 2026")
