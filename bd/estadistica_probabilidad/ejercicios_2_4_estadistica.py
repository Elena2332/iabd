import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

def ejercicio1():
    media = 1.9
    desviacion = 0.1
    prob_mas_2m = stats.norm.cdf(2, media, desviacion)
    prob_menos_1_85m = stats.norm.cdf(1.85, media, desviacion)
    #prob_mas_2m = stats.norm.cdf(2, media, desviacion)
    
    print('1.Probabilidad de medir más de 2m: ',prob_mas_2m)
    print('2.Probabilidad de medir menos de 1.85m: ',prob_menos_1_85m)
    menu()



def ejercicio2():
    
    menu()


#### MENU ####
def menu():
    try:
        print('''\nSelecciona Ejercicio
            1 = Ejercicio1
            2 = Ejercicio2
            para TERMINAR cualquier otra cosa''')
        num = int(input())
        if num == 1 : 
            ejercicio1()
        elif num == 2:
            ejercicio2()
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()