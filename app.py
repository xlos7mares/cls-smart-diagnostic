import streamlit as st
import scuderia_core
import time
import pandas as pd

# Estética Senna: Amarillo (#FDB927), Verde (#009B3A), Azul (#002776)
st.set_page_config(page_title="Scuderia CLS - Senna Edition", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stButton>button { 
        background-color: #FDB927; color: #002776; 
        border: 2px solid #009B3A; font-weight: bold; border-radius: 15px;
    }
    .metalic-card {
        background: linear-gradient(145deg, #1a1a1a, #262626);
        border: 1px solid #FDB927; padding: 20px; border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Selección de Usuario (Simulando el inicio de sesión)
user = scuderia_core.auto_prueba.obtener_cliente_random()

st.title("🏎️ SCUDERIA CLS - DASHBOARD")
st.markdown(f"**Desarrollador:** Leonardo Olivera | **Sede:** Paysandú")

col_info, col_map = st.columns([1, 1.5])

with col_info:
    st.markdown('<div class="metalic-card">', unsafe_allow_html=True)
    st.header("👤 DATOS DEL CLIENTE")
    st.write(f"**Nombre:** {user['nombre']}")
    st.write(f"**Vehículo:** {user['auto']} {user['img']}")
    st.write(f"**Ubicación:** {user['ciudad']}, {user['pais']}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("### 🛠️ ELEGIR ESCANEO")
    opcion = st.selectbox("Seleccione sistema:", ["Motor", "Sensores", "Electricidad", "Aire"])
    
    if st.button("🏁 INICIAR ESCANEO PROFESIONAL"):
        with st.spinner("Procesando telemetría..."):
            time.sleep(2)
            res = scuderia_core.auto_prueba.motor_diagnostico(opcion)
            st.warning(f"RESULTADO: {res['desc']}")
            
            # Precios dinámicos
            st.write("### 🛒 COSTO ESTIMADO REPUESTO:")
            st.write(f"🇺🇾 Uruguay: **${res['precio_uy']} UYU**")
            st.write(f"🇦🇷 Argentina: **${res['precio_ar']} ARS**")
            st.markdown(f"[Ver repuesto en Mercado Libre](https://www.mercadolibre.com.uy/s/{opcion})")
            
            st.button("📄 ENVIAR REPORTE PDF AL CELULAR (WhatsApp)")

with col_map:
    st.write("### 📍 UBICACIÓN Y TALLERES AFILIADOS")
    # Mapa centrado en la zona (simulado)
    map_data = pd.DataFrame({'lat': [-32.32], 'lon': [-58.08]})
    st.map(map_data)
    
    st.markdown('<div style="border: 2px solid #e60000; padding:10px; border-radius:10px;">', unsafe_allow_html=True)
    st.error("🆘 TALLERES AFILIADOS DE EMERGENCIA")
    st.write("📞 **Taller 'El Flaco' (Paysandú):** 099 123 456")
    st.write("📞 **Electromecánica 'Centro' (Young):** 098 765 432")
    st.write("📞 **Servicio 'Sur' (Colón, AR):** +54 3447 112233")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption("Sistema Scuderia CLS - Agilidad, Seguridad y Disponibilidad en la Nube.")
