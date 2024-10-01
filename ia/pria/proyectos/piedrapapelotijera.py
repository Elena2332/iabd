import random


def comprobarGanador(numJ,numM):    # True: gana jugador,  False: pierde jugador
    if numJ == 1 and numM == 3:   # piedra gana tijera
        return True
    if numJ == 2 and numM == 1:  # papel gana piedra
        return True
    if numJ == 3 and numM == 2:  # tijera gana papel
        return True
    return False


conteo = [0,0,0]   # partidas jugadas, victorias jugador, empates
opciones = {1:'Piedra', 2:'Papel', 3:'Tijeras'}
seguirJugando = True
print('Bienvenido sea al maravilloso juego de Piedra Papel Tijera')
while seguirJugando :
    respJugador = 0
    noBien = True
    while noBien:   #validamos la respuesta
        try:
            print('''\nSelecciona tu jugada
            1. Piedra
            2. Papel
            3. Tijera
            0. Ver resultados''')
            respJugador = int(input())
            if respJugador < 0 or respJugador > 3:
                print('Jugada Irreconocible. Introduce el numero de tu jugada')
            else:
                noBien = False
            if respJugador == 0 :
                seguirJugando = False
        except:
            print('Jugada Irreconocible. Introduce el numero de tu jugada')

    respMaquina = random.randint(1,3)
    if respJugador > 0 and respJugador <= 3:      # si no a elegido terminar
        conteo[0] += 1   # total partidas
        if respJugador == respMaquina:    # empate
            conteo[2] += 1   
            print('Empate a ',opciones[respJugador])
        else :      # guardamos si gana
            if comprobarGanador(respJugador, respMaquina) :
                conteo[1] = conteo[1]+1
                print(opciones[respJugador],' gana ',opciones[respMaquina],'\nJugador GANA')
            else:
                print(opciones[respMaquina],' gana ',opciones[respJugador],'\nJugador PIERDE')
        print('__'*20,'\n')
print('''
              RESULTADOS
      ===========================
        Partidas Jugadas --- {}
        Victorias ---------- {} 
        Empates ------------ {}
        Derrotas ----------- {}
      ==========================='''
      .format(conteo[0], conteo[1], conteo[2], (conteo[0]-conteo[1]-conteo[2]) ))
