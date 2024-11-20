#!/usr/bin/python3 
import sys 
lista = {}
for linea in sys.stdin:
    linea = linea.strip()
    letra,cont = linea.split('\t')
    cont = int(cont)
    if letra in lista:
        lista[letra] = lista[letra]+cont
    else:
        lista[letra] = cont
for letra in lista:
    print('{}\t{}'.format(letra,lista[letra]))
