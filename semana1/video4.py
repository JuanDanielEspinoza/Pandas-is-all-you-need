import pandas as pd
import time

# Dataset: Pacientes con frecuencia cardíaca
print("=== DATASET: Pacientes ===\n")

datos = {
    'Paciente': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'HR (bpm)': [72, 95, 110, 88, 65],
    'Systolic_BP (mmHg)': [120, 140, 160, 130, 115],
    'Diastolic_BP (mmHg)': [80, 90, 100, 85, 75]
}

df = pd.DataFrame(datos)
print(df)
print()

# 1. APPLY - Función en filas
print("1. APPLY - Clasificar Frecuencia Cardíaca\n")

def diagnostico_hr(fila):
    if fila['HR (bpm)'] > 100:
        return 'Taquicardia'
    elif fila['HR (bpm)'] < 60:
        return 'Bradicardia'
    else:
        return 'Normal'

df['Diagnostico_HR'] = df.apply(diagnostico_hr, axis=1)
print(df[['Paciente', 'HR (bpm)', 'Diagnostico_HR']])
print()

# 2. MAP - Transformar valores en Series
print("2. MAP - Transformar en Series\n")

diagnostico_map = {'Taquicardia': 'ALERTA', 'Bradicardia': 'ALERTA', 'Normal': 'OK'}
df['Estado'] = df['Diagnostico_HR'].map(diagnostico_map)
print(df[['Paciente', 'Diagnostico_HR', 'Estado']])
print()

# 3. LAMBDA EN COLUMNAS NUMÉRICAS
print("3. LAMBDA - Clasificar HR\n")

df['Categoria_HR'] = df['HR (bpm)'].apply(lambda x: 'Crítica' if x > 110 else 'Elevada' if x > 100 else 'Normal')
print(df[['Paciente', 'HR (bpm)', 'Categoria_HR']])
print()

# 4. LAMBDA CON MÚLTIPLES COLUMNAS
print("4. LAMBDA - Calcular Presión de Pulso\n")

df['Presion_Pulso'] = df.apply(lambda fila: fila['Systolic_BP (mmHg)'] - fila['Diastolic_BP (mmHg)'], axis=1)
print(df[['Paciente', 'Systolic_BP (mmHg)', 'Diastolic_BP (mmHg)', 'Presion_Pulso']])
print()

print(df[['Paciente', 'Systolic_BP (mmHg)', 'Diastolic_BP (mmHg)', 'Presion_Pulso']])
print()

# 5. EVITAR APPLY - Operaciones vectorizadas
print("5. EVITAR APPLY - Operaciones vectorizadas\n")

print("❌ LENTO - Usar apply:")
start = time.time()
resultado_apply = df['HR (bpm)'].apply(lambda x: x * 1.1)
tiempo_apply = time.time() - start

print("✓ RÁPIDO - Operación vectorizada:")
start = time.time()
resultado_vec = df['HR (bpm)'] * 1.1
tiempo_vec = time.time() - start

print(f"Apply: {tiempo_apply:.6f}s | Vectorizada: {tiempo_vec:.6f}s")
print(f"Speedup: {tiempo_apply/tiempo_vec:.2f}x más rápido\n")
print(resultado_vec.tolist())
print()

# 6. CONCLUSIÓN
print("=" * 80)
print("CONCLUSIÓN")
print("=" * 80)
print("""
✓ Apply: Lógica compleja con múltiples columnas
✓ Map: Transformar valores en una Serie
✓ Vectorizado: Operaciones simples (MÁS RÁPIDO)
✓ Apply te da flexibilidad pero ÚSALO CON CUIDADO
""")
print("=" * 80)