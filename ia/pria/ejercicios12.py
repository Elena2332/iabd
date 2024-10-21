import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx


def ejercicio1():
    arrX = np.random.randint(1,100, size = 100)
    arrY = np.random.randint(1,100, size = 100)
    color = np.random.randint(1,100, size = 100)
    tam = np.random.randint(1,50, size = 100) *10
    plt.figure(figsize=(10,10))
    plt.title('100 puntos aleatorios')
    plt.scatter(x = arrX, y = arrY, c = color, cmap='hsv', 
                s=tam, alpha = 0.5)
    plt.colorbar()
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

    x1 = fig.add_subplot(331)
    x1.plot(arrX, f1(arrX), c='#f06741')
    x1.set_title('sin(x)/x')

    #funcion 2sin(x)/x
    x2 = fig.add_subplot(332)
    x2.plot(arrX, f2(arrX) , c='#a4f041')
    x2.set_title('2sin(x)/x')

    #funcion -sin(x)/x
    x3 = fig.add_subplot(333)
    x3.plot(arrX, f3(arrX) , c='#8d41f0')
    x3.set_title('-sin(x)/x')
    plt.show()
    menu()
    

def ejercicio5():
    options = ["Suspenso", "Aprobado", "Notable", "Excelente"]
    count = [20, 10, 45, 25]
    colors = ["#ff2667", "#ff7226", "#26a8ff", "#67ff26"]
    plt.pie(count,colors=colors,labels=options)
    plt.show()
    menu()



def ejercicio6():
    G = nx.Graph()
    G.add_nodes_from("abcde")
    G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), 
                               ("a", "d", 2), ("a", "e", 5), 
                               ("b", "e", 4), ("c", "d", 3), 
                               ("d", "e", 1)])
    #print('Nodos: ',G.nodes,'Aristas: ',G.edges)
    fig, ax = plt.subplots()
    nx.draw(G, ax=ax, with_labels=True, 
            node_color='#ad80fa', font_weight='bold', font_color='#ffffff',
            edge_color='#b1ddf5')
    plt.show()
    menu()

def ejercicio7():
    G = nx.Graph()
    G.add_nodes_from("abcde")
    G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), 
                               ("a", "d", 2), ("a", "e", 5), 
                               ("b", "e", 4), ("c", "d", 3), 
                               ("d", "e", 1)])
    #print('Nodos: ',G.nodes,'Aristas: ',G.edges)
    fig, ax = plt.subplots()
    plt.figure=fig.set_size_inches(8,6)
    nx.draw(G, ax=ax, with_labels=True, 
            node_color='#ad80fa', node_size=350,
            font_weight='bold', font_color='#ffffff',
            edge_color='#b1ddf5')
    plt.show()
    menu()


def ejercicio8():
    G = nx.Graph()
    G.add_nodes_from("abcde")
    G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), 
                               ("a", "d", 2), ("a", "e", 5), 
                               ("b", "e", 4), ("c", "d", 3), 
                               ("d", "e", 1)])
    aristasData = G.edges.data()
    pesosArista = []
    for arista in aristasData:
        pesosArista.append(arista[2]['weight'])
    fig, ax = plt.subplots()
    plt.figure=fig.set_size_inches(8,6)
    nx.draw(G, ax=ax, with_labels=True, 
            node_color='#ad80fa', node_size=350,
            font_weight='bold', font_color='#ffffff',
            edge_color='#b1ddf5',width=pesosArista)
    plt.show()
    menu()


    
def ejercicio9():
    plt.figure(figsize=(10,8))
    plt.text(0.2, 0.8, 'LA', fontsize=50, rotation=25, 
             ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', fc='#242fff', ec='#242fff', alpha=0.7))
    
    plt.text(0.5, 0.55, 'AVENTURA', fontsize=50, rotation=-15, 
             ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', fc='#8a24ff', ec='#8a24ff', alpha=0.7))
    
    plt.text(0.8, 0.3, 'SIGUE', fontsize=50, rotation=10, 
             ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', fc='#24fff4', ec='#24fff4', alpha=0.7))
    plt.show()
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
    except:
        print('Adios')
menu()