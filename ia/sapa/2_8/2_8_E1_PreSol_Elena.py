import numpy as np
import pandas as pd
import joblib
import os


# cargar el CSV
def cargar_datos():
    datos = {'int_rate':None,'installment':None,'fico':None,'revol_bal':None,'revol_util':None,'inq_last_6mths':None,'pub_rec':None,'purpose':None}
    for nom,dato in datos.items():
        if dato == None:
            noBien = True
            while noBien:
                try:
                    aux = None
                    match nom:
                        case 'int_rate':
                            print('Introduce la tasa de interes (int_rate):  ')
                            aux = float(input()) 
                        case 'installment':
                            print('Introduce cuotas (installment):  ')
                            aux = float(input()) 
                        case 'fico':
                            print('Introduce fico:  ')
                            aux = int(input()) 
                        case 'revol_bal':
                            print('Introduce saldo rotativo del prestatario (revol_bal):  ')
                            aux = int(input()) 
                        case 'revol_util':
                            print('Introduce tasa de utilizacion de linea d credito (revol_util):  ')
                            aux = float(input()) 
                        case 'inq_last_6mths':
                            print('Introduce numero de consultas de acreedores (inq_last_6mths):  ')
                            aux = int(input())  
                        case 'pub_rec':
                            print('Introduce numero de registros publicos despectivos (pub_rec):  ')
                            aux = int(input()) 
                        case _:
                            print('Introduce proposito del prestamo:  ')
                            aux = input() 
                    if aux != None:
                        datos[nom] = aux
                        noBien = False
                except Exception as e:
                    print(e)
                    print('Error el valor introducido no es valido para {}. '.format(nom))
            
    return datos


# cargar el modelo, devuelve None en caso de error
def cargar_modelo():
    ruta = './2_8_E1_Elena.pkl'
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
# cargar datos
datos = cargar_datos()
df = pd.DataFrame(data = [datos.values()], columns=datos.keys())

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
