import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

def ejercicio1():
    media = 1.9
    desviacion = 0.1
    prob_mas_2m = 1 - stats.norm.cdf(2, media, desviacion)
    prob_menos_1_85m = stats.norm.cdf(1.85, media, desviacion)
    prob_entre_2_1_85m = stats.norm.cdf(2, media, desviacion) - prob_menos_1_85m 

    print('1.Probabilidad de medir más de 2m: ',round(prob_mas_2m,3))
    print('2.Probabilidad de medir menos de 1.85m: ',round(prob_menos_1_85m,3))
    print('3.Probabilidad de medir entre 2 y 1.85m: ',round(prob_entre_2_1_85m,3))

    # grafico gráfico de esta distribución normal 
    x= np.linspace(media- 3 * desviacion, media+ 3 * desviacion,100)
    y = stats.norm.pdf(x,media,desviacion)
    plt.figure(figsize=(10,8))
    plt.plot(x, y, label='metros jugador', color='red')
    plt.title('2_4 Ejercicio 1')
    plt.xlabel('metros jugador')
    plt.ylabel('probabilidad')
    plt.show()
    menu()



def ejercicio2():
    media = 3.2
    desviacion = 0.5
    prob_3_5kg = stats.norm.cdf(3.5, media, desviacion)-stats.norm.cdf(3.49, media, desviacion)
    prob_pesar_80_mas = stats.norm.ppf(0.8, media, desviacion) 

    print('1.probabilidad bebé recién nacido pese 3.5 kg: ',round(prob_3_5kg,3))
    print('2.peso mínimo de un recién nacido para que el 80% de los bebés pesen menos: ',round(prob_pesar_80_mas,3))

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