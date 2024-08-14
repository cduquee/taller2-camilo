
# Importar Librerias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df_bike = pd.read_csv('BikePrices.csv')

# Exploarcion de Datos
print(df_bike.tail())

print(df_bike.shape)

print(df_bike['Brand'].unique())

print(df_bike["Brand"].value_counts())

print(df_bike.describe())

# porcentaje de motocicletas de top 5
counts = df_bike.value_counts(df_bike['Brand'])
for i in counts.index[:5]:
  print(f'Porcentaje de {i}: {round(counts.loc[i]/sum(counts)*100, 2)} %')

# numero de duplicados
duplicates = len(df_bike[df_bike.duplicated()])
print(f'Numero de Registros Duplicados: {duplicates}')

# número de valores perdidos por cada columna
missing_values = df_bike.isnull().sum()
print(f'Numero de Registros con Valores Nulos: {missing_values}')

# Tipos de datos en el dataset
types = df_bike.dtypes.value_counts()

print('Number of Features: %d'%(df_bike.shape[1]))
print('Number of Customers: %d'%(df_bike.shape[0]))
print('Data Types and Frequency in Dataset:')
print(types)

# PreProcesamiento de Datos

# Conversión de características
df_bike['Seller_Type'] = df_bike['Seller_Type'].map({'Individual': 1, 'Dealer': 0})

catcols = df_bike.select_dtypes(exclude = ['int64','float64']).columns
intcols = df_bike.select_dtypes(include = ['int64']).columns
floatcols = df_bike.select_dtypes(include = ['float64']).columns

# codificación 
df_bike = pd.get_dummies(df_bike, columns = catcols)
   
print('New Number of Features: %d'%(df_bike.shape[1]))  