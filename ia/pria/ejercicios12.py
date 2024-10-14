import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

COLORES = np.array(['blue','green','red','cyan','magenta','yellow','black','white'])

def ejercicio1():
    arrX = np.random.randint(1,100, size = 100)
    arrY = np.random.randint(1,100, size = 100)
    color = np.random.randint(1,100, size = 100)
    tam = np.random.randint(1,50, size = 100) *10
    plt.figure(figsize=(10,10))
    plt.title('100 puntos aleatorios')
    plt.scatter(x = arrX, y = arrY, c = color, cmap='inferno', 
                s=tam, alpha = 0.5)
    plt.show()
    menu()


def ejercicio2():
    print('Introduce color rgb(255,255,255)\nNumeros entre 0 y 255 separados por comas')
    resp = input()
    arrAux = resp.split(',')
    rgb = (int(arrAux[0]),int(arrAux[1]),int(arrAux[2]))
    colorHexadecimal = '#{:02x}{:02x}{:02x}'.format(*rgb)
    print('rgb: ',rgb,'  hexadecimal: ',colorHexadecimal)
    menu()


def f1(x):
    return np.sin(x)/x
def f2(x):
    return 2 * np.sin(x)/x
def f3(x):
    return -1 * np.sin(x)/x


def ejercicio3():
    arrX = np.linspace(-5*np.pi, 5*np.pi, 100)
    plt.figure(figsize=(8.0,6.0))
    
    #funcion sin(x)/x
    plt.plot(arrX, f1(arrX), c='#f06741',label='sin(x)/x')
    #funcion 2sin(x)/x
    plt.plot(arrX, f2(arrX) , c='#a4f041', label='2sin(x)/x')
    #funcion -sin(x)/x
    plt.plot(arrX, f3(arrX) , c='#8d41f0', label='-sin(x)/x')
    plt.legend(title='Funciones')
    plt.show()
    menu()


def ejercicio4():
    fig = plt.figure(figsize=(10,5))
    arrX = np.linspace(-5*np.pi, 5*np.pi, 100)
    x1 = fig.add_subplot(311)
    x1.plot(arrX, f1(arrX), c='#f06741',label='sin(x)/x')
    #funcion 2sin(x)/x
    x2 = fig.add_subplot(312)
    x2.plot(arrX, f2(arrX) , c='#a4f041', label='2sin(x)/x')
    #funcion -sin(x)/x
    x3 = fig.add_subplot(313)
    x3.plot(arrX, f3(arrX) , c='#8d41f0')
    plt.title('-sin(x)/x')
    plt.show()


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
menu()