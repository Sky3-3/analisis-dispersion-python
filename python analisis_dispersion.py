import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# =====================================================================
# 1. ANÁLISIS: CORREDORES
# =====================================================================
# Leemos los datos desde la fila correspondiente de la hoja por defecto
df_inicial = pd.read_excel("tarea_clase_3.xlsx", header=3)
df_corredores = df_inicial["Prueba mts"].dropna().astype("int")

print("=== Corredores ===")
print(df_corredores.head())

std_corredores = df_corredores.std()
cv_corredores = std_corredores / df_corredores.mean()

print(f"Desviación Estándar: {round(std_corredores, 3)}")
print(f"Coeficiente de Variación: {round(cv_corredores, 3)}\n")

# Generación del gráfico de caja
plt.figure(figsize=(6, 4))
sns.boxplot(data=df_corredores, color="purple")
plt.title("Corredores de Prueba sobre los 100mts")
plt.ylabel("Prueba mts")
plt.savefig("Corredores.png", dpi=300, bbox_inches='tight') # Guarda la imagen para GitHub
plt.close()

# =====================================================================
# 2. ANÁLISIS: ESTATURA DE LOS ALUMNOS
# =====================================================================
# Especificamos explícitamente la pestaña de interés
df_inicial_1 = pd.read_excel("tarea_clase_3.xlsx", header=3, sheet_name="Estatura Alumnos")
df_estatura = df_inicial_1["Estatura"].dropna().astype("int")

print("=== Estatura Alumnos ===")
print(df_estatura.head())

std_estatura = df_estatura.std()
cv_estatura = std_estatura / df_estatura.mean()

print(f"Desviación Estándar: {round(std_estatura, 3)}")
print(f"Coeficiente de Variación: {round(cv_estatura, 3)}\n")

# Generación del gráfico de caja
plt.figure(figsize=(6, 4))
sns.boxplot(data=df_estatura, color="orange")
plt.title("Estatura de los Alumnos")
plt.ylabel("Estatura")
plt.savefig("Estatura Alumnos.png", dpi=300, bbox_inches='tight') # Guarda la imagen para GitHub
plt.close()

print("¡Procesamiento completo! Los gráficos se guardaron como 'Corredores.png' y 'Estatura Alumnos.png'.")

