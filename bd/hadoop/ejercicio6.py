import pandas as pd
import numpy as np


# Carga la información del fichero en un dataframe de pandas
ruta_csv='./bd/hadoop/ignore/2018.csv'
df = pd.read_csv(ruta_csv)

# Muestra las primeras líneas del dataframe
print(df.head())

# Guarda la información en un fichero parquet
ruta_parquet = './bd/hadoop/ignore/df.parquet'
parquet = df.to_parquet(ruta_parquet)

# Carga la información del fichero parquet en un dataframe de pandas
df_parquet = pd.read_parquet(ruta_parquet)

# Muestra las primeras líneas del dataframe del punto anterior
print(df_parquet.head())

# Muestra el tamaño del archivo parquet y el tiempo que se ha tardado en crear el archivo


