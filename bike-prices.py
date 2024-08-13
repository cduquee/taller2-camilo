
# Importar Librerias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df_bike = pd.read_csv('BikePrices.csv')

# Exploarcion de Datos
df_bike.head()

df_bike.shape

df_bike['Brand'].unique()

df_bike["Brand"].value_counts()

df_bike.describe()

# porcentaje de motocicletas de top 5
counts = df_bike.value_counts(df_bike['Brand'])
total = sum(counts)
for i in counts.index[:5]:
  print(f'Porcentaje de {i}: {round(counts.loc[i]/total*100, 2)} %')

# numero de duplicados
duplicates = len(df_bike[df_bike.duplicated()])
print(f'Numero de Registros Duplicados: {duplicates}')

# número de valores perdidos
missing_values = df_bike.isnull().sum().sum()
print(f'Numero de Registros con Valores Nulos: {missing_values}')

# Tipos de datos en el dataset
types = df_bike.dtypes.value_counts()

print('Number of Features: %d'%(df_bike.shape[1]))
print('Number of Customers: %d'%(df_bike.shape[0]))
print('Data Types and Frequency in Dataset:')
print(types)
