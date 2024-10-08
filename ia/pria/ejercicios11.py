import numpy as np
import pandas as pd

def ejercicio1():
    datos = {}
    datos['x'] = np.random.randint(50, size = 15)
    datos['y'] = np.random.randint(50, size = 15)
    df = pd.DataFrame(data = datos)
    print(df)
    menu()


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
def ejercicio10():
    print('Sin hacer aun')
def ejercicio11():
    print('Sin hacer aun')
def ejercicio12():
    print('Sin hacer aun')
def ejercicio13():
    print('Sin hacer aun')
def ejercicio14():
    print('Sin hacer aun')
def ejercicio15():
    print('Sin hacer aun')
def ejercicio16():
    print('Sin hacer aun')
def ejercicio17():
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
            10 = Ejercicio10
            10 = Ejercicio11
            10 = Ejercicio12
            10 = Ejercicio13
            10 = Ejercicio14
            10 = Ejercicio15
            10 = Ejercicio16
            10 = Ejercicio17
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
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()