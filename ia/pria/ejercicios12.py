import numpy as np

def ejercicio1():
    arr = np.zeros_like()
    print(arr)
def ejercicio2():
    print('Sin hacer aun')
def ejercicio3():
    print('Sin hacer aun')
def ejercicio4():
    print('Sin hacer aun')
def ejercicio5():
    print('Sin hacer aun')
def ejercicio6():
    print('Sin hacer aun')
def ejercicio7():
    print('Sin hacer aun')
def ejercicio8():
    print('Sin hacer aun')
def ejercicio9():
    print('Sin hacer aun')





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
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()