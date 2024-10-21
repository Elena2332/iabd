import math
import datetime as dt

#####  EJERCICIO 1  #####
def ejercicio1():
    print('Introduce numero')
    try:
        num = float(input())
        # radianes = num*math.pi/180
        radianes = math.radians(num)
        print(num,'º  =  ',radianes,'rad')
    except:
        print('Error en los datos')
    menu()



#####  EJERCICIO 2  #####
def ejercicio2():
    try:
        print('Introduce altura del cilindro')
        h = float(input())
        print('Introduce radio del cilindro')
        radio = float(input())
        pi = math.pi
        rr = math.pow(radio,2)
        volumen = pi*h*rr
        area = 2*pi*rr + 2*pi*radio*h
        print('Volumen: ',volumen,'\tArea: ',area)
    except:
        print('Error en los datos')
    menu()




#####  EJERCICIO 3  #####
def ejercicio3():
    try:
        print('Introduce numero')
        num = int(input())
        suma1 = 0
        suma2 = 0
        for i in range(num):
            suma1 += suma1
            suma2 = suma2 + math.pow(i+1,2)
        suma1 = math.pow(suma1,2)
        print(suma1,' - ',suma2,' = ',suma1-suma2)
    except:
        print('Error en los datos')
    menu()



#####  EJERCICIO 4  #####
def ejercicio4():
    try:
        print('Introduce numero')
        a = int(input())
        print('Introduce otro numero')
        b = int(input())
        while b != 0:
            aux = b
            b = a % b
            a = aux
        print('Maximo Comun Divisor: ',a)
    except:
        print('Error en los datos')
    menu()



#####  EJERCICIO 5  #####
def ejercicio5():
    noBien = True
    a=b=h = 0
    while noBien:
        try:
            print('''Calculadora de Pitagoras
                   Introduce 0 si es lo que necesitas calcular
                   Introduce cateto a''')
            a = float(input())
            print('Introduce cateto b')
            b = float(input())
            print('Introduce hipotenusa')
            h = float(input())
            if a==0 or b==0 or h==0:
                noBien = False
        except:
            print('Error en los datos')
    # h^2 = a^2 + b^2
    if h==0:  # calcular hipotenusa
        h = math.sqrt(math.pow(a,2)+math.pow(b,2))
    elif a==0:
        a = math.sqrt(math.pow(h,2)-math.pow(b,2))
    elif b==0:
        b = math.sqrt(math.pow(h,2)-math.pow(a,2))
    print('Hipotenusa: {}, cateto a: {}, cateto b: {}'.format(h,a,b))
    menu()


#####  EJERCICIO 6  #####
def ejercicio6():
    print('''
          a) Fecha y hora actuales
          b) Año en curso
          c) Mes del año
          d) Número de semana del año
          e) Día laborable de la semana
          f) Día del año
          g) Día del mes
          h) Día de la semana''')
    resp = input()
    d = dt.datetime.now()
    match resp:
        case 'a':
            print('Fecha y hora: ',d.strftime('%d/%m/%y   %X'))
        case 'b':
           print("Año: ", d.year)
        case 'c':
           print("Mes: ", d.strftime('%B'))
        case 'd':
            print('Numero de semana del año: ',d.strftime('%W'))
        case 'e':
            print('Dia laborable: ', d.strftime('%u'))
        case 'f':
            print('Dia del año: ', d.strftime('%j'))
        case 'g':
           print("Dia del mes: ", d.strftime('%d de %B'))
        case 'h':
            print('Dia de la semana: ', d.strftime('%A'))
        case _:
            print('Respuesta incorrecta')
    menu()


#####  EJERCICIO 7  #####
def ejercicio7():
    d = dt.datetime.now()
    d2 = d - dt.timedelta(days=5)
    print('Fecha actual: ',d.strftime('%d-%m-%y'))
    print('Fecha 5 dias antes: ', d2.strftime('%d-%m-%y'))
    menu()


#####  EJERCICIO 8  #####
def divisors(n):
    """
    Calcula los divisores de un número entero positivo.
    Args:
        n: Número entero positive
    Returns:
        divisors: Lista de divisores de n
    """
    if n<0:
        raise ValueError
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0: 
            divisors.append(i)
            return divisors
    

def ejercicio8():
    try:
        print(divisors(26))
        divisors('a')
        print(divisors(-3))
    except ValueError:
        print('ValueError: Valor negativo introducido')
    except TypeError:
        print('TypeError: Valor introducido no numerico')
    menu()


#####  EJERCICIO 9  #####
def ejercicio9():
    msgError = 'Numero no válido'
    try:
        print('Introduce edad')
        edad = int(input())
        if edad < 0 or edad >150:
            raise ValueError
    except ValueError:
        print(msgError,', debe estar entre 0 y 150 para ser valido')
    except :
        print(msgError,' no es un numero entero')
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
    except ValueError:
        print('Adios')
menu()