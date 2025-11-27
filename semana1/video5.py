import pandas as pd
import numpy as np

print("=== DATASET: Pacientes con Nulos ===\n")

datos = {
    'Paciente': ['P001', 'P002', 'P003', 'P003', 'P004', 'P005'],
    'HR (bpm)': [72, np.nan, 110, 110, 88, np.nan],
    'Systolic_BP (mmHg)': [120, 140, np.nan, 160, 130, 115],
    'SpO2 (%)': [98, 94, 92, 92, np.nan, 99],
    'Edad': [35, 42, 28, 28, 55, 60]
}

df = pd.DataFrame(datos)
print(df)
print()

print("1. DETECTAR NULOS")
print("=" * 60)
print("Contar nulos:", df.isnull().sum().to_dict())
print("Filas con nulos:", df[df.isnull().any(axis=1)].shape[0], "\n")

print("2. DROPNA - ESTRATEGIAS")
print("=" * 60)
print("❌ Eliminar cualquier nulo:")
df_any = df.dropna(how='any')
print(f"Filas: {len(df)} → {len(df_any)}\n")

print("✓ Eliminar duplicados:")
df_dup = df.drop_duplicates()
print(f"Filas: {len(df)} → {len(df_dup)}\n")

print("3. FILLNA - ESTRATEGIAS DE IMPUTACIÓN")
print("=" * 60)
df_clean = df.drop_duplicates()

print("Media:")
df_media = df_clean.copy()
df_media['HR (bpm)'] = df_media['HR (bpm)'].fillna(df_media['HR (bpm)'].mean())
print(df_media[['Paciente', 'HR (bpm)']].head(2))

print("\nForward Fill:")
df_ffill = df_clean.copy()
df_ffill['SpO2 (%)'] = df_ffill['SpO2 (%)'].fillna(method='ffill')
print(df_ffill[['Paciente', 'SpO2 (%)']].head(2))

print("\nValor constante (70):")
df_const = df_clean.copy()
df_const['HR (bpm)'] = df_const['HR (bpm)'].fillna(70)
print(df_const[['Paciente', 'HR (bpm)']].head(2))
print()

print("=" * 60)
print("CONCLUSIÓN - Pipeline de Limpieza")
print("=" * 60)
print("""
1. Detectar nulos: df.isnull().sum()
2. Eliminar duplicados: df.drop_duplicates()
3. Llenar nulos:
   - Media: df.fillna(df.mean())
   - Forward fill: df.fillna(method='ffill')
   - Constante: df.fillna(70)

✓ Datos limpios = Análisis confiable
""")
print("=" * 60)