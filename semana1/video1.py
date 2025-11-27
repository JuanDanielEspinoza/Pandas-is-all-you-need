import pandas as pd
import numpy as np

# 1. RECORDATORIO: ¿QUÉ ES UNA SERIE?
print("=== 1. SERIE: Datos univariables ===\n")

hr_paciente_1 = pd.Series([72, 75, 73, 74, 76, 75, 74], 
                          index=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
                          name='Frecuencia Cardíaca (bpm)')

print(hr_paciente_1)
print(f"Tipo: {type(hr_paciente_1)}\n")

# 2. RECORDATORIO: ¿QUÉ ES UN DATAFRAME?
print("=== 2. DATAFRAME: Datos multivariables ===\n")

datos_pacientes = {
    'Paciente': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'HR (bpm)': [72, 68, 95, 88, 65],
    'RR (rpm)': [16, 14, 20, 18, 12],
    'SpO2 (%)': [98, 97, 94, 96, 99],
    'Edad': [35, 42, 28, 55, 60],
    'Condición': ['Normal', 'Normal', 'Alerta', 'Normal', 'Normal']
}

df_pacientes = pd.DataFrame(datos_pacientes)
print(df_pacientes)
print(f"Tipo: {type(df_pacientes)}\n")

# 3. CREACIÓN MANUAL: MÉTODO DIDÁCTICO
print("=== 3. CREACIÓN MANUAL (para pruebas y simulación) ===\n")

filas = []
for i in range(3):
    fila = {
        'Paciente': f'P00{6+i}',
        'HR (bpm)': np.random.randint(60, 100),
        'RR (rpm)': np.random.randint(12, 20),
        'SpO2 (%)': np.random.randint(94, 100),
        'Edad': np.random.randint(25, 70),
        'Condición': 'Monitoreado'
    }
    filas.append(fila)

df_simulado = pd.DataFrame(filas)
print(df_simulado)
print()

# 4. GUARDAR Y CARGAR DESDE CSV
print("=== 4. GUARDAR Y CARGAR DESDE CSV ===\n")

ruta_csv = r'c:\Users\ASUS\Desktop\codigos semillero\semana1\datos_vitales.csv'
df_pacientes.to_csv(ruta_csv, index=False)
print(f"Archivo guardado: {ruta_csv}\n")

# Carga SIN especificar tipos
print("Carga automática (sin especificar dtype):")
df_auto = pd.read_csv(ruta_csv)
print(df_auto.dtypes)
print()

# Carga especificando tipos (BUENA PRÁCTICA)
print("Carga especificando tipos (RECOMENDADO):")
tipos_datos = {
    'Paciente': str,
    'HR (bpm)': int,
    'RR (rpm)': int,
    'SpO2 (%)': int,
    'Edad': int,
    'Condición': str
}

df_cargado = pd.read_csv(ruta_csv, dtype=tipos_datos)
print(df_cargado.dtypes)
print()

# 5. ANÁLISIS BÁSICO
print("=== 5. ANÁLISIS: Señales Vitales ===\n")

print("Pacientes con HR elevada (> 85 bpm):")
print(df_cargado[df_cargado['HR (bpm)'] > 85])
print()

print("Pacientes con SpO₂ baja (< 95%):")
print(df_cargado[df_cargado['SpO2 (%)'] < 95])
print()

print("Promedios de señales vitales:")
print(f"HR promedio: {df_cargado['HR (bpm)'].mean():.2f} bpm")
print(f"RR promedio: {df_cargado['RR (rpm)'].mean():.2f} rpm")
print(f"SpO₂ promedio: {df_cargado['SpO2 (%)'].mean():.2f}%\n")

# 6. CIERRE
print("=" * 80)
print("Un DataFrame es el PUNTO DE PARTIDA de todo análisis de datos.")
print("Todo análisis de SEÑALES VITALES comienza aquí.")
print("=" * 80)