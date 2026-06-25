# Análisis de Dispersión y Homogeneidad de Datos con Python

Este proyecto implementa un análisis estadístico descriptivo utilizando **Python**, **Pandas**, **Seaborn** y **Matplotlib** para evaluar y comparar la variabilidad de dos conjuntos de datos: tiempos de corredores en pruebas de 100 metros y la estatura de un grupo de alumnos.

El objetivo principal es determinar cuál de los dos grupos presenta un comportamiento más homogéneo mediante el cálculo del Coeficiente de Variación (CV), demostrando que la desviación estándar absoluta no siempre es suficiente para realizar comparaciones válidas entre variables con diferentes escalas.

## 📊 Métricas Estadísticas Obtenidas

A partir del procesamiento del archivo `tarea_clase_3.xlsx`, se extrajeron los siguientes resultados estadísticos[cite: 3, 4]:

| Conjunto de Datos | Desviación Estándar ($\sigma$) | Coeficiente de Variación (CV) | Estado del Grupo |
| :--- | :---: | :---: | :---: |
| **Corredores (100mts)** | 0.799 | 0.062 (6.2%) | Mayor dispersión relativa |
| **Estatura Alumnos** | 6.329 | 0.037 (3.7%) | **Más Homogéneo** |

## 🔍 Conclusión del Análisis

Aunque el grupo de **Corredores** presenta una desviación estándar numéricamente más baja (0.799), esto se debe puramente a la escala de la medición (segundos/metros)[cite: 4]. 

Al calcular el **Coeficiente de Variación** (que relativiza la desviación respecto a la media), observamos que el grupo de **Estatura de los Alumnos** posee un coeficiente menor (0.037 vs 0.062)[cite: 4]. Por lo tanto, metodológicamente concluimos que **el conjunto de datos más homogéneo es el de "Estatura de los alumnos"**[cite: 4].

## 🛠️ Tecnologías y Librerías Utilizadas
- **Python 3**
- **Pandas:** Para la lectura estructurada de múltiples pestañas de Excel.
- **Seaborn & Matplotlib:** Para la generación de gráficos de cajas (`boxplot`) que permiten visualizar la mediana, los cuartiles y la dispersión física de las muestras.

## 🚀 Cómo Ejecutar el Proyecto
1. Asegúrate de tener el archivo de datos `tarea_clase_3.xlsx` en la raíz del proyecto.
2. Instala las dependencias requeridas:
```bash
   pip install pandas seaborn matplotlib openpyxl
