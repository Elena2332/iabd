import os 

# variables 
PATH_NAME = './recursos'
FILE3 = '/ej3.txt'
FILE1 = '/ejercicio6_1.txt'


#####  EJERCICIO 1  #####
def ejercicio1():
    print('Introduce:')
    persona = {'nombre':input('Nombre:'),
               'apellido':input('Apellido:'),
               'edad':input('Edad:'),
               'color_favorito':input('Color Favorito:')}
    texto=''
    for clave in persona.keys():
        texto += clave+': '+persona[clave]+'\n'

    if not os.path.exists(PATH_NAME):   #crear carpeta 'recursos' si no existe
        os.mkdir(PATH_NAME)
        print('Carpeta "recursos" creada')

    with open(PATH_NAME+FILE1,'w') as f:    # with cierra el archivo automaticamente hehe
            f.write(texto)
        
    menu()



#####  EJERCICIO 2  #####
def ejercicio2():
    try:
        with open(PATH_NAME+FILE1,'r',encoding='utf-8') as f:    # abrimos modo lectura
            contenido = f.read()
            if len(contenido) < 1:
                print('Fichero vacio')
            else:
                print(contenido)
    except FileNotFoundError:
        print('Error. Comprueba que el fichero exista y la ruta este bien')
    menu()



#####  EJERCICIO 3  #####
def ejercicio3():
    if not os.path.exists(PATH_NAME+FILE3):  #crear el archivo si no existe
        f =  open(PATH_NAME+FILE3,'x')
        f.close()
    else:
        print('Este archivo ya existe')
    menu()



#####  EJERCICIO 4  #####
def ejercicio4():
    try:
        os.remove(PATH_NAME+FILE3)   #eliminamos el archivo
        if not os.path.exists(PATH_NAME+FILE3):   #comprobamos que se ha eliminado
            print('"'+PATH_NAME+FILE3+'" borrado correctamente')
    except FileNotFoundError:
        print('Error. No se puede borrar lo que no existe')
        
    menu()



#####  EJERCICIO 5  #####
def ejercicio5():
    file_name = '/ej5.txt'
    #creamos el archivo vacio si no existe
    if not os.path.exists(PATH_NAME+file_name):
        f =  open(PATH_NAME+file_name,'x')
        f.close()
    else:
        print('"'+PATH_NAME+file_name+'" ya existe')
    
    #escribimos
    lineas = ["x,y,Color,Shape\n","1,1,#6fb7ff,<\n","-1,1,#ffa66f,v\n","-1,-1,#ffee6f,>\n","1,-1,#db6fff,^\n"]
    with open(PATH_NAME+file_name,'a') as f:
        for lin in lineas:
            f.write(lin)
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
        else:
            print('Adios')
    except ValueError:
        print('Adios')
menu()