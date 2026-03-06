# --- SECCIÓN DE MAPA CON SEGURIDAD ---
st.subheader("📍 Tu Ubicación y Talleres Cercanos")
direccion = st.text_input("Dirección actual (o dejar vacío para GPS):", "Paysandú, Uruguay")

try:
    # Agregamos un tiempo de espera (timeout) más largo para evitar el error de "Unavailable"
    geolocator = Nominatim(user_agent="scuderia_cls_v1", timeout=10)
    location = geolocator.geocode(direccion)

    if location:
        # Si encuentra la dirección, muestra el punto exacto
        puntos = [{"lat": location.latitude, "lon": location.longitude, "nombre": "Tu Ubicación"}]
        # Sumamos los talleres que ya definimos arriba
        for t in talleres:
            puntos.append(t)
        
        st.map(pd.DataFrame(puntos))
        st.caption(f"📍 Confirmado: {location.address}")
    else:
        # Plan B: Si no encuentra la calle exacta, muestra Paysandú por defecto
        st.warning("No pudimos precisar la dirección exacta. Mostrando mapa general.")
        st.map(pd.DataFrame([{"lat": -32.31, "lon": -58.08}]))

except Exception as e:
    # Manejo de error para que la app no se ponga roja
    st.info("ℹ️ El servicio de mapas está procesando datos. Mostrando ubicación predeterminada.")
    st.map(pd.DataFrame([{"lat": -32.31, "lon": -58.08}]))
