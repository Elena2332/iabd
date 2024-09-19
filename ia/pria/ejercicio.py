import math  


#####  EJERCICIO 1  #####
def ejercicio1():
    sigue = True
    while sigue :
        try:
            print('\nIntroduce un numero entero')
            num = int(input())
            if num == 0:
                sigue = False
            if sigue:
                if num%2 == 0:
                    print(num,' es par')
                else: 
                    print(num,' no es par')
        except ValueError:
                print('Tiene que ser un numero entero')
    print('Fin ejercicio 1')
    menu()



#####  EJERCICIO 2  #####
def ejercicio2():
    print('Introduce nombre')
    nombre = input()
    cantLetras = len(nombre)
    if cantLetras > 10:
        print(nombre,' tiene más de 10 caracteres')
    elif cantLetras < 10:
        print(nombre, ' tiene menos de 10 letras')
    else:
        print(nombre,' tiene 10 letras')
    menu()



#####  EJERCICIO 3  #####
def ejercicio3():
    noValido = True
    num1 =0
    num2 =0
    while noValido :
        try:
            print('Introduce un numero')
            num1 = int(input())
            print('Introduce otro numero')
            num2 = int(input())
            
            if num2 == 0:  #evitamos que divida por 0
                print('el segundo numero no puede ser 0')
            else:
                noValido = False
        except:
            print('Ambos deben ser numeros enteros')
    if num1 >= num2:
        print('El primer numero ',num1, 'es mayor que el segundo ',num2)
    else:
        print('El segundo ncomo saber si es una letraumero ',num2, 'es mayor que el primer ',num1)

    cociente = num1/num2
    #if cociente - math.floor(cociente) == 0 : #version con libreria
    if cociente - num1//num2 == 0 :  #division exacta
        print('Division exacta ',num1,'/',num2,'=',cociente)
    else:
        print('NO es una division exacta ', num1,'/',num2,'=',cociente,'  Resto=',num1%num2)
    menu()



#####  EJERCICIO 4  #####
def ejercicio4():
    noValido = True
    num1 =0
    num2 =0
    while noValido :
        print('Introduce un numero')
        num1 = int(input())
        print('Introduce otro numero')
        num2 = int(input())
        if num1>=0 and num2>=0:
            noValido=False
        else:
            print('Ambos deben ser positivos')
    if num1 < num2:  # num1 es el mayor
        aux = num1
        num1 = num2
        num2 = aux
    if num2 == 0:
        print('Ningun numero es multiplo de 0')
    elif num1%num2 == 0 :
            print(num1,' es multiplo de ',num2)
    else:
        print(num1,' No es multiplo de ',num2)
    menu()



#####  EJERCICIO 5  #####
def ejercicio5():
    print('Introduce palabra')
    palabra = input()
    primeraLetra = palabra[0]
    if primeraLetra.isalpha():
        if primeraLetra == str.lower(primeraLetra):
            print(palabra,' empieza por minuscula')
        else:
            print(palabra,' empieza en Mayuscula')
    else:
        print('el primer caracter no es una letra')
    menu()



#####  EJERCICIO 6  #####
def ejercicio6():
    noBien = True
    vocales = ['a','e','i','o','u']
    while noBien:
        print('Introduce letra')
        letra = input()
        if len(letra)>1:
            print('Una letra solo')
        else:
            noBien = False
            if str.lower(letra) in vocales:
                print(letra,'es una vocal')
    menu()



#####  EJERCICIO 7  #####
def ejercicio7():
    print('ax² + bx + c = 0')
    noBien =True
    numA = 0
    numB = 0
    numC = 0
    while noBien:
        try:
            print('Introduce valor de a')
            numA = int(input())
            print('Introduce valor de b')
            numB = int(input())
            print('Introduce valor de c')
            numC = int(input())
            noBien = False
        except:
            print('Solo numeros enteros')
    
    raiz = numB*numB - 4*numA*numC
    if raiz>0:
        raiz = math.sqrt(raiz)
        print('raiz = ',raiz)
        x1 = (numB+raiz) / 2*numA
        print('x1 = ',round(x1,2))
        x2 = (numB-raiz) / 2*numA
        print('x2 = ',round(x2,2))
    else:   
        print('La ecuacion no tiene soluciones reales (4ac > b²)')
    menu()


#####  EJERCICIO 9  #####
def ejercicio9():
    cantNueva = float(1)
    cantTotal = float(0)
    while cantNueva != 0 and cantTotal <= 200 :
        print('Introduce cantidad (0 para terminar)')
        cantNueva = float(input())
        cantNueva = math.floor(cantNueva*100)/100  # nos quedamos solo con los dos primeros decimales
        cantTotal = cantTotal + cantNueva
        if cantTotal >200 :
            print('Ha sobrepasado el presupuesto por ',cantTotal-cantNueva,
                  '\nLa cantidad final es ',cantTotal)
        if cantNueva == 0:
            print('El precio final es ',cantTotal)
    menu()



#####  EJERCICIO 10  #####
def ejercicio10():
    num = 1
    positivos = 0
    negativos = 0
    while num != 0:
        print('Introduce numero')
        try:
            num = int(input())
            if num > 0 :
                positivos = positivos+1
            elif num < 0:
                negativos = negativos+1
        except:
            print('El numero debe ser entero')
    print('Recuento: \n Positivos:',positivos,'\n Negativos:',negativos)
    menu()


#####  EJERCICIO 11  #####
def ejercicio11():
    noBien = True
    while noBien:
        print('Introduce primer numero')
        num1 = math.floor(float(input()))
        print('Introduce segundo numero')
        num2 = math.floor(float(input()))
        if num1<num2:
            noBien=False
    num = num1
    suma = 0
    cont = 0
    while num <= num2:
        if num%3 == 0:
            print(num)
            cont = cont+1
            suma = suma+num
        num = num+1
    print('[',num1,',',num2,']\n suma:',suma,'\n media:',suma/cont)
    menu()



#####  EJERCICIO 12  #####
def ejercicio12():
    noBien = True
    while noBien:
        try:
            print('Cuantos numeros vas a introducir?')
            len = int(input())
            noBien = False
        except:
            print('Un numero entero melon')
    numeros = []
    for i in range(len):
        print('Introduce numero')
        numeros.append(float(input()))
    #print(numeros)
    producto = 1
    for num in numeros:
        producto = producto*num 
    print('Producto:',producto)

#####  EJERCICIO 13  #####
def ejercicio13():
    num = 0
    noBien = True
    while noBien:
        try:
            print('Cuantos numeros vas a introducir?')
            num = int(input())
            noBien = False
        except:
            print('Un numero entero melon')
    for i in range(num):
        linea = ''
        for j in range(i+1):   #linea del triangulo
            linea = linea+str(j+i+1)+' '
        for j in range(num-i) :  #espacios en blanco
            linea = linea+' '
        for j in range(num):   #linea cuadrado
            linea = linea+' '+str(j+1)
        print(linea)



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
            11 = Ejercicio11
            12 = Ejercicio12
            13 = Ejercicio13
            para TERMINAR cualquier otra cosa''')
        num = int(input())
        if num == 1 or num==8: #el ejercicio es el mismo
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
        elif num == 9:
            ejercicio9() 
        elif num == 10:
            ejercicio10()  
        elif num == 11:
            ejercicio11()  
        elif num == 12:
            ejercicio12()  
        elif num == 13:
            ejercicio13()  
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()