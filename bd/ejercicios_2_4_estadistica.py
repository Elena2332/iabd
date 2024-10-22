import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as scis

def ejercicio1():
    media = 1.9
    desviacion = 0.1
    menu()



def ejercicio11():
    
    menu()


#### MENU ####
def menu():
    try:
        print('''\nSelecciona Ejercicio
            1 = Ejercicio1
            2 = Ejercicio11
            para TERMINAR cualquier otra cosa''')
        num = int(input())
        if num == 1 : 
            ejercicio1()
        elif num == 11 or num == 2:
            ejercicio11()
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()