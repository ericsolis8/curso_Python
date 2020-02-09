# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:51:40 2019

@author: nomameserick

#Bucle while al estilo C (problema de Mandelbrot)

z = 1 + 1j
while abs(z) < 100:
    z= z**2 + 1
    
#Caracteristicas avanzadas
#break sale el bucle encerrado por for/while
    
z = 1 + 1j
while abs(z) < 100:
    if z.imag == 0:
        break
"""
#continue la siguiente iteracion de un bucle

a = [1,0,2,4]
for element in a:
    if element == 0:
        continue
    print (1. / element)
    
