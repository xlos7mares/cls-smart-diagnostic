import random
import time

class ScuderiaCLS:
    def __init__(self):
        self.vehiculo = "Hyundai HB20 2022"
    
    def simular_telemetria(self):
        """Simula la conexión y captura de datos de la ECU"""
        # Esto hace que el programa 'espere' y parezca que está trabajando
        time.sleep(1)
        return True

    def motor_diagnostico_ia(self):
        """Genera un diagnóstico aleatorio para mostrar dinamismo"""
        diagnosticos = [
            "✅ SISTEMA ÓPTIMO: Todos los parámetros de la ECU están en rango normal.",
            "⚠️ ALERTA: Desgaste detectado en Inyectores. Se sugiere limpieza preventiva.",
            "✅ RENDIMIENTO: Mezcla de combustible optimizada para ahorro de consumo.",
            "⚠️ AVISO: Sensor de oxígeno con lectura intermitente. Revisar cableado.",
            "✅ ESTADO: Presión de aceite y temperatura de motor estables."
        ]
        # Elige uno al azar de la lista anterior
        return random.choice(diagnosticos)

# Creamos la instancia para que app.py la pueda usar
auto_prueba = ScuderiaCLS()
