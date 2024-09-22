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
        # elif num == 3:
        #     ejercicio3()
        # elif num == 4:
        #     ejercicio4()
        # elif num == 5:
        #     ejercicio5()
        # elif num == 6:
        #     ejercicio6()
        # elif num == 7:
        #     ejercicio7()
        # elif num == 9:
        #     ejercicio9() 
        # elif num == 10:
        #     ejercicio10()  
        # elif num == 11:
        #     ejercicio11()  
        # elif num == 12:
        #     ejercicio12()  
        # elif num == 13:
        #     ejercicio13()  
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()