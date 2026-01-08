import streamlit as st
import time

# --- CONFIGURACIÓN DE LA PLATAFORMA ---
st.set_page_config(page_title="CLS Smart Diagnostic", page_icon="🚗", layout="centered")

# Título profesional
st.title("🚗 CLS Smart Diagnostic")
st.subheader("Plataforma de Monitoreo Masivo 2026")

# --- SIMULACIÓN DE HARDWARE ---
with st.sidebar:
    st.header("🌐 Estado del Sistema")
    st.success("📡 Chip Bluetooth CLS: Conectado")
    st.info("Vehículo: Chevrolet Corsa (2008)")
    st.write("---")
    st.write("Usuario: **Prueba Piloto Yanina**")

# --- INTERFAZ DE USUARIO ---
st.write("### 1. Análisis del Vehículo")
if st.button("🚀 INICIAR ESCANEO COMPLETO"):
    bar = st.progress(0)
    status_text = st.empty()
    
    # Simulación de las 3 partes del software que mencionamos
    status_text.text("Conectando con la ECU del auto (App Base)...")
    time.sleep(1)
    bar.progress(33)
    
    status_text.text("Enviando códigos a la Nube (Servidor de Diagnóstico)...")
    time.sleep(1)
    bar.progress(66)
    
    status_text.text("Consultando soluciones técnicas (Base de Datos)...")
    time.sleep(1)
    bar.progress(100)
    
    st.error("⚠️ ALERTA: Falla detectada en el motor")
    
    # RESULTADOS
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Código OBD2", value="P0130")
        st.write("**Falla:** Sensor de Oxígeno (Sonda Lambda)")
    with col2:
        st.write("**Gravedad:** Media")
        st.write("**Efecto:** Consumo excesivo de nafta y humo negro.")

    st.write("---")
    st.write("### 🛠️ Solución en Taller CLS")
    st.info("Repuesto sugerido: Sensor Bosch + Limpieza de contactos.")
    st.write("Precio aproximado: **$3.800 UYU**")
    
    # Botón de Monetización
    st.link_button("📅 AGENDAR TURNO POR WHATSAPP", "https://wa.me/59899417716?text=Mi auto Yanina dio error P0130. Necesito turno.")

st.write("---")
st.caption("Arquitectura diseñada para Escalabilidad de hasta 5M de vehículos.")
