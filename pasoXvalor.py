# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:15:31 2019

@author: nomameserick
"""

def intenta_modificar(x, y, z):
    x = 23
    y.append(42)
    z = [99] #nueva referencia
    print (x)
    print (y)
    print (z)
a=77  #variable Inmutable
b=[99]  #variable Mutable
c=[28]

intenta_modificar(a,b,c)