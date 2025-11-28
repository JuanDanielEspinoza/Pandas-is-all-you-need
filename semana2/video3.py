import pandas as pd
import numpy as np

print("=== DATASET: Monitoreo de Pacientes ===\n")

datos = {
    'Paciente': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'HR (bpm)': [72, 110, 95, 145, 58, 88],
    'Systolic_BP (mmHg)': [120, 160, 140, 170, 100, 130],
    'SpO2 (%)': [98, 92, 95, 88, 99, 94],
    'Condición': ['Normal', 'Crítica', 'Elevada', 'Crítica', 'Normal', 'Elevada']
}

df = pd.DataFrame(datos)
print(df)
print()

# 1. SORT_VALUES - Descendente
print("=" * 70)
print("1. SORT_VALUES - Ordenamiento descendente\n")

print(">>> Ordenar por HR (descendente - más críticos primero):")
df_hr_desc = df.sort_values('HR (bpm)', ascending=False)
print(df_hr_desc[['Paciente', 'HR (bpm)', 'Condición']])
print()

# 2. MÚLTIPLES COLUMNAS
print("=" * 70)
print("2. MÚLTIPLES COLUMNAS - Ordenar por prioridad\n")

print(">>> Ordenar por Condición (asc) y HR (desc):")
df_multi = df.sort_values(['Condición', 'HR (bpm)'], ascending=[True, False])
print(df_multi[['Paciente', 'Condición', 'HR (bpm)']])
print()

# 3. NLARGEST Y NSMALLEST
print("=" * 70)
print("3. NLARGEST Y NSMALLEST - Top extremos\n")

print(">>> 3 pacientes con HR más ALTA (riesgo de taquicardia):")
print(df.nlargest(3, 'HR (bpm)')[['Paciente', 'HR (bpm)']])

print("\n>>> 2 pacientes con HR más BAJA (riesgo de bradicardia):")
print(df.nsmallest(2, 'HR (bpm)')[['Paciente', 'HR (bpm)']])

print("\n>>> 3 pacientes con SpO2 más BAJA (hipoxemia):")
print(df.nsmallest(3, 'SpO2 (%)')[['Paciente', 'SpO2 (%)']])
print()

# 4. RANK - Clasificar por posición
print("=" * 70)
print("4. RANK - Clasificar por posición (1=menor, 6=mayor)\n")

df['Rank_HR'] = df['HR (bpm)'].rank()
df['Rank_BP'] = df['Systolic_BP (mmHg)'].rank(ascending=False)
print(">>> Ranking de HR y Presión Sistólica:")
print(df[['Paciente', 'HR (bpm)', 'Rank_HR', 'Systolic_BP (mmHg)', 'Rank_BP']])
print()

# 5. APLICACIÓN CLÍNICA - ALERTAS
print("=" * 70)
print("5. APLICACIÓN CLÍNICA - IDENTIFICAR ALERTAS\n")

print(">>> Pacientes con HR CRÍTICA (> 100):")
criticos_hr = df[df['HR (bpm)'] > 100].sort_values('HR (bpm)', ascending=False)
print(criticos_hr[['Paciente', 'HR (bpm)', 'Condición']])

print("\n>>> Pacientes con SpO2 CRÍTICA (< 93%):")
criticos_spo2 = df[df['SpO2 (%)'] < 93].sort_values('SpO2 (%)')
print(criticos_spo2[['Paciente', 'SpO2 (%)', 'Condición']])

print("\n>>> TOP 2 Pacientes de mayor riesgo (criterio: HR > 100 O SpO2 < 93):")
riesgo = df[(df['HR (bpm)'] > 100) | (df['SpO2 (%)'] < 93)]
print(riesgo.nlargest(2, 'HR (bpm)')[['Paciente', 'HR (bpm)', 'SpO2 (%)']])
print()

