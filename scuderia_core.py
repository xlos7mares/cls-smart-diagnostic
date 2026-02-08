import random

class ScuderiaCLS:
    def __init__(self):
        self.protocolo = "OBD-II Universal"

    def motor_diagnostico(self, categoria):
        # Diccionario de fallas reales para autos gama media (VW, Fiat, Chevrolet)
        base_datos = {
            "Motor": [
                "✅ (P0000) Combustión estable. Sin fallos de inyección.",
                "⚠️ (P0300) Fallo de encendido detectado. Revisar bujías/cables.",
                "⚠️ (P0171) Mezcla pobre. Posible entrada de aire o filtro sucio."
            ],
            "Sensores": [
                "✅ Sensores de oxígeno y flujo de aire en rango operativo.",
                "⚠️ (P0130) Sensor de Oxígeno con baja señal. Revisar cableado.",
                "⚠️ (P0101) Sensor MAF fuera de rango. Limpieza recomendada."
            ],
            "Electricidad": [
                "✅ Alternador cargando correctamente (14.2V).",
                "⚠️ (P0562) Voltaje de sistema bajo. Revisar batería/alternador.",
                "✅ Sistema de encendido y relés sin anomalías."
            ],
            "Aire": [
                "✅ Presión de gas refrigerante en nivel óptimo.",
                "⚠️ Presión de carga baja. Se recomienda control de fugas.",
                "✅ Ventilador de condensador operando correctamente."
            ]
        }
        return random.choice(base_datos.get(categoria, ["Escaneo completado"]))

auto_prueba = ScuderiaCLS()
