import streamlit as st
import time

# --- CONFIGURACIÓN ESTÉTICA SCUDERIA ---
st.set_page_config(page_title="CLS Diagnostic - Scuderia Edition", page_icon="🏎️")

# Estilo Ferrari: Fondo Negro, Botones Rojos, Detalles Amarillos
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #1a1a1a; border-right: 2px solid #FFEB00; }
    .stButton>button { 
        width: 100%; border-radius: 5px; height: 3.5em; 
        background-color: #FF2800; color: white; border: 2px solid #FFEB00;
        font-weight: bold; font-size: 18px;
    }
    h1, h2, h3 { color: #FFEB00; font-family: 'Arial Black'; }
    .stMetric { background-color: #1a1a1a; padding: 10px; border-radius: 10px; border-left: 5px solid #FF2800; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE SIMULACIÓN ---
ejemplos = [
    {"auto": "Chevrolet Corsa (2008)", "falla": "P0130 - Sensor de Oxígeno", "costo": 3800, "ruta": "Ruta 8, Km 24", "talleres": [("Taller Gustavo Diaz", "099 417 716")]},
    {"auto": "Peugeot 206 (2006)", "falla": "P0401 - Flujo EGR Insuficiente", "costo": 5400, "ruta": "Ruta 3, Km 300", "talleres": [("Taller Gustavo Diaz", "099 417 716")]},
    {"auto": "Ford Fiesta (2011)", "falla": "P0204 - Inyector Cilindro 4", "costo": 8900, "ruta": "Ruta Interbalnearia, Km 45", "talleres": [("Taller Gustavo Diaz", "099 417 716")]}
]

# --- SIDEBAR PROFESIONAL ---
with st.sidebar:
    st.markdown("# 🏁 SCUDERIA CLS")
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/36/Scuderia_Ferrari_logo.svg/1200px-Scuderia_Ferrari_logo.svg.png", width=150)
    st.write("---")
    st.write("👨‍💻 **Gestor de Flota:**")
    st.success("Gustavo Diaz")
    index = st.slider("Seleccionar Vehículo", 0, 2, 0)
    caso = ejemplos[index]

# --- CUERPO PRINCIPAL ---
st.title("🏎️ CLS SMART DIAGNOSTIC")
st.write(f"📍 **Geolocalización:** {caso['ruta']}")

if st.button("🏁 INICIAR TEST DE POTENCIA Y MOTOR"):
    with st.spinner("Conectando con la ECU..."):
        time.sleep(1.5)
        st.error(f"❌ FALLA DETECTADA: {caso['falla']}")
        
    col1, col2 = st.columns(2)
    with col1:
        st.metric("COSTO REPARACIÓN", f"${caso['costo']} UYU")
    with col2:
        st.write("### 🛠️ Taller Oficial")
        st.write(f"✅ {caso['talleres'][0][0]}")
        st.write(f"📞 {caso['talleres'][0][1]}")

    st.write("---")
    # El reporte va dirigido al CLIENTE para que él tenga la info y venga al taller
    mensaje_cliente = f"Resumen CLS para su {caso['auto']}: Se detectó error {caso['falla']}. Presupuesto en Taller Gustavo Diaz: ${caso['costo']} UYU. ¡Lo esperamos!"
    
    st.link_button("📩 ENVIAR DIAGNÓSTICO AL CLIENTE", f"https://wa.me/?text={mensaje_cliente}", type="primary")

st.write("---")
st.caption("Arquitectura Masiva: Agilidad, Costo, Escalabilidad y Rendimiento.")
