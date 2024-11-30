import numpy as np
import pandas as pd
import joblib


# cargar el modelo, devuelve None en caso de error
def cargar_modelo():
    ruta = './2_8_E1_Elena.pkl'
    try:
        modelo = joblib.load(ruta)
        return modelo
    except Exception as e:
        print(e)
        print('Error al cargar el modelo: ',e)
        return None


# cargar datos
def cargar_datos():
    datos = {}
    try:
        print('Introduce si cumple los requisitos para el prestamo (0 no, 1 si) (credit_policy):  ')
        datos['credit.policy'] = float(input()) 
        print('Introduce la tasa de interes (int_rate):  ')
        datos['int.rate'] = float(input()) 
        print('Introduce cuotas (installment):  ')
        datos['installment'] = float(input()) 
        print('Introduce fico:  ')
        datos['fico'] = int(input()) 
        print('Introduce saldo rotativo del prestatario (revol_bal):  ')
        datos['revol.bal'] = int(input()) 
        print('Introduce tasa de utilizacion de linea d credito (revol_util):  ')
        datos['revol.util'] = float(input()) 
        print('Introduce numero de consultas de acreedores (inq_last_6mths):  ')
        datos['inq.last.6mths'] = int(input())  
        print('Introduce numero de registros publicos despectivos (pub_rec):  ')
        datos['pub.rec'] = int(input()) 
        print('Introduce proposito del prestamo:  ')
        datos['purpose'] = input() 
        # print(datos)
        return datos
    except Exception as e:
        print(e)
        print('Error el valor introducido no es valido.')
        return None
    


# hacer la predicción, devuelve None en caso de error
def predecir(modelo, datos):
    try:
        df = pd.DataFrame([datos],columns=['credit.policy', 'int.rate', 'installment', 'fico', 'revol.bal', 'revol.util', 'inq.last.6mths', 'pub.rec', 'purpose'])
        prediciones = modelo.predict(df)
        return prediciones
    except Exception as e:
        print(e)
        return None




#####  MAIN  #####
# cargar el modelo
modelo = cargar_modelo()

# cargar datos
df = cargar_datos()

# predecir si el modelo no es None
if modelo is not None:
    predicciones = predecir(modelo, df)
    if predicciones is not None:    # Mostrar las predicciones
        df['predicciones'] = predicciones
        print('Predicciones realizadas:\n', df['predicciones'])
    else:
        print('Error al hacer las predicciones.')
