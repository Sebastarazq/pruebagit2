import numpy as np
import time
import random

print('Ingresa el orden de la matriz a calcular ')
filasA, columnasA = int(input()), int(input())

# Creando la matriz vacía
matrizL = []
for i in range(filasA):
    matrizL.append([0] * columnasA)

# Rellenando la matriz
inicio=time.time()
for fila in range(filasA):
    for columna in range(columnasA):
        matrizL[fila][columna] = random.randint(2,10)

determinante = np.linalg.det(matrizL)
print(determinante)
fin=time.time()
print ("\n")
print ("El tiempo del programa fue: ", fin-inicio)
print("Hola")