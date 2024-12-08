import numpy as np
import pandas as pd

#######  NUMPY  ########
# crear array
arr = []
np_arr = np.array(arr)   # Se puede con listas, tuplas
np_arr = np.arange(10)   # array de [0-9) len:10
np_arr = np.arange(10, 100, 10)  # [10,100) paso 10
np_arr.copy()  # copia

# shape
np_arr.ndim  # dimension, cantidad de arrays anidados ej:[ [],[] ] ndim=2 
np_arr.shape  # tupla con shape ej:(3,3,1)
np_arr.reshape(3,3,1)  # cambia el shape por el parentesis. Si no encaja con el len, peta

# acceso a valores
np_arr[0]  # posicion 0
np_arr[1:2:3]  # 1=inicio, 2=fin(No incluido), 3=paso
np_arr[::-1]  # array al reves
np_arr[:2]  # primeros 2 valores
np_arr[2:]  # de posicion 2(No incluido) al final

np_arr[np_arr>0]  # array de valores que cumplan la condicion
np.where(np_arr>0)  # array de posiciones que cumplen

for i in np.nditer(np_arr):  # saca todos los valores aunque haya mas arrays
    break
for index, i in np.ndenumerate(np_arr):  # index ej:(1,1,3)
  print("Índice:", index,"Elemento:", i)

# funciones
np.sort(np_arr)  # ordena
np.concatenate(np_arr,np_arr, axis=0)  # axis indica la dimension
a,b,c = np.split(np_arr, 3, axis=0)  # 3: partes en las que dividir, axis = modo de division (0= Vertical, 1= Horizontal)

np.random.randint(0, 10, size=10)  # 0:inicio(opcional), 10:fin, size: puede ser un shape
np.random.choice(np_arr, size=10)  # valor aleatorio del array, size:puede ser shape

np.round(np_arr, 3) 
np.trunc()
np.ceil()

np.sum(np_arr) # suma elemento de un array
np.prod(np_arr) # producto elementos de un array

np.add(np_arr, np_arr)  # suma arrays por posiciones
np.subtract(np_arr, np_arr)  # reta
np.divide(np_arr, np_arr)  # divide
np.divmod(np_arr, np_arr)  # divide, devuelve 2 tuplas cociente y resto
np.power(np_arr, np_arr)  # primero elevado al segundo

np_fun = np.frompyfunc(funcion, 1, 2)  # funcion: funcion que se ejecuta para cada valor, 1:parametros, 2:returns
np_fun(np_arr)

# matrices
M = np.matrix([[1, 0, -3, 2], [2, 0, 1, 1], [-1, 0, -1, 0]])
matrixSum = M + M   # mismo shape 
M.dot(M)  # multiplicar o producto matricial




#######  PANDAS  ########
# crear
datos = {}
df = pd.DataFrame(data=datos)
pd.DataFrame(data=datos, index =['id_fila1','id_fila2'])
pd.DataFrame(data=[[1,2],[1,2]], columns=['x','y'])  # data: lista de listas o resultado de zip()
df.copy()

# acceso valores
df.add()  # aniadir
df.columns  # array nombre de columnas
df['']  # valores de una columna Serie
df.loc['']  # nombres de columnas
df.iloc[0]  # indices columnas
df[df.loc['c1':'c3']]  # columnas desde c1 a c3
df[df.iloc[1:3]]  # desde la primera columna a la tercera


# metodos
df.head()  # 5 primeras
df.tail()  # 5 ultimas
df.rank(ascending=True)  # ranking, ascending ordena(opcional)
df.nunique()  # conteo valores unicos por columna
df.drop_duplicates(subset='nom_col', keep=False)  # keep first: primero unico reto duplicados, last, false:todos duplicados

df.insert(loc=3, column='nom_col', value=['v1','v2'])  # inserta columna con valores, loc:posicion(si ya existe el resto se mueven a la derch)
df.insert(3, 'nom_col', 'a')  # 3: loc, 'a' es el valor para todas las filas

df.drop(labels=['c1'], axis=1)  # axis: 0-fila 1-columna, labels: lo que se borra



