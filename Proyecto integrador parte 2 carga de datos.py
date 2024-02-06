import numpy as np
import csv
from datasets import load_dataset
import pandas as pd




dataset = load_dataset("mstz/heart_failure")
df = pd.DataFrame(dataset['train'])


with open('heart_failure_clinical_records_dataset.csv', 'r') as file:
     csv_reader = csv.reader(file)
     next(csv_reader)
     age = [float(row[0]) for row in csv_reader] 
        
     edades_np = np.array(age)

df['edad_del_csv'] = age

df_perecidos = df[df['is_dead'] == 1]
df_sobrevivientes = df[df['is_dead'] == 0]

promedio_edades_perecidos = df_perecidos['edad_del_csv'].mean()
promedio_edades_sobrevivientes = df_sobrevivientes['edad_del_csv'].mean()

print('Promedio de edades de personas que perecieron :', promedio_edades_perecidos)
print('Promedio de edades de personas que sobrevivieron :', promedio_edades_sobrevivientes)