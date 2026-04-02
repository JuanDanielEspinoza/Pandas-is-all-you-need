import pandas as pd
import numpy as np

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Tamaño del dataset
n = 1000

# 1. ID Paciente
id_paciente = [f"PAC-{i:04d}" for i in range(1, n + 1)]

# 2. Asimetría Izquierda (Edad)
# Usamos una distribución Beta para cargar los datos hacia la derecha (valores altos)
edad = np.random.beta(a=8, b=2, size=n) * 60 + 20 
edad = np.round(edad).astype(int)

# 3. Asimetría Derecha (Nivel Triglicéridos)
# Usamos una distribución exponencial para cargar datos a la izquierda con cola a la derecha
trigliceridos = np.random.exponential(scale=80, size=n) + 90
trigliceridos = np.round(trigliceridos, 1)

# 4. Platicúrtica (Nivel Vitamina D)
# Usamos una distribución uniforme (sin pico central, muy plana)
vitamina_d = np.random.uniform(low=10, high=80, size=n)
vitamina_d = np.round(vitamina_d, 1)

# 5. Correlaciones
# Positiva: Peso vs Colesterol
peso = np.random.normal(loc=75, scale=15, size=n)
ruido_pos = np.random.normal(loc=0, scale=15, size=n)
# Ecuación lineal simple para forzar correlación positiva
colesterol = 120 + (1.5 * peso) + ruido_pos 

# Negativa: Horas de actividad vs IMC
horas_actividad = np.random.uniform(low=0, high=10, size=n)
ruido_neg = np.random.normal(loc=0, scale=2, size=n)
# Ecuación lineal inversa para forzar correlación negativa
imc = 35 - (1.2 * horas_actividad) + ruido_neg 

# 6. Problema de Tipo de Dato (Frecuencia Cardíaca en String)
fc_numerica = np.random.normal(loc=75, scale=12, size=n).astype(int)
frecuencia_cardiaca = []
for fc in fc_numerica:
    # Introducimos el problema: 10% de los datos tendrán texto y todos son strings
    if np.random.rand() < 0.10:
        frecuencia_cardiaca.append(f"{fc} bpm")
    else:
        frecuencia_cardiaca.append(str(fc))

# 7. Anomalías de Sensores (Presión Arterial)
presion_arterial = np.random.normal(loc=120, scale=15, size=n)
# Introducimos fallos de sensores en índices aleatorios
indices_anomalos = np.random.choice(n, size=25, replace=False)
for idx in indices_anomalos:
    if np.random.rand() > 0.5:
        presion_arterial[idx] = 999.0 # Saturación del sensor
    else:
        presion_arterial[idx] = -45.0 # Error de calibración/desconexión

# Ensamblar el DataFrame
df_clinico = pd.DataFrame({
    'ID_Paciente': id_paciente,
    'Edad': edad,
    'Frecuencia_Cardiaca': frecuencia_cardiaca,
    'Presion_Arterial_Sistolica': np.round(presion_arterial, 1),
    'Nivel_Trigliceridos': trigliceridos,
    'Nivel_Vitamina_D': vitamina_d,
    'Horas_Actividad_Semana': np.round(horas_actividad, 1),
    'Peso_kg': np.round(peso, 1),
    'IMC': np.round(imc, 1),
    'Colesterol_Total': np.round(colesterol, 1)
})

# Guardar a CSV
df_clinico.to_csv('dataset_clinico_taller.csv', index=False)

print("Dataset 'dataset_clinico_taller.csv' generado con éxito con 1000 registros.")