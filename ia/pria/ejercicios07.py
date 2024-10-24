import pandas as pd
import requests 
from bs4 import BeautifulSoup as Bs


#####  EJERCICIO 1  #####
def ejercicio1():
    menu()



#####  EJERCICIO 2  #####
def ejercicio2():
    ruta = "https://datosabiertos.carm.es/odata/Agricultura/IMIDA_dia_2018.csv"
    pd_datos = pd.read_csv(ruta,
                           header=0,
                           sep=';',
                           decimal=',',
                           quotechar='"',
                           encoding='latin1')
    print(pd_datos.head())
    menu()



#####  EJERCICIO 3  #####
def ejercicio3():
    ruta = "https://cnecovid.isciii.es/covid19/resources/casos_diagnostico_provincia.csv"
    pd_datos = pd.read_csv(ruta,
                           usecols=['provincia_iso','fecha','num_casos','num_casos_prueba_pcr','num_casos_prueba_test_ac','num_casos_prueba_ag'],
                           sep=',',
                           decimal=',',
                           encoding='latin1')
    print(pd_datos.head(20))
    menu()



#####  EJERCICIO 4  #####
def ejercicio4():
    ruta = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'
    pd_datos = pd.read_json(ruta)
    print(pd_datos.head())
    menu()



#####  EJERCICIO 5  #####
def ejercicio5():
    ruta = 'https://catalogoreina.com/859-grifos-cocina-roca'
    req = requests.get(ruta)
    soup = Bs(req.text)
    data = soup.find_all(name='a', attrs={'class':'product-name'})
    for dato in data:
        print(str(dato).split('title=')[1].split('>')[0])
    menu()


#####  EJERCICIO 6  #####
def ejercicio6():
    ruta = 'https://db-engines.com/en/ranking'
    req = requests.get(ruta)
    soup = Bs(req.text)
    data = soup.css.select("th.pad-l a")
    for dato in data:
        print(dato.text)
    menu()


#####  EJERCICIO 7  #####
def ejercicio7():
    ruta = 'https://catalogoreina.com/nuestras-marcas-muebles-bano/10233-mueble-bano-con-patas-althea-moderno-3-cajones.html'
    req = requests.get(ruta)
    soup = Bs(req.text)
    condicion = soup.find_all(name='p', attrs={'id':'product_condition'})[0].text
    name = soup.find_all(name='h1', attrs={'itemprop':'name'})[0].text
    #medidas = soup.find_all(name='a', attrs={'class':'product-name'})
    #plazo = soup.find_all(name='a', attrs={'class':'product-name'})
    print('Nombre: ',name,'\nCondicion: ',condicion)
    
    menu()



#### MENU ####
def menu():
    #try:
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
    #except ValueError:
    #    print('Adios')
menu()