import random

class ScuderiaCLS:
    def __init__(self):
        self.base_clientes = []
        marcas = ["VW Gol", "Fiat Palio", "Chevrolet Corsa", "Renault Clio", "Ford Ka"]
        tipos_motor = ["Inyección Electrónica", "Carburador"]
        
        # Generamos los 30 ejemplos con diversidad técnica
        for i in range(1, 31):
            pais = random.choice(["Uruguay", "Argentina", "Chile"])
            motor = random.choice(tipos_motor)
            self.base_clientes.append({
                "id": i,
                "nombre": f"Cliente Demo {i}",
                "auto": f"{random.choice(marcas)} ({motor})",
                "motor_tipo": motor,
                "pais": pais,
                "ciudad": f"Zona {random.randint(1,9)}, Km {random.randint(10, 400)}",
                "lat": -32.0 + random.uniform(-2, 2),
                "lon": -58.0 + random.uniform(-2, 2) if pais != "Chile" else -70.0 + random.uniform(-1, 1),
            })

    def obtener_cliente(self, indice):
        return self.base_clientes[indice % len(self.base_clientes)]

    def generar_escaneo_completo(self, motor_tipo):
        # Lógica de fallas aleatorias por sistema
        sistemas = {
            "Aire Acondicionado": [
                "✅ Presión de gas óptima. Enfriamiento a 5°C.",
                "⚠️ FALLA: Presión baja. Posible fuga en condensador. Repuesto: Filtro deshidratador.",
                "❌ FALLA: Compresor no acopla. Revisar embrague electromagnético."
            ],
            "Luces y Visibilidad": [
                "✅ Todas las luminarias operativas.",
                "⚠️ AVISO: Lámpara H4 izquierda quemada.",
                "❌ FALLA: Motor de limpiaparabrisas sin retorno. Revisar temporizador."
            ],
            "Electricidad": [
                "✅ Alternador cargando a 14.2V. Batería OK.",
                "⚠️ ALERTA: Batería con celdas agotadas (11.5V). Cambio recomendado.",
                "⚠️ FALLA: Regulador de voltaje del alternador inestable."
            ],
            "Motor/Inyección": [
                "✅ Sincronización de encendido correcta.",
                "⚠️ (Inyección) Limpieza de inyectores necesaria por obstrucción.",
                "⚠️ (Carburador) Flotador trabado o chicler de baja tapado.",
                "❌ FALLA: Sensor de posición de cigüeñal (CKP) intermitente."
            ]
        }
        
        reporte = {}
        for sistema, opciones in sistemas.items():
            # Filtramos según el tipo de motor
            opcion = random.choice(opciones)
            if "Inyección" in motor_tipo and "Carburador" in opcion: continue
            if "Carburador" in motor_tipo and "Inyección" in opcion: continue
            reporte[sistema] = opcion
            
        return reporte

    def obtener_precios_repuesto(self, falla, pais):
        moneda = "UYU" if pais == "Uruguay" else "ARS" if pais == "Argentina" else "CLP"
        return [
            {"casa": "Repuestos 'La Tuerca'", "precio": random.randint(1200, 4000), "moneda": moneda, "orig": "Brasil"},
            {"casa": "Global Parts", "precio": random.randint(900, 3500), "moneda": moneda, "orig": "China"},
            {"casa": "Centro Repuesto", "precio": random.randint(2000, 6000), "moneda": moneda, "orig": "Original"}
        ]

auto_prueba = ScuderiaCLS()
