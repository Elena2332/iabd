import numpy as np
import pandas as pd
import joblib
import os
from sklearn.impute import SimpleImputer

# metodos pipeline
def familia_name(function_transformer, feature_names_in):
     return ['familia']
def familia_fusion(X):
     # X['sibsp'].fillna(X['sibsp'].mode()[0], inplace=True) 
     # X['parch'].fillna(X['parch'].mode()[0], inplace=True) 
     X=pd.DataFrame(X,columns=['parch','sibsp'])
     X['familia'] = X['sibsp'] + X['parch'] 
     #X=X.drop(['sibsp','parch'],axis=1)
     return X['familia'].values.reshape(-1,1)

def age_name(function_transformer, feature_names_in):
     return ['age']
def separar_age(X):
     X=pd.DataFrame(X,columns=['age'])
     X['age'] = pd.cut(X['age'], bins=[-1,16,32,48,64,np.inf], labels=[1,2,3,4,5]).to_numpy().reshape(-1,1)  #labels no admite str
     #X=X.drop('age',axis=1)  #sobra
     return X

def sex_name(function_transformer, feature_names_in):
     return ['sex']
def pasar_sex(X):
     return np.where(X == 'female',1,0)



# cargar el CSV
def cargar_csv():
    noBien=True
    while noBien:
        ruta = input('Introduce ruta del CSV ')
        if os.path.isfile(ruta):
            try:
                df = pd.read_csv(ruta)
                # quitamos survived si esta
                if 'survived' in df.columns:
                    df.drop(labels=['survived'], axis=1)
            except Exception as e:
                print('Error al cargar el archivo: ', e)
            noBien = False
        else:
            print('Archivo inexistente, comprueba la ruta: ',ruta)
    return df


# cargar el modelo, devuelve None en caso de error
def cargar_modelo():
    ruta = input('Introduce ruta del modelo (archivo.pkl)')
    if os.path.isfile(ruta):
        try:
            modelo = joblib.load(ruta)
            return modelo
        except Exception as e:
            print('Error al cargar el modelo: ',e)
            return None
    else:
        print('Modelo inexiste, comprueba la ruta: ',ruta)
        return None


# hacer la predicción, devuelve None en caso de error
def predecir(modelo, df):
    try:
        prediciones = modelo.predict(df)
        return prediciones
    except Exception :
        return None





#####  MAIN  #####
# cargar del CSV
df = cargar_csv()

# cargar el modelo
modelo = cargar_modelo()

# predecir si el modelo no es None
if modelo is not None:
    predicciones = predecir(modelo, df)
    if predicciones is not None:    # Mostrar las predicciones
        df['predicciones'] = predicciones
        print('Predicciones realizadas:\n', df[['predicciones']])
    else:
        print('Error al hacer las predicciones.')

