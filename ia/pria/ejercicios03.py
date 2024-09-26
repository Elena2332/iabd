from functools import reduce   #para ejercicio6

#####  EJERCICIO 1  #####
def devolverDivisores(num):     #devuelve array con los divisores
    divisores = set()
    for i in range(round(num/2)):  
        i = i+1
        if num%i == 0:
            divisores.add(i)
    divisores.add(num)
    return divisores

def ejercicio1():
    noBien = True
    num = 0
    while noBien:  # pedimos y validamos el numero
        try:
            print('Introduce un numero')
            num = int(input())   
            if num > 0:
                noBien = False   
        except:     # el numero debe ser positivo
            print('que sea un numero entero positivo')
    divisores = devolverDivisores(num)
    print('Divisores de ',num,':',divisores)
    menu()



#####  EJERCICIO 2  #####
def esVocal(letra):   
    vocales = ['a','A','e','E','i','I','o','O','u','U']
    if letra in vocales:
        return True
    else:
        return False

def ejercicio2():
    noBien = True
    letra = ''
    while noBien:
        print('Introduce letra')
        letra = input()
        if len(letra) != 1:
            print('Error en los datos')
        else:
            noBien = False
    if esVocal(letra):
        print(letra,' es vocal')
    else:
        print(letra,' no es vocal')
    menu()



#####  EJERCICIO 3  #####
def cuantaCaracteres(str):   # del ejercicio3
    dicc = {}
    for car in str:
        if car not in dicc.keys():   # aniadir si no esta
            cont = str.count(car)
            dicc[car] = cont
    return dicc

def ejercicio3():
    print('Escribe')
    str = input()
    caracteres = cuantaCaracteres(str)
    if len(caracteres)>0 :
        print(caracteres)
    else:
        print('Nada que mostrar')
    menu()



#####  EJERCICIO 4  #####
def tieneMasVocales(palabra):
    cantVocal = 0
    for letra in palabra:
        if esVocal(letra):   # reutilizo metodo del ejercicio2
            cantVocal = cantVocal+1
    if cantVocal > len(palabra)/2:
        return True
    else:
        return False

def ejercicio4():
    palabras = ['salmon','ana','sos','hada','asd','agua','zombi','palabra','queso']
    lista = list(filter(tieneMasVocales,palabras))
    print(lista)
    menu()



#####  EJERCICIO 5  #####
def cuentaDivisores(num):
    divisores = devolverDivisores(num)  # reutilizo del ejercicio1
    if len(divisores) >= 5:
        return True
    else:
        return False

def ejercicio5():
    numeros = [2,10,100,29,72,400,50,19]
    lista = list(filter(cuentaDivisores,numeros))
    print(lista)
    menu()


#####  EJERCICIO 6  #####
def masLarga(str1,str2):
    if len(str1) > len(str2):
        return str1
    else:
        return str2

def ejercicio6():
    palabras = ['salmon','ana','sos','hada','asd','agua','zombi','palabra','queso']
    palabra = reduce(masLarga,palabras)
    print(palabra)
    menu()


#####  EJERCICIO 7  #####
def tieneMasConsonantes(palabra):  # devuelve 0 si hay mas vocales, si no numero de consonantes
    cantConso = 0
    for letra in palabra:
        if not esVocal(letra):   # reutilizo metodo del ejercicio2
            cantConso = cantConso+1
    if cantConso > len(palabra)/2:
        return [cantConso,palabra]
    else:
        return [0,palabra]
    
def comparaConsonantes(num1,num2):  # num = [n consonantes, palabra]
    if num1[0] > num2[0]:
        return num1
    else:
        return num2

def ejercicio7():
    palabras = ['salmon','ana','sos','hada','asd','agua','zombi','palabra','queso']
    longs = list(map(tieneMasConsonantes, palabras))
    palabra = reduce(comparaConsonantes,longs)  #[len,palabra]
    print(palabra[1],' es la que más consonantes tiene: ',palabra[0],' consonantes')
    menu()



#### MENU ####
def menu():
    try:
        print('''\nSelecciona Ejercicio
            1 = Ejercicio1
            2 = Ejercicio2
            3 = Ejercicio3
            4 = Ejercicio4
            5 = Ejercicio5
            6 = Ejercicio6
            7 = Ejercicio7
            8 = Ejercicio8
            9 = Ejercicio9
            10 = Ejercicio10
            para TERMINAR cualquier otra cosa''')
        num = int(input())
        if num == 1 : 
            ejercicio1()
        elif num == 2:
           ejercicio2()
        elif num == 3:
           ejercicio3()
        elif num == 4:
           ejercicio4()
        elif num == 5:
           ejercicio5()
        elif num == 6:
           ejercicio6()
        elif num == 7:
           ejercicio7()
        #elif num == 8:
        #   ejercicio8()
        #elif num == 9:
        #   ejercicio9() 
        #elif num == 10:
        #   ejercicio10()  
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()