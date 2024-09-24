import math

@staticmethod
def listaAcadena(cadena):
    str = ''
    for cad in cadena:
        str = str+cad
    return(str)

@staticmethod
def cadenaAlista(str):
    cadena = []
    for letra in str:
        cadena.append(letra)
    return cadena

@staticmethod
def verMatriz(matriz):
    i = 0   # filas 
    for fila in matriz:
        strFila = ''
        for celda in fila:
            strFila = strFila+' '+str(celda)
        print(strFila+'\n')

   

#####  EJERCICIO 1  #####
def ejercicio1():
    print('Escribe lo que quieras')
    str = input()
    cadena = cadenaAlista(str)
    cadena.reverse()
    str = listaAcadena(cadena) 
    print(str)
    menu()


#####  EJERCICIO 2  #####
def ejercicio2():
    noBien = True
    cadena1 = ''
    cadena2 = ''
    while noBien :
        print('Introduce la primera cadena')
        cadena1 = input()
        print('introduce la segunda cadena')
        cadena2 = input()
        if len(cadena1) != len(cadena2):
            print('Ambas cadenas deben tener la misma longitud')
        else:
            noBien = False
    mezclaCadenas = []
    for i in range(len(cadena1)):
        mezclaCadenas.append(cadena1[i])
        mezclaCadenas.append(cadena2[i])
    cadenaFinal = listaAcadena(mezclaCadenas)
    print(cadenaFinal)



#####  EJERCICIO 3  #####
def ejercicio3():
    print('Escribe lo que quieras')
    str = input()
    consonantes = []
    vocales = ['a','A','e','E','i','I','o','O','u','U']
    for letra in str:
        if letra not in vocales :
            consonantes.append(letra)
    if len(consonantes) == 0:
        print('No hay consonantes')
    else:
        print(listaAcadena(consonantes))
    menu()



#####  EJERCICIO 4  #####
def ejercicio4():
    print('Introduce una palabra para conprobar si es palindromo')
    palabra = input()
    str.lower(palabra)
    cantLetras = len(palabra)
    for i in range(math.floor(cantLetras/2)):
        print(i,'  ',palabra[i] ,'  ', palabra[cantLetras-i-1])
        if palabra[i] != palabra[cantLetras-i-1] :
            print('No es palindromo')
            break
    menu()
    # PREGUNTAR sobre la lista del enunciado



#####  EJERCICIO 5  #####
def ejercicio5():
    n = 0
    noBien = True
    while noBien:
        try:
            print('Introduce n')
            n = int(input())
            noBien = False
        except:
            print('Un numero entero melon')
    matriz = []
    i=0
    while i < n*n:
        fila = []        
        for j in range(n):
            fila.append(i)
            i = i+1
        # print(fila)
        matriz.append(fila)
    verMatriz(matriz)
    


#####  EJERCICIO 6  #####
def ejercicio6():
    # Crear matriz
    n = 0
    m = 0
    noBien = True
    while noBien:
        try:
            print('Introduce n (filas)')
            n = int(input())
            print('Introduce m (columnas)')
            m = int(input())
            noBien = False
        except:
            print('Numero enteros, no me sea cochino')
    matriz = []
    i=0
    while i < n:
        j=0
        fila = []        
        while j < m :
            print('Introduce el numero [',i,'][',j,']')
            num = int(input())
            fila.append(num)
            j=j+1
        i=i+1        
        matriz.append(fila)
    verMatriz(matriz)
    # sumas
    suma = 0
    sumaAux = 'a'
    esIgual = True
    j = 0
    while j < m:   #recorer matriz por columnas
        i = 0
        suma = 0
        while i< n :
            suma = suma + matriz[i][j]
            i = i+1
        print('Suma columna ',j+1,'=',suma)
        #print('sumaAux = ',sumaAux)
        if sumaAux == 'a':   #entra solo la primera vez
            sumaAux = suma
        elif suma != sumaAux:  # si la suma es diferente
            esIgual = False
            break
        j = j+1
    if not esIgual :
        print('Las sumas de las columnas son distintas')
    else:
        print('La suma de todas las columnas es igual: ',suma)
    menu()



#####  EJERCICIO 7  #####
def ejercicio7():
    # crear matriz
    n = 0
    m = 0
    noBien = True
    while noBien:
        try:
            print('Introduce n (filas)')
            n = int(input())
            print('Introduce m (columnas)')
            m = int(input())
            noBien = False
        except:
            print('Numero enteros, no me sea cochino')
    matriz = []
    i=0
    while i < n:
        j=0
        fila = []        
        while j < m :
            print('Introduce el numero [',i,'][',j,']')
            num = int(input())
            fila.append(num)
            j=j+1
        i=i+1        
        matriz.append(fila)
    ## crear la traspuesta
    traspuesta = []
    i=0
    j=0 
    while j < m:   # recorro la matriz por columnas para ir transformandolas en filas
        i = 0
        fila = []
        while i < n:
            fila.append(matriz[i][j])
            i = i+1
        traspuesta.append(fila)
        j = j+1
    verMatriz(matriz)
    verMatriz(traspuesta)
    menu()


#####  EJERCICIO 8  #####
def ejercicio8():
    noBien = True
    num = 0
    while noBien:
        try:
            print('Introduce un numero entero positivo')
            num = int(input())
            if num >= 0:
                noBien = False
        except:
            print('Numero entero y positivo porfi')
    # crear diccionario
    listaAux = []
    while num != 1:
        fila = [num, num*num*num]   #clave = num  :  valor = num³
        listaAux.append(fila)
        if num == 0:   # 0 tambien es numero entero positivo
            num = num +1
        else:
            num = num -1
    listaAux.append([1,1])
    dicc = dict(listaAux)
    print(dicc)
    menu()



#####  EJERCICIO 9  #####
def ejercicio9():
    noBien = True
    while noBien:
        try:
            print('Introduce nombre')
            nombre = input()
            print('Introduce edad')
            edad = int(input())
            print('Introduce telefono')
            telf = input()
            if edad < 0:  # si, admitimos recien nacidos
                print('La edad no puede ser negativa')
            if len(telf) != 9:
                print('Un telefono debe tiene 9 digitos')
            telf = float(telf)
            noBien = False
        except:
            print('Error al introducir los datos')
    persona = {"name": nombre,
        "edad": edad,
        "telefono": telf}
    print(persona.get("name"),' tiene ',persona.get('edad'),' años y su número de teléfono es ',persona.get('telefono'))
    menu()


#####  EJERCICIO 10  #####
def ejercicio10():
    seguir = True
    cesta = {}
    while seguir:
        print('Introduce nombre del articulo (0 = TERMINAR)')
        nombre = input()
        precio = 0
        if nombre == '0':   #terminar
            seguir = False
        else:               #pedir datos y anadir al diccionario
            noBien = True
            while noBien:   #recoger los datos y validarlos
                try: 
                    print('Introduce precio')
                    precio = float(input())
                    if precio >= 0:
                        noBien = False
                    else:
                        print('No admitimos precios negativos')
                except:
                    print('El precio es un numero positivo')
            
            #comprobar que no se ha introducido ya
            claves = cesta.keys()
            nombre = nombre.lower()
            if nombre not in claves:   # si no esta se aniade
                cesta[nombre] = precio
            else:  
                print('Este articulo ya existe, vale: ',cesta[nombre])
                print('Quieres sobrescribir? (y/n)')
                resp = input().lower()
                if resp == 'y':    #remplazar valor
                    cesta[nombre] = precio
    # mostrar el diccionario
    print('Articulo         Precio')
    total = 0
    for articulo in cesta:
        total = total+cesta[articulo]
        print(articulo,' ---------- ',cesta[articulo])             
    print('Total        ',total)
    menu()


#####  EJERCICIO 11  #####
def ejercicio11():
    alumnos = {}
    seguir = True
    while seguir:
        print('Nombre del alumno')
        nombre = input()
        if len(nombre) > 0:
            notas = []
            seguirNotas = True
            while seguirNotas:     # pedir notas
                try:
                    print('Introduce nota (-1 = Terminar)')
                    num = float(input())
                    if num < -1 or num > 10:
                        print('Nota mal introducida')
                    elif num == -1:
                        seguirNotas = False
                    else:
                        num = round(num,2)
                        notas.append(num)
                except:
                    print('Nota mal introducida')
            alumnos[nombre] = notas
        else:
            seguir = False
    # mostrar lista de alumnos
    for al in alumnos:
        alTxt = al+':'
        total = 0
        for nota in alumnos[al]: 
            total = total+nota
            alTxt = alTxt + '\n\t'+str(nota)
        alTxt = alTxt+'\nMedia: '+str(round(total/len(alumnos[al]),2))
        print(alTxt)






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
        elif num == 8:
            ejercicio8()
        elif num == 9:
            ejercicio9() 
        elif num == 10:
            ejercicio10()  
        elif num == 11:
            ejercicio11()  
        # elif num == 12:
        #     ejercicio12()  
        # elif num == 13:
        #     ejercicio13()  
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()