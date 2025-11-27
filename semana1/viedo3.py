import pandas as pd

# Dataset: Pacientes con mediciones clínicas
print("=== DATASET ===\n")

datos = {
    'Paciente': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'HR (bpm)': [72, 95, 110, 88, 65],
    'Systolic_BP (mmHg)': [120, 140, 160, 130, 115],
    'Diagnóstico': ['Normal', 'Hipertensión', 'Crisis', 'Hipertensión', 'Normal']
}

df = pd.DataFrame(datos)
print(df)
print()

# 1. CREAR NUEVAS COLUMNAS
print("1. CREAR NUEVAS COLUMNAS\n")

df['Pulse_Pressure'] = df['Systolic_BP (mmHg)'] - 60
print(df[['Paciente', 'Systolic_BP (mmHg)', 'Pulse_Pressure']])
print()

# 2. ÍNDICE DE CHOQUE (HR / Systolic BP)
print("2. ÍNDICE DE CHOQUE\n")

df['Shock_Index'] = df['HR (bpm)'] / df['Systolic_BP (mmHg)']
print(df[['Paciente', 'Shock_Index']])
print()

# 3. RENOMBRAR COLUMNAS
print("3. RENOMBRAR COLUMNAS\n")

df_rename = df.rename(columns={'HR (bpm)': 'FC', 'Systolic_BP (mmHg)': 'PAS'})
print(df_rename[['Paciente', 'FC', 'PAS']].head(2))
print()

# 4. REEMPLAZAR VALORES
print("4. REEMPLAZAR VALORES\n")

df_replace = df.copy()
df_replace['Diagnóstico'] = df_replace['Diagnóstico'].replace({
    'Normal': 'Sin Patología',
    'Crisis': 'EMERGENCIA'
})
print(df_replace[['Paciente', 'Diagnóstico']])
print()

# 5. ELIMINAR COLUMNAS
print("5. ELIMINAR COLUMNAS\n")

df_drop = df.drop(columns=['Pulse_Pressure'])
print(f"Columnas restantes: {df_drop.columns.tolist()}")
print()

# 6. EVITAR CHAINING - Malo vs Bueno
print("6. EVITAR CHAINING\n")

# ❌ MALO
resultado_malo = df_replace['Diagnóstico'].replace('Sin Patología', 'OK').str.upper()

# ✓ BUENO
paso1 = df_replace['Diagnóstico'].replace('Sin Patología', 'OK')
resultado_bueno = paso1.str.upper()
print(f"Resultado: {resultado_bueno.tolist()}")
print()

# 7. BUENAS PRÁCTICAS
print("7. BUENAS PRÁCTICAS\n")

# ❌ MALO - Sobrescribir
df_malo = df.copy()
df_malo['HR (bpm)'] = df_malo['HR (bpm)'] * 1.1

# ✓ BUENO - Nueva columna
df_bueno = df.copy()
df_bueno['HR_ajustado'] = df_bueno['HR (bpm)'] * 1.1
print(df_bueno[['Paciente', 'HR (bpm)', 'HR_ajustado']])
print()

print("=" * 80)
print("Resumen: Crear nuevas columnas, usar .copy(), dividir operaciones")
print("=" * 80)