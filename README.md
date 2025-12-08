# Análisis Exploratorio de Datos - Spotify 🎧📊

Proyecto final de la materia Programacion, donde realizamos un análisis exploratorio sobre datos de Spotify extraidos de Kaggle, utilizando Python, Pandas y Matplotlib.

---

## 📌 Objetivo del proyecto

El objetivo es analizar:
- popularidad de canciones
- géneros más escuchados
- artistas más presentes
- evolución musical en los últimos años
- correlación entre seguidores y popularidad

---

## 📁 Estructura del proyecto
Proyecto_Spotify
│── data/
│ └── spotify_data_clean.csv
│
│── src/
│ └── main.py
│
│── venv/
│── output_*.png
│── datos_procesados.csv
│── requirements.txt
│── README.md

---

## ▶ Ejecución del proyecto

### 1️⃣ Crear el entorno virtual (solo la primera vez)
python -m venv venv
### 2️⃣ Activar entorno (Windows)
venv\Scripts\activate
### 3️⃣ Instalar dependencias
pip install -r requirements.txt
### 4️⃣ Ejecutar el programa
python src/main.py

---

## 📊 Resultados principales

### ✔ Top artistas
Identifica los artistas con mayor cantidad de canciones en la base.

### ✔ Top géneros
Muestra los géneros más frecuentes.

### ✔ Popularidad por año
Promedio de popularidad agrupada por año de lanzamiento.

### ✔ Gráficos generados

El script genera:
- `output_top_generos.png`
- `output_followers_pop.png`
- `output_popularidad.png`
- `output_canciones_por_año.png`

También exporta:
datos_procesados.csv
---

## 🛠 Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- CSV
- Entorno virtual (venv)

---

## 📬 Autor

Proyecto final desarrollado por Carabajal Jose Patricio
