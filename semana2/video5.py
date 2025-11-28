import pandas as pd

print("=== DATASET: Signos vitales + Demografía ===\n")

vitales = {
    'Paciente': ['P001', 'P002', 'P003', 'P004'],
    'HR (bpm)': [72, 95, 110, 88],
    'SpO2 (%)': [98, 94, 92, 96]
}
df_vitales = pd.DataFrame(vitales)

demografia = {
    'Paciente': ['P001', 'P002', 'P005', 'P006'],
    'Edad': [35, 42, 28, 55],
    'Diagnóstico': ['Normal', 'Hipertensión', 'Diabetes', 'Asma']
}
df_demo = pd.DataFrame(demografia)

print("DataFrame 1 - Signos Vitales:")
print(df_vitales)
print("\nDataFrame 2 - Demografía:")
print(df_demo)
print()

# 1. MERGE - Tipos de combinación
print("=" * 70)
print("1. MERGE - Tipos (inner, left, outer)\n")

print(">>> INNER JOIN (solo pacientes en ambos DataFrames):")
merge_inner = pd.merge(df_vitales, df_demo, on='Paciente', how='inner')
print(merge_inner)

print("\n>>> LEFT JOIN (mantiene todos los vitales):")
merge_left = pd.merge(df_vitales, df_demo, on='Paciente', how='left')
print(merge_left)

print("\n>>> OUTER JOIN (todos los pacientes):")
merge_outer = pd.merge(df_vitales, df_demo, on='Paciente', how='outer')
print(merge_outer)
print()

# 2. CONCAT - Horizontal vs Vertical
print("=" * 70)
print("2. CONCAT - Concatenación\n")

vitales2 = {
    'Paciente': ['P001', 'P002', 'P003', 'P004'],
    'RR (rpm)': [16, 20, 22, 18]
}
df_vitales2 = pd.DataFrame(vitales2)

print(">>> CONCAT Horizontal (axis=1, agregar columnas):")
concat_h = pd.concat([df_vitales, df_vitales2], axis=1)
print(concat_h)

print("\n>>> CONCAT Vertical (axis=0, agregar filas):")
vitales_mas = pd.DataFrame({'Paciente': ['P005'], 'HR (bpm)': [100], 'SpO2 (%)': [91]})
concat_v = pd.concat([df_vitales, vitales_mas], axis=0, ignore_index=True)
print(concat_v)
print()

# 3. JOIN - Sobre índices
print("=" * 70)
print("3. JOIN - Sobre índices\n")

df_v_idx = df_vitales.set_index('Paciente')
df_d_idx = df_demo.set_index('Paciente')

print(">>> JOIN por índice (left):")
join_result = df_v_idx.join(df_d_idx, how='left')
print(join_result)
print()

# 4. ERRORES COMUNES
print("=" * 70)
print("4. ERRORES COMUNES\n")

print("❌ Duplicados: combinación cartesiana")
print(f"Duplicados vitales: {df_vitales['Paciente'].duplicated().sum()}")
print(f"Duplicados demo: {df_demo['Paciente'].duplicated().sum()}\n")

print("❌ Inner join: pierde P005, P006")
print("✓ Solución: usar left o outer según necesidad")
print()

