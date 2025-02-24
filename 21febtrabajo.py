# -*- coding: utf-8 -*-
"""21febTrabajo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FL_VQI5CxB-_XC3e6Z8KbhfNuw2v8W-c

Trabajo dia 21 Febrero
Grupo: David Ricardo Jimenez,
Cesar Martinez
"""

import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns

df = pd.read_csv("/content/schizophrenia_dataset.csv")  # Cambiar nombre si es diferente

# Ver las primeras filas
df.head()

# Información general
print(df.info())

# Resumen estadístico
print(df.describe())

plt.figure(figsize=(8,5))
sns.histplot(df['age'], bins=20, kde=True, color='skyblue')
plt.title("Distribución de la Edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['hospitalizations'], y=df['disease_duration'], palette="coolwarm")
plt.title("Distribución de Hospitalizaciones y duracion de la enfermedad")
plt.xlabel("Hospitalizaciones")
plt.ylabel("Duracion Enfermedad")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x=df['hospitalizations'], y=df['disease_duration'], alpha=0.7)
plt.title("Relación entre Hospitalizaciones y Duracion de la Enfermedad")
plt.xlabel("Hospitalizaciones")
plt.ylabel("Duración de la enfermedad")
plt.show()

"""Tendencia esperada

    En general, a mayor duración de la enfermedad (disease_duration), mayor número de hospitalizaciones (hospitalizations).
    Esto es lógico, ya que los pacientes que han tenido la enfermedad por más tiempo tienden a requerir más hospitalizaciones.

Patrón de distribución

    Si los puntos se agrupan en líneas verticales, podría significar que los valores de hospitalización están discretizados (por ejemplo, valores enteros de hospitalizaciones como 0, 1, 2, etc.).
    Si los puntos son muy dispersos sin una tendencia clara, podría indicar que la duración de la enfermedad no es un factor determinante en las hospitalizaciones.

Verificación del patrón

    Si la correlación entre estas variables fue alta en el heatmap previo (cercana a +0.68), esto respalda la hipótesis de que la duración de la enfermedad aumenta la probabilidad de hospitalización.
"""

# Eliminar columnas no numéricas para evitar errores en la correlación
df_numeric = df.select_dtypes(include=['number'])

# Calcular la matriz de correlación
correlation_matrix = df_numeric.corr()

# Crear el heatmap
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor de Correlación entre Variables")
plt.show()

"""Principales Correlaciones Relevantes

    Alta correlación positiva (cercana a +1)
        disease_duration vs. diagnosis (0.83) → A mayor tiempo de enfermedad, mayor es la confirmación del diagnóstico.
        hospitalizations vs. disease_duration (0.68) → Personas con mayor duración de la enfermedad tienden a ser hospitalizadas más veces.
        negative_symptom_score vs. diagnosis (0.84) → Diagnósticos más severos se asocian con puntuaciones más altas de síntomas negativos.
        positive_symptom_score vs. diagnosis (0.85) → Similar al caso anterior, los síntomas positivos también están fuertemente relacionados con el diagnóstico.

    Alta correlación negativa (cercana a -1)
        global_assessment_of_functioning vs. negative_symptom_score (-0.72) → A mayor puntuación de síntomas negativos, menor es la funcionalidad global del paciente.
        global_assessment_of_functioning vs. positive_symptom_score (-0.71) → Similar a la relación anterior, a mayor gravedad de síntomas, menor capacidad funcional.

    Correlaciones moderadas interesantes
        suicide_attempt vs. positive_symptom_score (0.41) → Los intentos de suicidio parecen estar asociados con una mayor puntuación de síntomas positivos.
        stress_factors vs. negative_symptom_score (0.29) → El estrés parece influir en la gravedad de los síntomas negativos.
        medication_adherence vs. global_assessment_of_functioning (0.29) → Una mejor adherencia a la medicación podría estar asociada con una mayor funcionalidad global.

📊 Posibles Patrones y Tendencias

✅ Duración de la enfermedad y hospitalización

    Personas con mayor tiempo con la enfermedad tienden a ser hospitalizadas con más frecuencia.

✅ Síntomas y funcionalidad

    Los pacientes con síntomas más graves (positivos y negativos) presentan menor capacidad funcional según la evaluación global.

✅ Impacto del estrés y adherencia al tratamiento

    Los síntomas negativos tienen una correlación moderada con los factores de estrés.
    La adherencia a la medicación parece tener un impacto positivo en la funcionalidad del paciente.

📌 Conclusiones Claves

📍 Los síntomas (positivos y negativos) son los factores más fuertemente correlacionados con el diagnóstico y la funcionalidad del paciente.
📍 La hospitalización está ligada a la duración de la enfermedad, lo que sugiere que un diagnóstico temprano podría ayudar a reducir hospitalizaciones.
📍 El estrés y la falta de adherencia a la medicación pueden influir negativamente en la funcionalidad de los pacientes.
📍 Las intervenciones deben centrarse en mejorar la adherencia al tratamiento y reducir el estrés para mejorar la calidad de vida de los pacientes.
"""