import math
import numpy as np

##### EJERCICIO1 #####
def ejercicio1():
    try:
        arr = np.arange(9)
        print('Dimension: ',arr.ndim,'\tShape: ',arr.shape,'\tArray:\n',arr)
        arr = arr.reshape(1,3,3)
        print('Dimension: ',arr.ndim,'\tShape: ',arr.shape,'\tArray:\n',arr)
    except Exception as message:
        print(message)
    menu()

##### EJERCICIO2 #####
def ejercicio2():
    a1 = [[-6, 5], [-4, 3], [-2, 1]] 
    a2 = [[1, 2], [3, 4], [5, 6]]
    arr = np.concatenate((a1,a2),axis=0)
    print('a1: ',a1)
    print('a2: ',a2)
    print('arr: ',arr)
    menu()


##### EJERCICIO3 #####
def esPalindromo(palabra):
    str.lower(palabra)
    cantLetras = len(palabra)
    for i in range(math.floor(cantLetras/2)):
        #print(i,'  ',palabra[i] ,'  ', palabra[cantLetras-i-1])
        if palabra[i] != palabra[cantLetras-i-1] :
            #palabra NO es palindromo
            return [False,palabra]
    return [True,palabra]

def ejercicio3():
    arr = [["ala", "delfín", "arroz"], ["cena", "kayak", "picnic"], ["hoja", "gato", "elle"]]
    esPali = np.frompyfunc(esPalindromo, 1,1)
    for pal in np.nditer(arr):
        for resp in esPali(pal):
            if resp[0]:
                print(resp[1],' ES palindromo')
            else:
                print(resp[1],' No es palindromo')
    menu()


##### EJERCICIO4 #####
def ejercicio4():
    n = np.random.randint(1, 10)
    numIntento = 0
    seguir = True
    while seguir :
        num = 0
        numIntento +=1
        noBien = True
        while noBien:  #validamos que numero entre 1 y10
            print('Introduce numero del 1 al 10')
            num = input()
            try:
                num = int(num)
                if num>=1 and num<=10:
                    noBien = False
                else:
                    raise Exception
            except:
                print('Error al introducir el dato')
        if num == n:
            seguir = False
        else:
            print('¡Has fallado! ¡Prueba otra vez!')
    print('¡¡¡ENHORABUENA!!! Has acertado el número que había pensado: el ',n)
    print('Numero de intentos: ',numIntento)
    menu()


##### EJERCICIO5 #####
def numerosValidos(arr):
    for n in arr:
        try:
            if int(n)<1 or int(n)>20:
                return False
        except:
            return False
    return True

def ejercicio5():
    n = np.random.randint(1,20, size = 5)
    #print('SOLUCION: ',n,'\n')
    numIntento = 0
    seguir = True
    while seguir :
        numeros = []
        numIntento +=1
        noBien = True
        while noBien:  #validamos que entre bien los numeros
            print('Introduce 5 numeros separados por espacios')
            resp = input()
            numeros = resp.split(' ')
            if len(numeros) == 5 and numerosValidos(numeros):
                noBien = False
            else:
                print('Error al introducir los numeros')
        
        bienColocado = 0
        existentes = 0
        pos = 0
        for num in numeros:
            num = int(num)
            if num in n:
                existentes += 1
            if n[pos] == num:
                bienColocado +=1
            pos += 1
        
        if bienColocado == len(n):
            seguir = False
        else:
            print('Has acertado {} de 5 y {} estan en su lugar'.format(existentes,bienColocado))
            print('¡Has fallado! ¡Prueba otra vez!\n')
    print('¡¡¡ENHORABUENA!!! Has acertado el número que había pensado: el ',n)
    print('Numero de intentos: ',numIntento)
    menu()



##### EJERCICIO6 #####
def ejercicio6():
    arr = [-3, -2, -1, 0, 1, 2, 3]
    arr1 = np.random.choice(arr, size = (3,4))
    arr2 = np.random.choice(arr, size = (3,4))
    suma = np.add(arr1,arr2)
    print(arr1,'\n   + \n',arr2,'\n   = \n',suma)
    menu()



##### EJERCICIO7 #####
def ejercicio7():
    arr = np.array([[1, 2, 3],[-1, 0, 1], [4, 5, 6], [-4, 0, 4], [3, 2, 1], [-3, 0, 3]])
    a,b,c = np.split(arr,3,axis=0)
    print('1:\n',a)
    print('2:\n',b)
    print('3:\n',c)
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
        else:
            print('Adios')
    except ValueError:
        print('Formato no valido, Adios')
    except Exception as m:
        print(m)

menu()