import streamlit as st
import pandas as pd
import urllib.parse
import time
import obd  # LIBRERÍA PARA LA CONEXIÓN REAL

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Scuderia CLS REAL", page_icon="🏎️", layout="centered")

# --- 2. ESTILOS F1 NEÓN ---
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
        border: 2px solid #e63946; text-align: center; margin-bottom: 15px;
    }
    .gauge-val { font-family: 'Exo 2', sans-serif; font-size: 1.8rem; color: #00f2ff; }
    .stButton>button {
        width: 100%; height: 80px; font-weight: 900; font-size: 1.4rem;
        background-color: #1d3557; color: white; border: 2px solid #e63946; border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='f1-neon'>🏎️ SCUDERIA CLS</h1>", unsafe_allow_html=True)

# --- 3. SELECCIÓN DE UNIDAD ---
marca = "Hyundai"
modelo = "HB20"
st.write(f"🔍 **Unidad detectada:** {marca} {modelo}")

st.markdown("---")

# --- 4. ESCANEO REAL ---
if st.button("🚀 INICIAR ESCANEO REAL"):
    p_gauge = st.empty()
    
    with st.status("Estableciendo enlace con V-LINK...", expanded=True) as status:
        try:
            # INTENTO DE CONEXIÓN REAL POR BLUETOOTH
            connection = obd.OBD() 
            
            if connection.is_connected():
                st.write("✅ Enlace establecido con la ECU.")
                
                # Leemos los datos reales del motor
                r_rpm = connection.query(obd.commands.RPM)
                r_temp = connection.query(obd.commands.COOLANT_TEMP)
                r_fallas = connection.query(obd.commands.GET_DTC)

                val_rpm = int(r_rpm.value.magnitude) if not r_rpm.is_null() else 0
                val_temp = int(r_temp.value.magnitude) if not r_temp.is_null() else 0
                
                p_gauge.markdown(f"""
                    <div class='gauge-box'>
                        <div style='color:#a8dadc; font-size:0.7rem;'>TELEMETRÍA REAL</div>
                        <div class='gauge-val'>{val_rpm} RPM | {val_temp}ºC</div>
                    </div>
                """, unsafe_allow_html=True)
                
                status.update(label="Escaneo Finalizado", state="complete")
                
                if r_fallas.value:
                    st.error(f"🚨 FALLAS DETECTADAS: {r_fallas.value}")
                else:
                    st.success("✅ SISTEMA ÓPTIMO: No hay fallas en la ECU.")
            else:
                st.error("❌ NO CONECTADO: El chip no responde. ¿Está el Bluetooth vinculado?")
                
        except Exception as e:
            st.warning("⚠️ Error de Hardware: Asegúrate de que el Vgate iCar2 esté prendido.")

# --- 5. REPORTE WHATSAPP ---
st.markdown("---")
nombre_cliente = st.text_input("Nombre del Cliente:", "Usuario HB20")
wa_url = f"https://wa.me/59899417716?text=Reporte CLS: {marca} {modelo} analizado."
st.markdown(f'<a href="{wa_url}" target="_blank"><button style="width:100%; background-color:#25d366; color:white; border:none; padding:15px; border-radius:10px; font-weight:bold;">📲 ENVIAR REPORTE</button></a>', unsafe_allow_html=True)
