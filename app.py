import streamlit as st
import scuderia_core  # Conectamos con el motor que acabamos de actualizar

# Configuración de la pestaña del navegador
st.set_page_config(page_title="Scuderia CLS - Diagnóstico", page_icon="🏎️")

# Encabezado profesional
st.title("🏎️ Scuderia CLS - Panel de Control")
st.markdown(f"**Operador:** Ing. Leonardo Olivera | **Ubicación:** Paysandú")
st.write("---")

# Sección principal
st.subheader("Monitoreo de Telemetría en Tiempo Real")
st.info("Vehículo detectado: **Hyundai HB20 2022**")

# El botón que pediste con el nuevo nombre
if st.button("🚀 Iniciar Escaneo de Sensores"):
    # Usamos un 'status' para que Gustavo vea que el programa está 'pensando'
    with st.status("Conectando con la ECU del vehículo...", expanded=True) as status:
        st.write("Estableciendo conexión vía CAN-BUS...")
        scuderia_core.auto_prueba.simular_telemetria()
        
        st.write("Descargando logs de fallas almacenados...")
        time_sim = 1 # Pequeña pausa estética
        
        st.write("Analizando datos con el motor de IA de Scuderia...")
        # Obtenemos el resultado real del motor
        resultado = scuderia_core.auto_prueba.motor_diagnostico_ia()
        
        # Cambiamos el estado a completado
        status.update(label="¡Escaneo Completado con éxito!", state="complete", expanded=False)
    
    # Mostramos el resultado final de forma destacada
    st.success(f"**Resultado del Análisis:** {resultado}")
    
    # Efecto visual de globos si el sistema está bien (opcional, da un toque de éxito)
    if "ÓPTIMO" in resultado:
        st.balloons()

# Pie de página técnico
st.write("---")
st.caption("Arquitectura basada en Computación en la Nube: Agilidad, Escalabilidad y Disponibilidad.")
