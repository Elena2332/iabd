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
    for fila in matriz:
        strFila = ''
        for celda in fila:
            strFila = strFila+' '+str(celda)
        print(strFila+'\n')

@staticmethod
def verDiccionario(dicc):
    print(dicc.keys())
    for clave in dicc.keys():
        strFila = str(clave)+':'
        try:        # si no es lista salta excepcion
            for valor in dicc[clave]:
                strFila = strFila+'\n\t'+str(valor)
        except:
            strFila = strFila+'\n\t'+str(dicc[clave])
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



#####  EJERCICIO 12  #####
def ejercicio12():
    noBien = True
    while noBien:  # pedimos y validamos cuantas palabras
        print('Cuantas palabras van a ser?')
        num = math.floor(float(input()))    #truncamos para evitar decimales
        if num < 0:
            print('Numeros positivos por favor')
        else:
            noBien = False
    vocales = ['a','A','e','E','i','I','o','O','u','U']
    dicc = {}
    for i in range(num):   #recogemos y almacenamos las palabras
        print('Introduce palabra')
        palabra = input()
        cantVocales = 0
        for letra in palabra:
            if letra in vocales :
                cantVocales = cantVocales+1
        dicc[palabra] = cantVocales
    verDiccionario(dicc)
    menu()


#####  EJERCICIO 13  #####
def ejercicio13():
    noBien = True
    num = 0
    while noBien:  # pedimos y validamos el numero
        try:
            print('Introduce un numero')
            num = int(input())  
            noBien = False
        except:
            print('numero entero')
    divisores = set()
    for i in range(round(num/2)):  
        i = i+1
        if num%i == 0:
            divisores.add(i)
    divisores.add(num)
    print('Divisores de ',num,':',divisores)
    menu()


#####  EJERCICIO 14  #####
def ejercicio14():
    conjunto={-2,-15,1,6,9,-50,100,200,10,20,5}
    itemAux = 999999
    for item in conjunto:
        if item<itemAux:
            itemAux = item
    print(itemAux)


#####  EJERCICIO 15  #####
def ejercicio15():
    conjunto={'0','*','a','A','z'}
    itemAux = 0
    for item in conjunto:
        print(item,'=',ord(item))  
        if ord(item)>itemAux:
            itemAux = ord(item)
    print(chr(itemAux))
    menu()


#####  EJERCICIO 16  #####
def ejercicio16():
    conjunto = set()
    print('Introduce una frase')
    frase = input()
    noBien = False
    palabras = frase.split(' ')
    for palabra in palabras:
        if palabra[0].isalpha() :
            conjunto.add(palabra[0].lower())
        else:
            noBien = True
            break
    if noBien:
        print('Error en los datos. Intentalo de nuevo')
    else:
        print(conjunto)
    menu()


#####  EJERCICIO 17  #####
def ejercicio17():
    noBien = True
    while noBien:
        try:
            print('Cuantos numeros vas a introducir?')
            cantNum = int(input())
            for i in range(cantNum):
                print('Introduce numero')
                num = int(input())
                if num%2 == 0:   # par
                    t = num, 'es par'
                else:
                    t = num, 'es impar'
                print(t)
            noBien = False
        except:
            print('error en los datos')
    menu()



#####  EJERCICIO 18  #####
def ejercicio18():
    print('Introduce una frase')
    frase = input()
    palabras = frase.split(' ')   #lista de palabras
    contenidoTupla = []
    i = 0
    for palabra in palabras:
        contenidoTupla.append([palabra,len(palabra),palabra[0],i])
        i = i+1
    tupla = tuple(contenidoTupla)
    print(tupla)
    menu()


#####  EJERCICIO 19  #####
def ejercicio19():
    seguir = True
    contenidoTupla = []
    while seguir:
        print('introduce palabra')
        palabra = input()
        if palabra == '':    #Terminamos
            seguir = False
        else:
            contenidoTupla.append(palabra)
    tupla = tuple(contenidoTupla)
    palI,*pals,palF = tupla
    print('primera palabra: ',palI,'\nultima palabra: ',palF)
    menu()


#####  EJERCICIO 20  #####
def ejercicio20():
    lista = ['salmon','sos','asd','zombi','palabra']
    longitudes = []
    for pal in lista:
        longitudes.append(len(pal))
    tupla = dict(zip(lista,longitudes))
    print(tupla)
    menu()


#####  EJERCICIO 21  #####
def ejercicio21():
    num1 = 1
    num2 = 1
    noBien = True
    while noBien:
        try:
            print('Introduce un entero')
            num1 = int(input())
            print('Introduce otro entero')
            num2 = int(input())
            if num1 >= num2:
                noBien = False
            else:
                print('error en los datos')
        except:
            print('error en los datos')
    tupla = num1, num2, num1/num2, num1%num2
    print(tupla) 
    menu()


#####  EJERCICIO 22  #####
def ejercicio22():
    num = 1
    lista = []
    seguir = True
    while seguir:
        noBien = True
        while noBien:
            try:
                print('Introduce un entero')
                num = int(input())
                if num >=1 or num<=360 :
                    noBien = False
                else:
                    print('error en los datos')
            except:
                print('error en los datos')
        numRad = round(num*math.pi/180, 2)
        lista.append(tuple([num,numRad]))
        #para terminar
        print('si quieres continuar introduce s')
        resp = input()
        if resp != 's':
            seguir = False
    print(lista)
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
            11 = Ejercicio11
            12 = Ejercicio12
            13 = Ejercicio13
            14 = Ejercicio14
            15 = Ejercicio15
            16 = Ejercicio16
            17 = Ejercicio17
            18 = Ejercicio18
            19 = Ejercicio19
            20 = Ejercicio20
            21 = Ejercicio21
            22 = Ejercicio22
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
        elif num == 12:
            ejercicio12()  
        elif num == 13:
            ejercicio13()  
        elif num == 14:
            ejercicio14()  
        elif num == 15:
            ejercicio15() 
        elif num == 16:
            ejercicio16()  
        elif num == 17:
            ejercicio17()  
        elif num == 18:
            ejercicio18()  
        elif num == 19:
            ejercicio19()  
        elif num == 20:
            ejercicio20()  
        elif num == 21:
            ejercicio21()  
        elif num == 22:
            ejercicio22()  
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()