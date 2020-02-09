import numpy as np
import random
import time
#define tamaño arreglo forma directa
#a=np.array([0,0,0])

#define tamaño arreglo forma auto
a=np.arange(3)

#define tamaño arreglo desde un rango incremental
arreglo_rango=np.arange(1,1000,1)

#captura de valores del rango
for posicion in range(0,3,1):
    numero=int(input("Escribe el valor del arreglo de la posicion: "))
    a[posicion]=numero
    
for posicion in range(0,3,1):
    print("El valor del arreglo en la posicion: ", posicion, "es: ", a[posicion])

'''
for posicion in range(0,a.size):
    numero=int(input("Escribe el valor del arreglo de la posicion: "))
    a[posicion]=numero
'''

print("En 1 segundo se mostrara el tamaño del arreglo")
time.sleep(1)
print(a.size)

print("En 1 segundo se mostrara el arreglo")
time.sleep(1)
print(a)

print("En 1 segundo se ordenara el arreglo")
time.sleep(1)
a.sort()
print(a)

print("En 1 segundo se mostrara el arreglo de 1000 valores")
time.sleep(5)
print(arreglo_rango)

print("En 1 segundo se mostrara el arreglo de 1000 valores pero ordenado")
time.sleep(5)
arreglo_rango.sort()
print(arreglo_rango)

arreglo_aleatorio=np.arange(1000)
for x in range(1,1000,1):
    numeroAleatorio=random.uniform(1,10000)
    arreglo_aleatorio[x]=numeroAleatorio
    
print(arreglo_aleatorio)
