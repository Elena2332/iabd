from vectors_ej8 import Vector2D

vec1 = Vector2D(2,6)
print(vec1.__str__())  # respuesta: (2,6)

print(vec1.modules())   # raiz de 2*2+6*2 = 4
print(vec1.__str__())   # compruebo que vec1 no ha cambiado


vec1.scalar_prod(2)
print(vec1.__str__())  # (2,6) --> (4,12)

vec2 = Vector2D(1,1)
vec_suma = Vector2D.sum(vec1,vec2)  #(4,12) + (1,1) = (5,13)
print(vec_suma.__str__())

vec_resta = Vector2D.subtract(vec2,vec1)  #(1,1) - (4,12) = (-3,-11)
print(vec_resta.__str__())