import pandas as pd
import os
import time


# Carga la información del fichero en un dataframe de pandas
ruta_csv='./bd/hadoop/ignore/2018.csv'
df = pd.read_csv(ruta_csv)

# Muestra las primeras líneas del dataframe
print(df.head())

# Guarda la información en un fichero parquet
ruta_parquet = './bd/hadoop/ignore/df.parquet.gzip'
tiempoIni = time.time()
df.to_parquet(ruta_parquet,compression='gzip')
tiempoFin = time.time()-tiempoIni
tamano = os.stat(ruta_parquet).st_size

# Carga la información del fichero parquet en un dataframe de pandas
df_parquet = pd.read_parquet(ruta_parquet)

# Muestra las primeras líneas del dataframe del punto anterior
print(df_parquet.head())

# Muestra el tamaño del archivo parquet y el tiempo que se ha tardado en crear el archivo
print("Tiempo de creacion del archivo parquet:",tiempoFin)
print("Tamaño del archivo parquet(Bytes):",tamano)

