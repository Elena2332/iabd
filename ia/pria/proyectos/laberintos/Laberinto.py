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

    def __init__(self,i,j):
        self.tablero = []
        self.totalFilas = i
        self.totalColumnas = j
        
    def llenarLaberinto(self):
        '''Selecciona entrada
            Construye camino al azar y guarda en una lista las casillas
            genera caminos secundarios/falsos a partir de puntos al azar de la lista'''
        for i in range(self.totalFilas):
            fila = []
            for j in range(self.totalColumnas):
                fila.append(0)
            self.tablero.append(fila)

    def mostrarLaberinto(self):
        for i in range(self.totalFilas):
            fila = ''
            for j in range(self.totalColumnas):
                fila += str(self.tablero[i][j])+'  '
            print(fila)