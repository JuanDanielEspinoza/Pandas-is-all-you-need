import pandas as pd
import numpy as np

print("=== DATASET: Monitoreo de Pacientes ===\n")

datos = {
    'Paciente': ['P001', 'P001', 'P002', 'P002', 'P001', 'P002', 'P003', 'P003'],
    'Día': [1, 2, 1, 2, 1, 1, 1, 2],
    'Turno': ['Mañana', 'Tarde', 'Mañana', 'Tarde', 'Noche', 'Noche', 'Mañana', 'Tarde'],
    'HR (bpm)': [72, 75, 95, 98, 78, 100, 65, 68],
    'Condición': ['Normal', 'Normal', 'Elevada', 'Elevada', 'Normal', 'Crítica', 'Normal', 'Normal']
}

df = pd.DataFrame(datos)
print(df)
print()

# 1. GROUPBY vs PIVOT_TABLE
print("=" * 70)
print("1. GROUPBY vs PIVOT_TABLE - Diferencias\n")

print(">>> GROUPBY (resultado: Series o DataFrame vertical):")
print(df.groupby('Paciente')['HR (bpm)'].mean())

print("\n>>> PIVOT_TABLE (resultado: matriz):")
pivot = df.pivot_table(values='HR (bpm)', index='Paciente', aggfunc='mean')
print(pivot)
print()

# 2. PIVOT_TABLE - Estructura matricial
print("=" * 70)
print("2. PIVOT_TABLE - Estructura matricial\n")

print(">>> HR por Paciente y Día (matriz):")
pivot_dia = df.pivot_table(values='HR (bpm)', index='Paciente', columns='Día', aggfunc='mean')
print(pivot_dia.round(2))

print("\n>>> HR por Paciente y Turno:")
pivot_turno = df.pivot_table(values='HR (bpm)', index='Paciente', columns='Turno', aggfunc='mean')
print(pivot_turno.round(2))
print()

# 3. MANEJO DE VALORES DUPLICADOS
print("=" * 70)
print("3. MANEJO DE VALORES DUPLICADOS EN PIVOTE\n")

print(">>> Contar mediciones (aggfunc='count'):")
pivot_count = df.pivot_table(values='HR (bpm)', index='Paciente', columns='Día', aggfunc='count')
print(pivot_count)

print("\n>>> Máximo HR por Paciente y Día:")
pivot_max = df.pivot_table(values='HR (bpm)', index='Paciente', columns='Día', aggfunc='max')
print(pivot_max)
print()

# 4. CROSSTAB - Conteos y relaciones
print("=" * 70)
print("4. CROSSTAB - Conteos y relaciones\n")

print(">>> Conteo: Condición vs Turno:")
ct = pd.crosstab(df['Condición'], df['Turno'])
print(ct)

print("\n>>> Porcentaje por fila:")
ct_pct = pd.crosstab(df['Condición'], df['Turno'], normalize='index') * 100
print(ct_pct.round(1))
print()

# 5. APLICACIÓN CLÍNICA - Análisis por Turno
print("=" * 70)
print("5. APLICACIÓN CLÍNICA - Análisis por Turno\n")

print(">>> HR promedio por Turno:")
hr_turno = df.pivot_table(values='HR (bpm)', index='Turno', aggfunc='mean')
print(hr_turno.round(2))

print("\n>>> Distribución de Condiciones por Turno:")
print(pd.crosstab(df['Turno'], df['Condición']))
print()

