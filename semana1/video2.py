import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Crear dataset de ejemplo: Monitoreo de Pacientes
print("=== DATASET: Monitoreo de Señales Vitales ===\n")

fechas = pd.date_range('2024-01-01', periods=10, freq='H')
datos = {
    'Timestamp': fechas,
    'Paciente': ['P001'] * 5 + ['P002'] * 5,
    'HR (bpm)': [72, 78, 95, 110, 105, 68, 75, 88, 92, 100],
    'RR (rpm)': [16, 17, 19, 22, 21, 14, 15, 18, 20, 19],
    'SpO2 (%)': [98, 97, 95, 93, 92, 99, 98, 96, 94, 93],
    'Temperatura (°C)': [36.5, 36.6, 37.0, 37.2, 37.5, 36.4, 36.5, 36.8, 37.1, 37.3]
}

df = pd.DataFrame(datos)
df.set_index('Timestamp', inplace=True)
print(df)
print()

# ============================================================================
# 2. SELECCIONAR COLUMNAS CON LOC
# ============================================================================
print("=" * 80)
print("2. SELECCIONAR COLUMNAS CON LOC")
print("=" * 80)

print("\n>>> Seleccionar columnas HR y RR (por etiquetas):")
print(df.loc[:, ['HR (bpm)', 'RR (rpm)']])

print("\n>>> Seleccionar fila específica por timestamp:")
print(df.loc['2024-01-01 00:00:00'])

print("\n>>> Seleccionar rango de filas por etiquetas:")
print(df.loc['2024-01-01 00:00:00':'2024-01-01 03:00:00', ['HR (bpm)', 'RR (rpm)']])
print()

# ============================================================================
# 3. SELECCIONAR COLUMNAS CON ILOC
# ============================================================================
print("=" * 80)
print("3. SELECCIONAR COLUMNAS CON ILOC")
print("=" * 80)

print("\n>>> Primeras 5 filas (por posición numérica):")
print(df.iloc[:5])

print("\n>>> Filas 2 a 4, columnas 0 a 2 (sin incluir 5):")
print(df.iloc[2:5, 0:3])

print("\n>>> Primeras 3 filas, solo columnas HR y RR:")
print(df.iloc[:3, [1, 2]])
print()

# ============================================================================
# 4. FILTRADO BOOLEANO - CONDICIÓN SIMPLE
# ============================================================================
print("=" * 80)
print("4. FILTRADO BOOLEANO - CONDICIÓN SIMPLE")
print("=" * 80)

print("\n>>> Pacientes con HR > 100 bpm (taquicardia):")
print(df[df['HR (bpm)'] > 100])

print("\n>>> Pacientes con SpO₂ < 95% (hipoxemia):")
print(df[df['SpO2 (%)'] < 95])

print("\n>>> Registros del Paciente P001:")
print(df[df['Paciente'] == 'P001'])
print()

# ============================================================================
# 5. CONDICIONES LÓGICAS COMBINADAS
# ============================================================================
print("=" * 80)
print("5. CONDICIONES LÓGICAS COMBINADAS")
print("=" * 80)

print("\n>>> HR > 90 Y SpO₂ < 95 (alerta crítica):")
print(df[(df['HR (bpm)'] > 90) & (df['SpO2 (%)'] < 95)])

print("\n>>> Paciente P001 O HR > 100:")
print(df[(df['Paciente'] == 'P001') | (df['HR (bpm)'] > 100)])

print("\n>>> NO es Paciente P002:")
print(df[~(df['Paciente'] == 'P002')])

print("\n>>> (HR > 95) Y (RR > 18) Y (SpO₂ < 96):")
print(df[(df['HR (bpm)'] > 95) & (df['RR (rpm)'] > 18) & (df['SpO2 (%)'] < 96)])
print()

# ============================================================================
# 6. COMBINANDO LOC/ILOC CON FILTRADO BOOLEANO
# ============================================================================
print("=" * 80)
print("6. COMBINANDO LOC/ILOC CON FILTRADO BOOLEANO")
print("=" * 80)

print("\n>>> Pacientes con HR > 100, solo columnas HR y RR:")
print(df.loc[df['HR (bpm)'] > 100, ['HR (bpm)', 'RR (rpm)']])

print("\n>>> Primeras 7 filas, pacientes con alerta (HR > 90):")
print(df.iloc[:7].loc[df['HR (bpm)'] > 90])

print("\n>>> Filtro: Paciente P001 Y HR > 80, mostrar Timestamp, HR y SpO₂:")
condicion = (df['Paciente'] == 'P001') & (df['HR (bpm)'] > 80)
print(df.loc[condicion, ['HR (bpm)', 'SpO2 (%)']])
print()

# ============================================================================
# 7. CASOS DE USO PRÁCTICOS EN SALUD
# ============================================================================
print("=" * 80)
print("7. CASOS DE USO PRÁCTICOS EN SALUD")
print("=" * 80)

print("\n>>> Alertas: HR > 100 O SpO₂ < 94:")
alertas = df[(df['HR (bpm)'] > 100) | (df['SpO2 (%)'] < 94)]
print(alertas[['Paciente', 'HR (bpm)', 'SpO2 (%)']])

print("\n>>> Estado crítico: HR > 100 Y SpO₂ < 95 Y Temperatura > 37:")
critico = df[(df['HR (bpm)'] > 100) & (df['SpO2 (%)'] < 95) & (df['Temperatura (°C)'] > 37)]
print(critico)

print("\n>>> Registros normales para P001:")
normales = df[(df['Paciente'] == 'P001') & (df['HR (bpm)'] >= 60) & (df['HR (bpm)'] <= 100)]
print(normales[['HR (bpm)', 'RR (rpm)', 'SpO2 (%)']])
print()

