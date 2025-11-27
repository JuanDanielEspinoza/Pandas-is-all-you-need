import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("=== DATASET: Monitoreo de Pacientes ===\n")

fechas = pd.date_range('2024-01-01', periods=8, freq='6H')
datos = {
    'Timestamp': fechas,
    'Paciente': ['P001', 'P002', 'P001', 'P002', 'P001', 'P002', 'P001', 'P002'],
    'HR (bpm)': [72, 95, 110, 88, 78, 92, 85, 100],
    'Diagnóstico': ['Normal', 'Elevada', 'Crítica', 'Elevada', 'Normal', 'Elevada', 'Normal', 'Crítica']
}

df = pd.DataFrame(datos)
df.set_index('Timestamp', inplace=True)
print(df)
print()

# 1. SORT_VALUES - Por una columna
print("1. SORT_VALUES - Ordenar por una columna\n")

print(">>> Ordenar por HR ascendente:")
df_sorted_asc = df.sort_values('HR (bpm)')
print(df_sorted_asc[['Paciente', 'HR (bpm)']])

print("\n>>> Ordenar por HR descendente:")
df_sorted_desc = df.sort_values('HR (bpm)', ascending=False)
print(df_sorted_desc[['Paciente', 'HR (bpm)']].head(3))
print()

# 2. SORT_VALUES - Múltiples columnas
print("2. SORT_VALUES - Múltiples columnas\n")

print(">>> Ordenar por Paciente (asc) y HR (desc):")
df_multi = df.sort_values(['Paciente', 'HR (bpm)'], ascending=[True, False])
print(df_multi[['Paciente', 'HR (bpm)']])
print()

# 3. SORT_INDEX - Por tiempo (Timestamp)
print("3. SORT_INDEX - Ordenar por índice (Timestamp)\n")

df_desordenado = df.sample(frac=1)
print(">>> DataFrame desordenado (por tiempo):")
print(df_desordenado[['Paciente', 'HR (bpm)']].head(3))

print("\n>>> Después de sort_index():")
df_tiempo = df_desordenado.sort_index()
print(df_tiempo[['Paciente', 'HR (bpm)']].head(3))
print()

# 4. INPLACE - Modificar original vs copia
print("4. PARÁMETRO INPLACE - Diferencias\n")

print(">>> SIN inplace (return nuevo DataFrame):")
df_copy = df.copy()
resultado = df_copy.sort_values('HR (bpm)')
print(f"Original: {df_copy['HR (bpm)'].iloc[0]} | Resultado: {resultado['HR (bpm)'].iloc[0]}\n")

print(">>> CON inplace=True (modifica original):")
df_copy2 = df.copy()
df_copy2.sort_values('HR (bpm)', inplace=True)
print(f"Original modificado: {df_copy2['HR (bpm)'].iloc[0]}")
print()

# 5. CIERRE
print("=" * 60)
print("CONCLUSIÓN")
print("=" * 60)
print("""
✓ sort_values: Ordena por valores de columna
✓ sort_index: Ordena por índice (timestamps)
✓ ascending: False para orden descendente
✓ Múltiples columnas: [col1, col2]
✓ inplace=True: Modifica el original

Ordenar es esencial para:
- Trazar curvas de señales vitales
- Detectar tendencias en el tiempo
- Analizar secuencias de eventos
""")
print("=" * 60)