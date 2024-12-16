import joblib
import pandas as pd
import math

def cargar_modelo():
    try:
        return joblib.load('./Ex1_E1_Elena.pkl')
    except Exception as e:
        print('Error al cargar el modelo\n',e)

def cargar_datos():
    try:
        # sepal length (cm)	sepal width (cm)	petal length (cm)	petal width (cm)
        print('Introduce la Longitud del sepalo: ')
        sepal_len = float(input().strip())
        print('Introduce Anchura del sepalo: ')
        sepal_width = float(input().strip())
        print('Introduce Longitud del petalo: ')
        petal_len = float(input().strip())
        print('Introduce anchura del petalo: ')
        petal_width = float(input().strip())
        datos = {'sepal length (cm)': sepal_len,
            'sepal width (cm)': sepal_width,
            'petal length (cm)': petal_len,
            'petal width (cm)': petal_width}
        # print('DATOS:\t',datos)
        return datos

    except Exception as e:
        print('Error en los datos. Sigue intentandolo\n')
        # print(e)
        return None


# hacer la predicción, devuelve None en caso de error
def predecir(modelo, datos):
    try:
        df = pd.DataFrame([datos], columns=['sepal length (cm)', 'sepal width (cm)', 
                                            'petal length (cm)','petal width (cm)'])
        prediciones = modelo.predict(df)
        return prediciones
    except Exception as e:
        # print(e)
        return None



#####  MAIN  #####
# cargar el modelo
modelo = cargar_modelo()
# predecir si el modelo no es None
if modelo is not None:

    # cargar datos
    df = cargar_datos()
    if df is not None:
        predicciones = predecir(modelo, df)
        if predicciones is not None:    # Mostrar las predicciones
            print('Predicciones realizadas')
            if predicciones == [0]:
                print('Iris del tipo Setosa')
            elif predicciones == [1]:
                print('Iris del tipo Versicolor')
            else:
                print('Iris del tipo Virginica')
        else:
            print('Error al hacer las predicciones.')
