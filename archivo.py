# -*- coding: utf-8 -*-
import numpy as np
import sys
#Genera una lista de mil numeros
S=range(1000)
print('Resultado lista python: ')
#calcular memoria asignada
print(sys.getsizeof(5))
print()
#generar array de mil numeros utilizando numpy
D=np.arange(1000)
print('Resultado Numpy array: ')
#calcular memoria asiganada
print(D.size*D.itemsize)