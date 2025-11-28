import pandas as pd
import numpy as np

print("=== DATASET: Monitoreo de HR por horas ===\n")

datos = {
    'Hora': pd.date_range('2024-01-01', periods=10, freq='1H'),
    'HR (bpm)': [72, 75, 78, 80, 82, 79, 77, 75, 73, 70],
    'Cambio (bpm)': [0, 3, 3, 2, 2, -3, -2, -2, -2, -3]
}

df = pd.DataFrame(datos)
df.set_index('Hora', inplace=True)
print(df)
print()

# 1. ¿QUÉ ES OPERACIÓN ACUMULATIVA?
print("=" * 70)
print("1. OPERACIONES ACUMULATIVAS\n")
print("""
Acumulativas: agregan valores progresivamente
- cumsum: suma acumulada
- cumprod: producto acumulado
- rolling: ventana móvil (promedio/suma de últimos N valores)
""")
print()

# 2. CUMSUM - Suma acumulada
print("=" * 70)
print("2. CUMSUM - Suma Acumulada\n")

print(">>> Cambio acumulado en HR:")
df['Cambio_acumulado'] = df['Cambio (bpm)'].cumsum()
print(df[['HR (bpm)', 'Cambio (bpm)', 'Cambio_acumulado']])
print()

# 3. CUMPROD - Producto acumulado
print("=" * 70)
print("3. CUMPROD - Producto Acumulado\n")

df['Factor'] = [1.0, 1.02, 1.01, 1.015, 1.01, 0.98, 0.99, 0.98, 0.98, 0.99]
print(">>> Producto acumulado (efecto compuesto):")
df['Producto_acumulado'] = df['Factor'].cumprod()
print(df[['Factor', 'Producto_acumulado']].round(4))
print()

# 4. ROLLING - Ventana móvil
print("=" * 70)
print("4. ROLLING - Ventana Móvil (últimas 3 horas)\n")

print(">>> HR promedio móvil (ventana=3):")
df['HR_rolling_mean'] = df['HR (bpm)'].rolling(window=3).mean()
print(df[['HR (bpm)', 'HR_rolling_mean']].round(2))

print("\n>>> HR máximo en ventana móvil:")
df['HR_rolling_max'] = df['HR (bpm)'].rolling(window=3).max()
print(df[['HR (bpm)', 'HR_rolling_max']].head(6))
print()

# 5. APLICACIÓN CLÍNICA - TENDENCIAS
print("=" * 70)
print("5. APLICACIÓN CLÍNICA - ANÁLISIS DE TENDENCIAS\n")

print(">>> HR original vs promedio móvil (suavizado):")
resultado = df[['HR (bpm)', 'HR_rolling_mean']].copy()
resultado.columns = ['HR_original', 'HR_suavizado']
print(resultado.round(2))

print("\n>>> Detectar cambios en tendencia:")
df['Tendencia'] = df['HR_rolling_mean'].diff()
df['Estado'] = df['Tendencia'].apply(
    lambda x: 'Aumentando' if x > 0.5 else 'Disminuyendo' if x < -0.5 else 'Estable'
)
print(df[['HR (bpm)', 'HR_rolling_mean', 'Estado']].tail(6).round(2))
print()

