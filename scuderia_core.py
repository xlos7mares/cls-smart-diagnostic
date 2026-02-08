import random

class ScuderiaCLS:
    def __init__(self):
        # Datos simulados de 30 clientes (Uruguay y Argentina)
        self.clientes = [
            {"nombre": "Carlos Pérez", "auto": "VW Gol 2005", "pais": "Uruguay", "ciudad": "Paysandú", "img": "🚗"},
            {"nombre": "Marta Silva", "auto": "Fiat Palio 2010", "pais": "Argentina", "ciudad": "Colón", "img": "🚙"},
            {"nombre": "Jorge Sosa", "auto": "Chevrolet Corsa 2008", "pais": "Uruguay", "ciudad": "Young", "img": "🏎️"},
            # ... (el sistema elegirá uno al azar para la demo)
        ]
        
    def obtener_cliente_random(self):
        return random.choice(self.clientes)

    def motor_diagnostico(self, categoria):
        fallas = {
            "Motor": {"desc": "Falla de Bobina P0301", "precio_uy": 2500, "precio_ar": 45000},
            "Sensores": {"desc": "Sensor Oxígeno P0130", "precio_uy": 3800, "precio_ar": 62000},
            "Electricidad": {"desc": "Alternador bajo voltaje", "precio_uy": 8500, "precio_ar": 120000},
            "Aire": {"desc": "Fuga gas refrigerante", "precio_uy": 4200, "precio_ar": 75000}
        }
        return fallas.get(categoria)

auto_prueba = ScuderiaCLS()
