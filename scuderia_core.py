import random
import time

class ScuderiaCLS:
    def __init__(self, vin):
        self.vin = vin
        self.status = "Conectado"
        self.sensores = {
            "RPM": 0,
            "Temp_Motor": 90,
            "Presion_Aceite": 40,
            "Consumo_L/km": 8.5
        }

    def simular_telemetria(self):
        """Simula datos en tiempo real fluyendo desde el chip a la nube."""
        print(f"--- Escaneando Vehículo VIN: {self.vin} ---")
        for _ in range(5):
            self.sensores["RPM"] = random.randint(800, 3500)
            self.sensores["Temp_Motor"] += random.uniform(-1, 2)
            print(f"Capturando datos... [RPM: {self.sensores['RPM']} | Temp: {self.sensores['Temp_Motor']:.2f}°C]")
            time.sleep(1)

    def motor_diagnostico_ia(self):
        """Algoritmo predictivo de fallas (Lo que le dará valor al proyecto)."""
        print("\n[IA] Analizando patrones de desgaste...")
        # Simulación de detección de falla
        probabilidad_falla = random.random()
        
        if probabilidad_falla > 0.8:
            return "ALERTA: Desgaste detectado en Inyectores. Sugerencia: Limpieza preventiva."
        else:
            return "SISTEMA ÓPTIMO: No se requieren reparaciones inmediatas."

# Ejecución de prueba para mostrarle a Gustavo
auto_prueba = ScuderiaCLS("HYUNDAI-HB20-2022")
auto_prueba.simular_telemetria()
resultado = auto_prueba.motor_diagnostico_ia()
print(f"\nREPORTE FINAL: {resultado}")
