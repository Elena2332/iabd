import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx

def ejercicio1():
    options = ['1','2','3','4','5','6']
    count = [5,15,20,10,8,2] 
    colores = sns.color_palette("muted", 7)
    total = 0
    porcentajes = []
    for i in range(2):
        for j in count:
            if i == 0: 
                total = total+j
            if i == 1:
                porcentajes.append(round((j/total*100),2))
   
    fig = plt.figure(figsize=(10,5))
    #grafo pastel
    x1 = fig.add_subplot(121)
    x1.pie(count, labels=options, colors = colores, autopct = "%0.2f%%")
    x1.set_title('Apartado B')

    #grafo barras
    x2 = fig.add_subplot(122)
    x2.bar(options, count, color=colores)
    x2.set_title('Apartado C')

    plt.show()
    menu()



def ejercicio11():
    muestra = [9,12,6,11,19,5,8,13,2,8,5,12,0,9,4,15,18,10,6,16]
    valores = {'0-4':0, '5-9':0, '10-14':0, '15-19':0}
    for num in muestra:
        if num in range(5):
            valores['0-4'] += 1
        elif num in range(5,10):
            valores['5-9'] += 1
        elif num in range(10,15):
            valores['10-14'] += 1
        else:
            valores['15-19'] += 1
    plt.bar(valores.keys(),valores.values(), 
            color=["#ff7f7d", "#ffc07d", "#817dff", "#7dff86"])
    plt.xlabel('Intervalos de Puntos')
    plt.ylabel('Cantidad')
    plt.title('Puntos obtenidos por 2 equipos de baloncesto')
    plt.show()
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