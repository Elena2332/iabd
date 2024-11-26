import pandas as pd

from sklearn.linear_model import SGDClassifier,LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import LinearSVR
from sklearn.tree import DecisionTreeRegressor

#######  DATOS  #######
df = pd.read_csv('ruta_csv')



### Correlacion
corr_matrix = df.corr(numeric_only=True)
corr_matrix["survived"].sort_values(ascending=False)
corr_matrix.style.background_gradient()

# eliminar segun un valor
target_corr = corr_matrix['survived'].abs()
cols_drop = target_corr[target_corr < 0.4].index.tolist()
df = df.drop(columns = cols_drop)



### Division
train_set, test_set = train_test_split(df, test_size=0.15, random_state=42,
        stratify=df['pclass'])  # para que los diferentes casos de pclass esten balanceados



#######  CLASIFICACION  #######
'Clasificar los datos por tipos. si,no; perro,gato,caracol,colibri...'

# Clasificacion binaria
modelo_sgdClas = SGDClassifier(random_state=42)
modelo_knn = KNeighborsClassifier()
modelo_RL = LogisticRegression()
modelo_svc = SVC(random_state=42)

# Clasificacion multiclase
modelo_RL = LogisticRegression()
modelo_svc = SVC(random_state=42)
modelo_rfc = RandomForestClassifier(random_state=42)
modelo_knn = KNeighborsClassifier()

## Evaluacion
# Datos Balanceados
    # Exactitud: accuracy,  usar cuando las soluciones esten balanceadas(50% si, 50% no) y no son binarios
# Datos Desiguales
    # Precision: proporcion de predicciones positivas correctas. 
    # Sensibilidad:  capacidad para detectar correctamente los aciertos.
    # F1: punto medio entre sensibilidad y precision
    # Matriz confusion: muestra los positivos y negativos, verdaderos y falsos
# Evaluar modelos d clasificacion binaria o de probabilidad
    # Area de roc: Evaluar modelos d clasificacion binaria





#######  REGRESION  #######
'Se usa cuando se quieren predecir numeros continuos'

## Regresion Lineal
modelo_lr = LinearRegression()
modelo_sgdReg = SGDRegressor()

## Regresion polinomial
# para Ridge, Lasso y ElasticNet usar con polynomialFeatures 
poly_features = PolynomialFeatures(degree=30, include_bias=False)
modelo_ridge_reg = Ridge(alpha=1.,random_state=42)  # Si α=0, entonces no hay regularización. Si α es muy grande, los pesos acaban muy cerca de 0 y el resultado es una línea plana que cruza la media de los datos.
modelo_lasso_reg = Lasso(alpha=1.,random_state=42)
modelo_net_reg = ElasticNet(alpha=0.1, l1_ratio=0.5)
pipeline_net = make_pipeline(poly_features, modelo_net_reg)

# SVM se crea una calle en la que encajen todos los datos posibles. epsilo=anchura de calle
svr_reg = LinearSVR(epsilon=0.5, random_state=42)

# Arbol decision
tree_reg2 = DecisionTreeRegressor(max_depth=2, random_state=42)


## Evaluacion
# Error absoluto medio (MAE): media de los errores, deferencia valor real-prediccion
# Error cuadrático medio (MSE): MAE al cuadrado. Penaliza más los errores grandes
# Raiz error cuadratico medio (RMSE): MSE pero en la unidades originales





#######  EVALUACION del MODELO  #######
###  Evaliacion cruzada  ###
'''Divide los datos de entrenamiento en cv partes. Evalua con la parte1 y evalua con el resto, 
evalua con la parte2 y entrena con el resto y asi hasta hacerlo con todas'''
from sklearn.model_selection import cross_val_predict, cross_val_score
# cross_val_predict
    y_train_pred = cross_val_predict(modelo, X_train, y_train, cv=3, method='decision_function')
    # Entrena y genera arrya con predicciones de las muestras
    # cv: cantidad de separaciones
    # scoring: metodo de evaluacion ['accuracy','f1','roc_auc']
    # method: controlar como se genera la prediccion ['predict','predict_proba','decision_function']
        # 'predict': Devuelve las etiquetas o valores predichos (Clasificación y Regresion).
        # 'predict_proba': Devuelve probabilida de la clases predicha(Clasificacion). Útil calcular curvas ROC o métricas basadas en probabilidades 
        # 'decision_fuction': Devuelve puntuaciones de decision(no todos los moselos). Útil calcular curvas ROC
          

# cross_val_score
    y_trian_perd = cross_val_score(modelo, X_train, y_train, cv=3, scoring="accuracy")
    # scoring metodo de evaluacion ['accuracy','f1','roc_auc']


#######  OPTIMIZACION del MODELO  #######

# GridSearchCV y RandomizedSearchCV usan validacion cruzada


