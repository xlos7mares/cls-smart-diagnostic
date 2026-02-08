import streamlit as st
import scuderia_core
import time

# Configuración de la página
st.set_page_config(page_title="Scuderia CLS - F1 Edition", page_icon="🏎️", layout="wide")

# ESTILO FÓRMULA 1 (CSS Personalizado)
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #e60000; /* Rojo Ferrari */
        color: white;
        border-radius: 5px;
        border: 2px solid #ffffff;
        font-weight: bold;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        border: 2px solid #e60000;
    }
    h1 {
        color: #e60000;
        font-family: 'Arial Black', sans-serif;
        text-transform: uppercase;
        border-bottom: 3px solid #e60000;
    }
    .status-box {
        background-color: #262626;
        padding: 20px;
        border-left: 5px solid #e60000;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado con tu nuevo título
st.title("🏎️ SCUDERIA CLS - TELEMETRY")
st.markdown(f"### **Desarrollador de Software:** Leonardo Olivera")
st.write("**Localización:** Sede Paysandú | **Sistema:** Cloud-Ready 2026")

st.markdown("---")

# Layout de dos columnas para que parezca un tablero de carreras
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="status-box">', unsafe_allow_html=True)
    st.write("### 🛠️ CONTROL DE UNIDAD")
    st.info("Vehículo: **HYUNDAI HB20 (2022)**")
    
    if st.button("🏁 INICIAR ESCANEO MOLECULAR"):
        with st.status("Conectando con ECU...", expanded=True) as status:
            st.write("⚡ Sincronizando sensores CAN-BUS...")
            time.sleep(1)
            st.write("📊 Analizando flujo de datos en la Nube...")
            resultado = scuderia_core.auto_prueba.motor_diagnostico_ia()
            time.sleep(1)
            status.update(label="¡CONEXIÓN EXITOSA!", state="complete", expanded=False)
        
        st.success(f"**DIAGNÓSTICO FINAL:** {resultado}")
        if "SISTEMA ÓPTIMO" in resultado:
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.write("### 📈 RENDIMIENTO EN NUBE")
    # Simulación de métricas de F1
    st.metric(label="Latencia de Respuesta", value="14ms", delta="-2ms")
    st.metric(label="Disponibilidad del Sistema", value="99.9%", delta="Estable")

st.markdown("---")
st.caption("Tecnología de Alto Rendimiento | Agilidad • Escalabilidad • Seguridad")
