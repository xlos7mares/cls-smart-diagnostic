import streamlit as st
import time

# --- CONFIGURACIÓN ESTÉTICA 2026 ---
st.set_page_config(page_title="CLS Smart Diagnostic Pro", page_icon="🏎️", layout="centered")

# CSS para Interfaz Moderna Gris Oscura (Dark Mode)
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #E0E0E0; }
    [data-testid="stSidebar"] { background-color: #1E1E1E; }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5em; 
        background-color: #2D2D2D; color: #00E676; border: 1px solid #00E676;
    }
    .stExpander { background-color: #1E1E1E; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE SIMULACIÓN (10 EJEMPLOS) ---
ejemplos = [
    {"auto": "Chevrolet Corsa (2008)", "falla": "P0130 - Sensor de Oxígeno", "costo": 3800, "ruta": "Ruta 8, Km 24", "talleres": [("Taller El Rayo", "099 123 456"), ("Mecánica Sur", "098 765 432")]},
    {"auto": "Fiat Uno (2004)", "falla": "P0300 - Fallo de Encendido", "costo": 2500, "ruta": "Ruta 5, Km 102", "talleres": [("Repuestos Carlitos", "091 222 333"), ("Taller Florida", "094 555 666")]},
    {"auto": "VW Gol (2012)", "falla": "P0420 - Catalizador Eficiencia Baja", "costo": 12500, "ruta": "Av. Giannattasio, Km 21", "talleres": [("Escapes Uruguay", "095 888 999"), ("Servicio Costa", "099 000 111")]},
    {"auto": "Renault Clio (2010)", "falla": "P0115 - Sensor Temp. Refrigerante", "costo": 2900, "ruta": "Ruta 1, Km 50", "talleres": [("Mecánica Delta", "097 444 555"), ("Electromóvil", "092 111 222")]},
    {"auto": "Peugeot 206 (2006)", "falla": "P0401 - Flujo EGR Insuficiente", "costo": 5400, "ruta": "Ruta 3, Km 300", "talleres": [("Diesel Paysandú", "093 333 444"), ("Taller Paysandú", "098 121 212")]},
    {"auto": "Suzuki Alto (2015)", "falla": "P0500 - Sensor Velocidad Vehículo", "costo": 4200, "ruta": "Centro, Montevideo", "talleres": [("Taller Central", "099 999 888"), ("Reparaciones 18 de Julio", "094 777 666")]},
    {"auto": "Hyundai Accent (2002)", "falla": "P0101 - Sensor Flujo Aire (MAF)", "costo": 6700, "ruta": "Ruta 9, Km 140", "talleres": [("Mecánica Maldonado", "091 000 999"), ("San Carlos Motor", "096 555 444")]},
    {"auto": "Toyota Corolla (1998)", "falla": "P0171 - Mezcla muy pobre", "costo": 3100, "ruta": "Ruta 2, Km 280", "talleres": [("Fray Bentos Auto", "092 333 222"), ("Repuestos Mercedes", "095 111 000")]},
    {"auto": "Ford Fiesta (2011)", "falla": "P0204 - Inyector Cilindro 4", "costo": 8900, "ruta": "Ruta Interbalnearia, Km 45", "talleres": [("Atlántida Motores", "097 999 000"), ("Inyección del Este", "099 777 888")]},
    {"auto": "Citroen C3 (2007)", "falla": "P0562 - Voltaje Sistema Bajo", "costo": 4500, "ruta": "Ruta 26, Km 10", "talleres": [("Baterías Melo", "098 555 111"), ("Electrónica Melo", "091 222 444")]}
]

# --- LÓGICA DE INTERFAZ ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2343/2343750.png", width=100)
    st.title("Gobernanza")
    st.success("👤 Sesión: Gustavo Diaz")
    st.info("Estado: Administrador Global")
    
    st.write("---")
    index = st.slider("Cambiar de Caso (Ejemplo)", 0, 9, 0)
    caso = ejemplos[index]
    st.write("Caso actual: ", index + 1)

# --- CUERPO PRINCIPAL ---
st.title("🏎️ CLS Diagnostic Pro")
st.write(f"📍 **Ubicación actual detectada:** {caso['ruta']}")

st.write("---")
if st.button("🧬 REALIZAR ESCANEO MOLECULAR"):
    with st.spinner("Conectando con Servidores Cloud..."):
        time.sleep(1.5)
        st.error(f"⚠️ {caso['falla']}")
        st.subheader(f"Vehículo: {caso['auto']}")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Presupuesto Estimado", f"${caso['costo']} UYU")
        st.write("**Impacto:** Pérdida de potencia y seguridad.")
    
    with col2:
        st.write("### 🏥 Talleres Afiliados Cercanos")
        for t in caso['talleres']:
            st.write(f"✅ **{t[0]}**")
            st.caption(f"📞 {t[1]} | [Llamar Ahora]")

    st.write("---")
    st.link_button("🚀 ENVIAR REPORTE A GUSTAVO", f"https://wa.me/59899417716?text=Reporte CLS: {caso['falla']} en {caso['auto']}", type="primary")

st.write("---")
st.caption("Tecnología de Grado Coursera: Escalabilidad, Agilidad y Disponibilidad 24/7.")
