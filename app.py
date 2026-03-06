import streamlit as st
import pandas as pd
import urllib.parse
from geopy.geocoders import Nominatim

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro Aliados CLS", page_icon="🚛", layout="centered")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .contrato-box {
        background-color: #f8f9fa;
        padding: 15px;
        border: 1px solid #d1d5db;
        border-radius: 10px;
        height: 200px;
        overflow-y: scroll;
        margin-bottom: 20px;
        font-size: 14px;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-weight: bold;
        background-color: #01579b;
        color: white;
        border-radius: 10px;
    }
    .btn-wa {
        display: block;
        width: 100%;
        padding: 20px;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        text-decoration: none;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚛 Registro de Fleteros")
st.markdown("### CONEXIÓN LOGÍSTICA SUR")

# --- 1. CONTRATO ---
st.subheader("Contrato de Adhesión")
st.markdown("""
<div class="contrato-box">
<b>CONTRATO DE ADHESIÓN Y DESLINDE DE RESPONSABILIDAD - CLS</b><br><br>
1. <b>Intermediación:</b> CLS actúa únicamente como nexo comercial. No existe relación de dependencia.<br><br>
2. <b>Responsabilidad:</b> El Fletero es el único responsable por la carga y cualquier daño o siniestro. CLS queda libre de toda responsabilidad.<br><br>
3. <b>Comisión:</b> El Fletero acepta abonar el 15% del valor de cada flete gestionado.<br><br>
4. <b>Documentación:</b> Declara tener vehículo, seguros y documentación personal al día según las leyes de Uruguay.<br><br>
5. <b>Seguridad:</b> La unidad debe estar en óptimas condiciones mecánicas.
</div>
""", unsafe_allow_html=True)

# --- 2. FORMULARIO ---
with st.form("registro_form"):
    acepto = st.checkbox("HE LEÍDO Y ACEPTO LOS TÉRMINOS DEL CONTRATO")
    
    st.markdown("---")
    nombre = st.text_input("Nombre y Apellido completo:")
    celular = st.text_input("Número de celular:")
    ciudad = st.text_input("Ciudad y Departamento:", "Paysandú, Uruguay")
    domicilio = st.text_input("Domicilio y Nro de Casa:")
    
    # --- MAPA DINÁMICO ---
    st.write("📍 **Verificación de Ubicación en Mapa**")
    if domicilio:
        try:
            geolocator = Nominatim(user_agent="cls_app_2026")
            direccion_completa = f"{domicilio}, {ciudad}"
            location = geolocator.geocode(direccion_completa)
            
            if location:
                df_mapa = pd.DataFrame({'lat': [location.latitude], 'lon': [location.longitude]})
                st.map(df_mapa)
                st.caption(f"Ubicación detectada: {location.address}")
            else:
                st.warning("No se encontró la dirección exacta. Se muestra mapa general.")
                st.map(pd.DataFrame({'lat': [-32.31], 'lon': [-58.08]}))
        except:
            st.error("Error al cargar el mapa dinámico.")
    
    st.markdown("---")
    st.subheader("Adjuntar Documentación (Fotos)")
    f_ci = st.file_uploader("Foto de Cédula", type=['jpg','png','jpeg'])
    f_lic = st.file_uploader("Foto de Licencia de Conducir", type=['jpg','png','jpeg'])
    f_lib = st.file_uploader("Foto de Libreta de Propiedad", type=['jpg','png','jpeg'])
    f_seg = st.file_uploader("Foto de Póliza de Seguro", type=['jpg','png','jpeg'])
    f_veh = st.file_uploader("Foto del Vehículo", type=['jpg','png','jpeg'])
    
    enviar = st.form_submit_button("✅ GUARDAR Y GENERAR FICHA")

# --- 3. LÓGICA DE ENVÍO ---
if enviar:
    if acepto and nombre and domicilio:
        st.balloons()
        
        # Mensaje para WhatsApp
        resumen = (
            f"🚀 *NUEVO FLETERO REGISTRADO*\n\n"
            f"👤 *Nombre:* {nombre}\n"
            f"📱 *Celular:* {celular}\n"
            f"📍 *Ciudad:* {ciudad}\n"
            f"🏠 *Domicilio:* {domicilio}\n\n"
            f"✅ El fletero ha aceptado el contrato y cargado los archivos."
        )
        
        url_wa = f"https://wa.me/59899417716?text={urllib.parse.quote(resumen)}"
        
        st.success("¡Registro procesado correctamente!")
        st.markdown(f"""
            <div style="background-color: #f1f8e9; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #2e7d32;">
                <h3>¡FICHA LISTA!</h3>
                <p>Tocá el botón para avisar a Leonardo por WhatsApp:</p>
                <a href="{url_wa}" target="_blank" class="btn-wa">
                    📲 ENVIAR REGISTRO POR WHATSAPP
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Por favor, acepta el contrato y completa los campos obligatorios (Nombre y Domicilio).")

st.sidebar.caption("CLS - Conexión Logística Sur 2026")
