import joblib
import pandas as pd
import math

def cargar_modelo():
    try:
        return joblib.load('./2_11_E5_CO2_Elena.pkl')
    except Exception as e:
        print('Error al cargar el modelo\n',e)

def cargar_datos():
    try:
        car = input('Introduce la marca del coche: ')
        model = input('Introduce modelo del coche: ')
        print('Introduce Volume del coche: ')
        vol = int(input().strip())
        print('Introduce Weight del coche: ')
        wei = int(input().strip())
        datos = {'Car':car, 'Model':model,'Volume': math.floor(vol), 'Weight': math.floor(wei)}

        return datos

    except Exception as e:
        print('Error en los datos\n',e)
        return None


# hacer la predicción, devuelve None en caso de error
def predecir(modelo, datos):
    try:
        df = pd.DataFrame([datos], columns=['Car','Model','Volume','Weight'])
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
