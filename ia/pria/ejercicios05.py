import re 


def ejercicio1():
    txt = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, 
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, 
adarga antigua, rocín flaco y galgo corredor"""
    p = re.compile(r"\s", re.IGNORECASE)
    print(p.split(txt))
    #print(p.findall(txt))
    menu()


def ejercicio2():
    texto = '''En 1492 los Reyes Católicos financiaron el proyecto del navegante Cristóbal 
Colón en la búsqueda de una nueva ruta comercial con Asia a través del océano 
Atlántico, y proclamarían la expulsión de los judíos. La llegada al Nuevo Mundo 
y la posterior conquista de América forjaron la creación del Imperio español. 
Durante los siguientes siglos España se alzaría como actor principal del mundo 
occidental y primera potencia de la época. Durante los siglos xvi y xvii 
tendría lugar también la época de mayor apogeo de la cultura y las artes 
hispanas conocida como Siglo de Oro.

El Imperio español en 1580, tras la unificación de la península ibérica bajo un 
único rey español Felipe II, comprendía América del Sur, América Central y el 
Caribe, grandes áreas de América del Norte en diferentes grados de influencia o 
control, las islas Filipinas en Asia, así como enclaves de diversa importancia 
en las costas de África y la India. Incluía además numerosas posesiones en 
Europa, los Países Bajos españoles, el Ducado de Milán o el Reino de Nápoles, la 
mayoría de ellas perdidas tras la paz de Utrecht de 1713.'''
    
    for a in re.findall(r'\d{4}',texto): print(a)
    menu()


def ejercicio3():
    texto = '¡¡¡¡¡¡¡Oye!!!!!!!!'
    repes = re.findall(r'\W+',texto)
    for a in repes: texto=str.replace(texto,a,a[0])
    print(texto)
    menu()


def ejercicio4():
    texto = 'Me lo estoy pasando muy muy muy bien'
    print('Sin hacer aun')


def ejercicio5():
    print('Sin hacer aun')
def ejercicio6():
    print('Sin hacer aun')
def ejercicio7():
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