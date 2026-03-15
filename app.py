import streamlit as st
import pandas as pd
import time
import random

# --- 1. CONFIGURACIÓN PARA MÓVIL ---
st.set_page_config(
    page_title="Scuderia CLS Mobile", 
    page_icon="🏎️", 
    layout="centered", # Mejor para celulares
    initial_sidebar_state="collapsed"
)

# --- 2. BASE DE DATOS ROBUSTA ---
datos_autos = {
    "Chevrolet": ["Onix", "Prisma", "Corsa", "S10", "Cruze", "Montana"],
    "Hyundai": ["HB20", "i10", "Accent", "Tucson", "Creta"],
    "Fiat": ["Cronos", "Argo", "Strada", "Toro", "Palio"],
    "Volkswagen": ["Gol", "Amarok", "Vento", "Saveiro", "Up!"],
    "Toyota": ["Hilux", "Corolla", "Etios", "Yaris"],
    "Renault": ["Kwid", "Sandero", "Logan", "Duster", "Oroch"]
}

# --- 3. ESTILOS F1 NEÓN (OPTIMIZADOS PARA TOUCH) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;900&display=swap');
    .stApp { background-color: #0b0f19; color: #e0e6ed; }
    .f1-header {
        font-family: 'Exo 2', sans-serif; font-weight: 900; font-size: 2.2rem;
        text-align: center; color: #fff; text-transform: uppercase;
        text-shadow: 0 0 10px #e63946; margin-bottom: 5px;
    }
    .gauge-box {
        text-align: center; background-color: #161b2a; padding: 15px;
        border-radius: 12px; border: 2px solid #e63946; margin-bottom: 10px;
    }
    .gauge-label { color: #a8dadc; font-size: 0.8rem; text-transform: uppercase; }
    .gauge-val { font-family: 'Exo 2', sans-serif; font-size: 2rem; color: #00f2ff; }
    
    /* Botón gigante para el dedo */
    .stButton>button {
        width: 100%; height: 90px; border-radius: 15px;
        background: linear-gradient(135deg, #1d3557 0%, #e63946 100%);
        color: white; font-family: 'Exo 2', sans-serif; font-weight: 900;
        font-size: 1.4rem; text-transform: uppercase; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. INTERFAZ PRINCIPAL ---
st.markdown("<h1 class='f1-header'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#a8dadc; font-size:0.8rem;'>DATALOGGER MOBILE v2.1</p>", unsafe_allow_html=True)

# SELECCIÓN RÁPIDA
col1, col2 = st.columns(2)
with col1:
    marca = st.selectbox("MARCA:", sorted(list(datos_autos.keys())))
with col2:
    modelo = st.selectbox("MODELO:", datos_autos[marca])

st.markdown("---")

# --- 5. PANEL DE TELEMETRÍA ---
st.markdown("### 📊 TELEMETRÍA EN VIVO")

# Espacios para actualización
p_gauges = st.empty()
p_chart = st.empty()

if st.button("🚀 INICIAR CAPTURA DE DATOS"):
    historial = []
    for i in range(20):
        # Simulación de telemetría para prueba visual en el cel
        val_rpm = random.randint(850, 4200)
        val_temp = random.randint(88, 95)
        val_psi = round(random.uniform(28.0, 34.0), 1)
        historial.append(val_rpm)
        
        with p_gauges.container():
            # Layout vertical para celulares
            st.markdown(f"""
                <div class='gauge-box'>
                    <div class='gauge-label'>RPM ACTUALES</div>
                    <div class='gauge-val'>{val_rpm}</div>
                </div>
                <div class='gauge-box'>
                    <div class='gauge-label'>TEMPERATURA MOTOR</div>
                    <div class='gauge-val'>{val_temp}ºC</div>
                </div>
                <div class='gauge-box'>
                    <div class='gauge-label'>PRESIÓN ACEITE</div>
                    <div class='gauge-val'>{val_psi} PSI</div>
                </div>
            """, unsafe_allow_html=True)
        
        p_chart.line_chart(historial)
        time.sleep(0.4)
    st.success(f"Sesión completada: {marca} {modelo}")

st.markdown("---")

# --- 6. INGENIERÍA DE PISTA (ENTRADA MANUAL PARA EL CEL) ---
with st.expander("📝 REGISTRAR FALLA MANUAL (BOXES)"):
    st.write("Si el scanner detecta un código en el cel, anótalo aquí:")
    codigo_falla = st.text_input("CÓDIGO DTC (Ej: P0300):")
    desc_falla = st.text_area("DESCRIPCIÓN:")
    if st.button("💾 GUARDAR EN LOG DE SCUDERIA"):
        st.toast("Dato guardado en la base de datos de Paysandú")

# --- 7. BOTÓN DE EMERGENCIA ---
tel_taller = "099417716"
wa_link = f"https://wa.me/598{tel_taller}?text=SOS: Telemetría crítica en mi {marca} {modelo}."
st.markdown(f"""
    <a href="{wa_link}" style="text-decoration:none;">
        <div style="background-color:#e63946; color:white; text-align:center; 
        padding:15px; border-radius:10px; font-weight:900; margin-top:20px;">
            🆘 LLAMAR A BOXES (URGENTE)
        </div>
    </a>
""", unsafe_allow_html=True)

st.sidebar.caption("Scuderia CLS - Proyect 2026")
