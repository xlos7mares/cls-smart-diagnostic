import random

class ScuderiaCLS:
    def __init__(self):
        # Base de datos de 30 clientes reales (Uruguay, Argentina, Chile)
        self.base_clientes = [
            {"id": 1, "nombre": "Juan Rodríguez", "auto": "VW Gol 1.6", "pais": "Uruguay", "ciudad": "Paysandú, Ruta 3 Km 370", "lat": -32.31, "lon": -58.08, "repuesto": "Bomba de Agua"},
            {"id": 2, "nombre": "Matías Gauto", "auto": "Fiat Palio", "pais": "Argentina", "ciudad": "Colón, Calle 12", "lat": -32.22, "lon": -58.14, "repuesto": "Bujías Bosch"},
            {"id": 3, "nombre": "Diego Retamales", "auto": "Chevrolet Corsa", "pais": "Chile", "ciudad": "Santiago, Av. Providencia", "lat": -33.44, "lon": -70.66, "repuesto": "Sensor MAF"},
            {"id": 4, "nombre": "Ana Clara Sosa", "auto": "Peugeot 206", "pais": "Uruguay", "ciudad": "Salto, Costanera Norte", "lat": -31.38, "lon": -57.96, "repuesto": "Bobina de Ignición"},
            # ... (Simularemos la rotación de los 30 en la App)
        ]
        # Generar el resto hasta 30 automáticamente para la demo
        for i in range(5, 31):
            pais = random.choice(["Uruguay", "Argentina", "Chile"])
            self.base_clientes.append({
                "id": i,
                "nombre": f"Cliente Demo {i}",
                "auto": random.choice(["Fiat Uno", "VW Suran", "Toyota Yaris"]),
                "pais": pais,
                "ciudad": f"Zona Rural {pais}, Km {random.randint(10, 500)}",
                "lat": -32.0 + random.uniform(-2, 2),
                "lon": -58.0 + random.uniform(-2, 2) if pais != "Chile" else -70.0 + random.uniform(-1, 1),
                "repuesto": "Filtro de Aceite"
            })

    def obtener_cliente(self, indice):
        return self.base_clientes[indice % len(self.base_clientes)]

    def obtener_casas_repuestos(self, repuesto, pais):
        moneda = "UYU" if pais == "Uruguay" else "ARS" if pais == "Argentina" else "CLP"
        return [
            {"local": "Repuestos 'El Rayo'", "precio": random.randint(1500, 5000), "moneda": moneda, "origen": "Brasil (Original)"},
            {"local": "Euro-Partes", "precio": random.randint(1200, 4500), "moneda": moneda, "origen": "Alemania (Alternativo)"},
            {"local": "Amazon Global", "precio": random.randint(20, 100), "moneda": "USD", "origen": "China (Genérico)"}
        ]

auto_prueba = ScuderiaCLS()
