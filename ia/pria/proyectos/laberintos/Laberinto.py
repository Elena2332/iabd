import random

class Laberinto:
    '''Laberinto
        Atributos:
            +tablero  (matriz)
            +totalFilas  (int)
            +totalColumnas  (int)
        Metodos:
            llenarLaberintos(self)
            mostrarLaberinto(self)
    '''

    def __init__(self, i, j):
        self.tablero = None
        
        # tablero minimo 5x5
        if j < 5:
            self.totalColumnas = None 
        else:
            self.totalColumnas = j
        if i < 5:  
            self.totalFilas = None
        else:          
            self.totalFilas = i
            

    def casillasPosibles(self, cActual, cAntes, cEntrada):  # devuelve array de casilla a las que puede ir sin contar la anterior
        casillas = []   #la casilla no puede superar el borde, ser la anterior o la entrada
        #comprobar casilla sup
        if cActual[0] != 0:   #comprueba el borde
            aux = [cActual[0]-1,cActual[1]]
            if aux != cAntes  and  aux != cEntrada :  # comprueba la anterior y entrada
                if self.tablero[aux[0],aux[1]] == 2:  #aux = casilla de relleno inicial
                    casillas.append(aux)

        #comprobar casilla inf
        if cActual[0] != self.totalFilas-1:  
            aux = [cActual[0]+1,cActual[1]]
            if aux != cAntes  :  # comprueba la anterior, entrada por fila 0
                if self.tablero[aux[0],aux[1]] == 2:  
                    casillas.append(aux)

        #comprobar casilla izq
        if cActual[1] != 0:   
            aux = [cActual[0],cActual[1]-1]
            if aux != cAntes and  aux != cEntrada:  
                if self.tablero[aux[0],aux[1]] == 2:  
                    casillas.append(aux)

        #comprobar casilla der
        if cActual[1] != self.totalColumnas-1:   
            aux = [cActual[0],cActual[1]+1]
            if aux != cAntes  and  aux != cEntrada :  
                if self.tablero[aux[0],aux[1]] == 2:  
                    casillas.append(aux)
        
        return casillas

        

    def llenarLaberinto(self):    #return False si no ha podido,  True si ha ido bien
        '''0:Pared  1:camino  2:relleno inicial  3:entrada  7:salida  
            Selecciona entrada (primera fila azar) 
            Construye camino al azar y guarda en una lista las casillas
            genera caminos secundarios/falsos a partir de puntos al azar de la lista
            '''
        # tablero minimo 
        if self.totalColumnas == None or self.totalFilas == None:
            return False    # tablero no creado
        
        # inicializamos tablero vacio
        self.tablero = []
        
        # rellenamos tablero con 2 para poder referenciar casillas por indices
        # y diferencir las casillas cambiadas de las que no al rellenar el laberinto
        for i in range(self.totalFilas):
            fila = []
            for j in range(self.totalColumnas):
                fila.append(2)
            self.tablero.append(fila)

        #casilla entrada fila superior, columna al azar
        entrada = [0,random.randint(0,self.totalColumnas-1)]
        self.tablero[0][entrada[1]] = 3  #entrada
        casillaActual = entrada
        casillaAnterior = entrada

        #crear el camino
        casillas = self.casillasPosibles(casillaActual, casillaAnterior, entrada)
        print(casillas)

        return True     #tablero creado correctamente
        

    def mostrarLaberinto(self):
        if self.tablero != None: 
            for i in range(self.totalFilas):
                fila = ''
                for j in range(self.totalColumnas):
                    fila += str(self.tablero[i][j])+' '
                print(fila)
        else:
            print('No hay laberinto que mostrar')