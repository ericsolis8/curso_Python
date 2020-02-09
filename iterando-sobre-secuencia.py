# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:05:24 2019

@author: nomameserick
""
vocales = 'aeiou'
for i in 'parangutirimicuaro':
    if i in vocales:
        print (i)
"""
mensaje = "Hola, como estas?"
mensaje.split() #devuelve una lista
['Hola', 'como', 'estas?']
for palabra in mensaje.split():
    print (palabra)