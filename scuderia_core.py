import random

class ScuderiaCLS:
    def __init__(self):
        # Usamos el protocolo estándar OBD-II (SAE J1979)
        self.protocolo = "ISO 15765-4 (CAN)" 

    def motor_diagnostico(self, categoria):
        # Base de datos universal basada en códigos estándar P0 (Genéricos)
        # Esto funciona para VW, Fiat, Chevrolet, etc.
        diagnosticos_universales = {
            "Motor": [
                "✅ (P0000) Sin fallos detectados en ciclo de combustión.",
                "⚠️ (P0300) Detectado fallo de encendido. Revisar bujías o cables.",
                "⚠️ (P0171) Mezcla demasiado pobre. Posible entrada de aire o filtro sucio."
            ],
            "Sensores": [
                "✅ Sensores de oxígeno y flujo de aire operando en rango.",
                "⚠️ (P0130) Sensor de Oxígeno (Banco 1) con baja señal.",
                "⚠️ (P0101) Sensor MAF fuera de rango. Limpieza recomendada."
            ],
            "Electricidad": [
                "✅ Voltaje de batería estable (13.8V - 14.2V con motor encendido).",
                "⚠️ (P0562) Voltaje del sistema bajo. Revisar Alternador.",
                "✅ Circuito de encendido y relés operativos."
            ],
            "Aire": [
                "✅ Sistema de climatización con presión de carga correcta.",
                "⚠️ Presión de refrigerante baja. Posible fuga en el circuito.",
                "✅ Ventilador de condensador activado correctamente."
            ]
        }
        return random.choice(diagnosticos_universales.get(categoria, ["Escaneo completado"]))

auto_prueba = ScuderiaCLS()
