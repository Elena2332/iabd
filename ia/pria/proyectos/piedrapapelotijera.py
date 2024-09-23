import random


conteo = [0,0,0]   # partidas jugadas, victorias jugador, empates
seguirJugando = True
print('Bienvenido sea al maravilloso juego de Piedra Papel Tijera')
while seguirJugando :
    respJugador = 0
    noBien = True
    while noBien:
        try:
            print('''\nSelecciona tu jugada
            1. Piedra
            2. Papel
            3. Tijera
            0. Ver resultados''')
            respJugador = int(input())
            noBien = False
            if respJugador == 0 :
                seguirJugando = False
        except:
            print('Debes introducir el numero correspondiente a tu jugada')
    respMaquina = random.randint(1,3)
    if respJugador != 0:
        conteo[0] = conteo[0]+1   # total partidas
        if respJugador == respMaquina: 
            conteo[2] = conteo[2]+1   # empate
        else :
            if respJugador == 1 and respMaquina ==3:
                conteo[1] = conteo[1]+1
            if respJugador == 2 and respMaquina == 1:
                conteo[1] = conteo[1]+1
            if respJugador == 3 and respMaquina == 2:
                conteo[1] = conteo[1]+1
        conteo[0] = conteo[0]+1
print(conteo)
