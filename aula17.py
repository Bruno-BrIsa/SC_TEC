# Código para mostrar valores ordenados da coluna de temperatura
import pandas as pd

df = pd.read_csv('Ice Cream Sales - temperatures.csv')
temperatures = df['Temperature'].sort_values()
print(temperatures)