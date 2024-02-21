import numpy as np
import csv
from datasets import load_dataset
import pandas as pd

# Carga el conjunto de datos
dataset = load_dataset("mstz/heart_failure")
df = pd.DataFrame(dataset['train'])

# Lee el archivo CSV y lo carga en un DataFrame
csv_df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# Verifica los tipos de datos en cada columna del DataFrame original
tipos_de_datos_original = df.dtypes

# Verifica los tipos de datos en cada columna del DataFrame cargado desde el CSV
tipos_de_datos_csv = csv_df.dtypes

# Combina los DataFrames
df_completo = pd.concat([df, csv_df], axis=1)

# Calcula la cantidad de hombres fumadores y mujeres fumadoras
cantidad_hombres_fumadores = df_completo[(df_completo['sex'] == 'Male') & (df_completo['smoking'] == 'Yes')].shape[0]
cantidad_mujeres_fumadoras = df_completo[(df_completo['sex'] == 'Female') & (df_completo['smoking'] == 'Yes')].shape[0]

print('Tipos de datos en cada columna del DataFrame original:\n', tipos_de_datos_original)
print('Tipos de datos en cada columna del DataFrame cargado desde el CSV:\n', tipos_de_datos_csv)
print('Cantidad de hombres fumadores:', cantidad_hombres_fumadores)
print('Cantidad de mujeres fumadoras:', cantidad_mujeres_fumadoras)

# He intentado hacer que esta version del codigo se complementara con la anterior, sin embargo siempre mostraba error y al final tuve que hacerlo asi



