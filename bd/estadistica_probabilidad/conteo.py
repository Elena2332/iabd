import math
xi = (0, 1, 2, 3, 4)
fi = (5, 6, 8, 4, 2)
n = 0
for f in fi:
    n = n+f
print('N= ',n)


#sumatorio xi[i]*fi[i] / n
media = 0.0
for i in range(len(xi)):
    media = media + xi[i]*fi[i]
media = media/n 
print('Media= ',media)


#1/N *(sumatorio de (xi - media)² * fi)
varianza = 0.0
for i in range(len(xi)):
    varianza = varianza + math.pow(xi[i]-media,2)*fi[i]
varianza = varianza*(1/n) 
print('Varianza= ',varianza)


# raiz cuadrada varianza
desviacion = math.sqrt(varianza)
print('Desviacion= ',desviacion)




