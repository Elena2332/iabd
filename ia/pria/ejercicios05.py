import re 


def ejercicio1():
    txt = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, 
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, 
adarga antigua, rocín flaco y galgo corredor"""
    p = re.compile(r"\s", re.IGNORECASE)
    print(p.split(txt))
    print(p.findall(txt))


def ejercicio2():
    print()
def ejercicio3():
    print()
def ejercicio4():
    print()
def ejercicio5():
    print()
def ejercicio6():
    print()
def ejercicio7():
    print()


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
        print('Adios')
menu()