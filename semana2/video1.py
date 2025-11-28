import pandas as pd
import numpy as np

print("=== DATASET: Pacientes con múltiples mediciones ===\n")

datos = {
    'Paciente': ['P001', 'P001', 'P001', 'P002', 'P002', 'P002', 'P003', 'P003'],
    'Día': [1, 2, 3, 1, 2, 3, 1, 2],
    'HR (bpm)': [72, 75, 78, 95, 98, 100, 65, 68],
    'Systolic_BP (mmHg)': [120, 122, 125, 140, 145, 150, 115, 118],
    'SpO2 (%)': [98, 97, 96, 94, 93, 92, 99, 99]
}

df = pd.DataFrame(datos)
print(df)
print()

# 1. ¿QUÉ ES GROUPBY?
print("=" * 70)
print("1. ¿QUÉ ES GROUPBY? - Agrupar para análisis clínico")
print("=" * 70)
print("""
GroupBy:
- Agrupa filas por valores comunes en una columna
- Permite análisis por paciente, por día, por diagnóstico
- Esencial en datos clínicos para comparar tendencias
""")
print()

# 2. GROUPBY BÁSICO
print("2. GROUPBY BÁSICO - Agrupar por Paciente\n")

print(">>> Agrupar por Paciente:")
agrupado = df.groupby('Paciente')
print(f"Número de grupos: {agrupado.ngroups}\n")
for paciente, grupo in df.groupby('Paciente'):
    print(f"{paciente}: {len(grupo)} mediciones")
print()

# 3. AGREGACIONES SIMPLES
print("=" * 70)
print("3. AGREGACIONES SIMPLES - Una función, una columna\n")

print(">>> HR promedio por Paciente:")
print(df.groupby('Paciente')['HR (bpm)'].mean())

print("\n>>> Systolic BP máximo por Paciente:")
print(df.groupby('Paciente')['Systolic_BP (mmHg)'].max())

print("\n>>> SpO2 mínimo por Paciente:")
print(df.groupby('Paciente')['SpO2 (%)'].min())
print()

# 4. AGREGACIONES MÚLTIPLES
print("=" * 70)
print("4. AGREGACIONES MÚLTIPLES - Una función, múltiples columnas\n")

print(">>> Promedio de todas las señales vitales:")
resultado = df.groupby('Paciente')[['HR (bpm)', 'Systolic_BP (mmHg)', 'SpO2 (%)']].mean()
print(resultado.round(2))
print()

# 5. AGREGACIONES DIFERENTES POR COLUMNA
print("=" * 70)
print("5. AGREGACIONES DIFERENTES POR COLUMNA\n")

print(">>> Estadísticas variadas por Paciente:")
resultado_custom = df.groupby('Paciente').agg({
    'HR (bpm)': ['mean', 'max', 'min'],
    'Systolic_BP (mmHg)': 'mean',
    'SpO2 (%)': ['min', 'count']
})
print(resultado_custom.round(2))
print()
