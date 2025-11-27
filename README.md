📘 Pandas Learning Path — Manejo e Interpretación de Datos Tabulares

Bienvenido a este repositorio orientado al aprendizaje práctico de
Pandas, la librería fundamental de Python para el análisis y
procesamiento de datos tabulares.
Aquí encontrarás:

-   Guías estructuradas por niveles
-   Notebooks interactivos
-   Ejercicios reales
-   Retos aplicados al contexto de datos clínicos (sin datos sensibles)
-   Buenas prácticas de análisis de datos
-   Mini-proyectos de interpretación y reporte

📌 Objetivo del repositorio

Permitir al estudiante aprender Pandas de forma progresiva, con ejemplos
claros, ejercicios guiados y aplicaciones reales, dominando la
manipulación, limpieza, transformación, agregación y análisis de datos
tabulares.

🧭 Mapa de Aprendizaje (Learning Path)

📖 Semana 1 — Fundamentos Intermedios de Pandas

-   Creación y manipulación de DataFrames
-   Indexación avanzada
-   Operaciones con columnas
-   Funciones: apply, map, applymap, lambda
-   Valores nulos y duplicados
-   Ordenamiento

📊 Semana 2 — Limpieza y Preprocesamiento

-   Outliers
-   Conversión de tipos
-   Manejo de fechas
-   Validación de estructura

📈 Semana 3 — Exploración e Interpretación (EDA)

-   Estadísticos
-   Agrupación
-   Pivot tables
-   Visualización rápida

🤖 Semana 4 — Pandas para Machine Learning

-   Feature engineering
-   Encoding
-   Joins avanzados
-   Preparación final del dataset

🗂 Estructura del Repositorio

    pandas-learning-path/
    ├── README.md
    ├── data/
    ├── semana_1_fundamentos/
    ├── semana_2_preprocesamiento/
    ├── semana_3_eda/
    ├── semana_4_pandas_ml/
    └── proyectos/

📘 Contenido Clave

Lectura de DataFrames

    import pandas as pd
    df = pd.read_csv("data/vital_signs_sample.csv")
    df.head()

Indexación avanzada

    df.loc[0:5, ["HR", "SpO2"]]
    df.iloc[0:10, 0:3]
    df[df["HR"] > 100]

Limpieza

    df["HR"] = df["HR"].fillna(df["HR"].median())
    df = df.drop_duplicates()

Transformaciones

    def risk_index(row):
        return row["HR"] / row["SpO2"]
    df["RiskIndex"] = df.apply(risk_index, axis=1)

Agregación

    df.groupby("patient_id")[["HR", "SpO2"]].mean()

🧪 Mini-Proyectos

-   Limpieza de dataset de signos vitales
-   Exploración descriptiva
-   Preparación para ML

📝 Cómo usar

    git clone https://github.com/usuario/pandas-learning-path.git
    pip install -r requirements.txt
    jupyter notebook

🤝 Contribuciones

Bienvenidas mejoras, ejercicios y notebooks.

📧 Contacto

Juan Daniel Espinoza
