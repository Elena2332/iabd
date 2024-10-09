import numpy as np
import pandas as pd

'''
print('\n~~~~~~~~~~ EJERCICIO 1 ~~~~~~~~~~~~\n')
datos = {}
datos['x'] = np.random.randint(-20,50, size = 15)
datos['y'] = np.random.randint(-20,50, size = 15)
points = pd.DataFrame(data = datos)
print(points)


print('\n~~~~~~~~~~ EJERCICIO 2 ~~~~~~~~~~~~\n')
columnaX = points['x']
for num in columnaX:
    if num>= 0:
        print(num)



print('\n~~~~~~~~~~ EJERCICIO 3 ~~~~~~~~~~~~\n')
for fila in points.itertuples():
    if fila[2]<0:
        print('Index {}: {}'.format(fila[0],fila[2]))



print('\n~~~~~~~~~~ EJERCICIO 4 ~~~~~~~~~~~~\n')
primerC = points[(points['y']>=0) & (points['x']>=0)]
print(primerC)



print('\n~~~~~~~~~~ EJERCICIO 5 ~~~~~~~~~~~~\n')
for index,fila in points.iterrows():
    x = fila['x']
    y = fila['y']
    if x >= 0 and y >=0:
        print('El punto({},{}) si pertenece al primer cuadrante'.format(x,y))
    else:
        print('El punto({},{}) no pertenece al primer cuadrante'.format(x,y))



print('\n~~~~~~~~~~ EJERCICIO 6 ~~~~~~~~~~~~\n')
def cantVocales(pal):
    vocales = ['a','A','e','E','i','I','o','O','u','U']
    cont = 0
    for letra in pal:
        if letra in vocales:
            cont += 1
    return cont
    
palabras = ['euro', 'diez', 'algas', 'broma', 'cicuta', 'fatiga', 'nachos', 'jadeos', 'hazañas', 'boutique']
columnas = ['word','length','vowels','consonants']
datos = []
for pal in palabras:
    vocales = cantVocales(pal)
    lon = len(pal)
    datos.append([pal,lon,vocales,(lon-vocales)])
words = pd.DataFrame(data = datos,columns = columnas)
print(words)

# version IRUNE
#    df = pd.DataFrame({
#        'word': words,
#        'length': [len(word) for word in words],
#        'vowels': [sum(1 for char in word.lower() if char in 'aeiou') for word in words],
#        'consonants': [len(word) - sum(1 for char in word.lower() if char in 'aeiou') for word in words]
#    })
#    print (df)



print('\n~~~~~~~~~~ EJERCICIO 7 ~~~~~~~~~~~~\n')
for i,fila in words.iterrows():
    print('La palabra {} tiene {} letras, de las cuales {} son vocales y {} consonantes'
          .format(fila['word'],fila['length'],fila[2],fila[3]))



print('\n~~~~~~~~~~ EJERCICIO 8 ~~~~~~~~~~~~\n')
for i,fila in words.iterrows():
    if fila['vowels'] == fila['consonants']:
        print('{} tiene {} vocales, {} consonantes'.format(fila['word'],fila['vowels'],fila['consonants']))
'''


print('\n~~~~~~~~~~ EJERCICIO 9 ~~~~~~~~~~~~\n')
fotocasa_df = pd.read_csv("https://drive.google.com/uc?export=view&id=1DwvALe87aeDzTk7s6xGPDd6itJ65s4YE", index_col = 0)
print('Numero de filas: ',fotocasa_df.shape[0],
      'Numero de columnas: ',fotocasa_df.shape[1],
      'Numero de valores: ',fotocasa_df.size)



print('\n~~~~~~~~~~ EJERCICIO 10 ~~~~~~~~~~~~\n')
print('Primeros 5: \n',fotocasa_df.head())



print('\n~~~~~~~~~~ EJERCICIO 11 ~~~~~~~~~~~~\n')
print('Ultimos 5: \n',fotocasa_df.tail())
print(fotocasa_df.columns)
#print('Tipos de inmueble de 3 ultimos: \n Inmobiliaria: {} \nTipo: {}'.format(fotocasa_df.tail(3)['Inmobiliaria'],fotocasa_df.tail(3)['Tipo']))



