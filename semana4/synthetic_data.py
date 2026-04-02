import pandas as pd
import numpy as np

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Tamaño del dataset
n = 1000

# --- FASE 1: DATOS PERSONALES (PII) ---
nombres_base = ["Carlos", "Maria", "Juan", "Ana", "Luis", "Laura", "Pedro", "Sofia", "Diego", "Valentina"]
apellidos_base = ["Gomez", "Perez", "Rodriguez", "Martinez", "Lopez", "Garcia", "Hernandez", "Ruiz", "Diaz", "Florez"]

nombre_paciente = [f"{np.random.choice(nombres_base)} {np.random.choice(apellidos_base)}" for _ in range(n)]
documento_identidad = [f"{np.random.randint(10000000, 99999999)}" for _ in range(n)]

# --- FASE 2: VARIABLES ESTADÍSTICAS ---
# Asimetría Izquierda (Edad)
edad = np.random.beta(a=8, b=2, size=n) * 60 + 20 
edad = np.round(edad).astype(int)

# Asimetría Derecha (Triglicéridos)
trigliceridos = np.random.exponential(scale=80, size=n) + 90
trigliceridos = np.round(trigliceridos, 1)

# Platicúrtica - Plana (Nivel Vitamina D)
vitamina_d = np.random.uniform(low=10, high=80, size=n)
vitamina_d = np.round(vitamina_d, 1)

# Leptocúrtica - Pico agudo y colas pesadas (Glucosa)
# Usamos distribución de Laplace para simular fuerte concentración en 95 y valores atípicos
glucosa = np.random.laplace(loc=95, scale=5, size=n)
glucosa = np.round(glucosa, 1)

# Correlaciones (Peso vs Colesterol y Actividad vs IMC)
peso = np.random.normal(loc=75, scale=15, size=n)
ruido_pos = np.random.normal(loc=0, scale=15, size=n)
colesterol = 120 + (1.5 * peso) + ruido_pos 

horas_actividad = np.random.uniform(low=0, high=10, size=n)
ruido_neg = np.random.normal(loc=0, scale=2, size=n)
imc = 35 - (1.2 * horas_actividad) + ruido_neg 

# --- FASE 3: PROBLEMAS TÉCNICOS ---
# 1. Problema de Tipo de Dato (Texto mezclado)
fc_numerica = np.random.normal(loc=75, scale=12, size=n).astype(int)
frecuencia_cardiaca = [f"{fc} bpm" if np.random.rand() < 0.10 else str(fc) for fc in fc_numerica]

# 2. Anomalías de Sensores
presion_arterial = np.random.normal(loc=120, scale=15, size=n)
indices_anomalos = np.random.choice(n, size=25, replace=False)
for idx in indices_anomalos:
    presion_arterial[idx] = 999.0 if np.random.rand() > 0.5 else -45.0

# Ensamblar DataFrame
df = pd.DataFrame({
    'Documento_Identidad': documento_identidad,
    'Nombre_Paciente': nombre_paciente,
    'Edad': edad,
    'Frecuencia_Cardiaca': frecuencia_cardiaca,
    'Presion_Arterial_Sistolica': np.round(presion_arterial, 1),
    'Nivel_Glucosa': glucosa,
    'Nivel_Trigliceridos': trigliceridos,
    'Nivel_Vitamina_D': vitamina_d,
    'Horas_Actividad_Semana': np.round(horas_actividad, 1),
    'Peso_kg': np.round(peso, 1),
    'IMC': np.round(imc, 1),
    'Colesterol_Total': np.round(colesterol, 1)
})

# 3. Datos Faltantes (NaNs) en Vitamina D (5%) y Peso (8%)
df.loc[df.sample(frac=0.05).index, 'Nivel_Vitamina_D'] = np.nan
df.loc[df.sample(frac=0.08).index, 'Peso_kg'] = np.nan

# Guardar a CSV
df.to_csv('dataset_clinico_taller.csv', index=False)
print("Dataset con PII, valores nulos y distribución leptocúrtica generado con éxito.")