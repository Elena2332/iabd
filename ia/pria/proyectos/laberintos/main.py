#from Laberinto import *
from Laberinto import Laberinto

labe = Laberinto(5,8)
  
#print(Laberinto.__doc__)

if labe.llenarLaberinto():
    labe.mostrarLaberinto()
else:
    print('El laberinto no se ha podido crear prueba de nuevo')