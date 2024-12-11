import pandas as pd

# Ruta del archivo Excel
archivo_excel = 'C:/Users/DELL/Documents/python/Prueba1.xlsx'

# Leer el archivo Excel
df = pd.read_excel(archivo_excel)

# Contar filas
num_filas = df.shape[0]

# Contar columnas
num_columnas = df.shape[1]

# Total de registros (filas * columnas)
total_registros = df.size

# Mostrar resultados
print(f"Número de filas: {num_filas}")
print(f"Número de columnas: {num_columnas}")
print(f"Total de registros: {total_registros}")

# Mostrar las primeras filas del DataFrame
print(df.head())

# Descripción de variables:

# El dataset se compone de 13 columnas las cuales tienen información acerca del pago de un crédito,
# (variable de pagado o pendiente), Fecha programada de pago, fecha real de pago, estado de la cuota entre otras.