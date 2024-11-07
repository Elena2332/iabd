import pandas as pd
import numpy as np
import joblib
import os


def cargarCSV():
    ruta = input('Introduce ruta del archivo csv')
    #comprobar que el csv existe
    if os.path.exists(ruta):
        df = pd.read_csv(ruta)
        return df
    else:
        return None


