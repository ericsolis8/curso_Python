# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:46:35 2019

@author: nomameserick
"""
pila = [] #creación
pila.append("Argentina") #apilamiento
pila.append("Uruguay")
pila.append("Brazil")
pila.append("Paraguay")
pila.append("Venezuela")
print("Primeras inserciones ", pila)

pila.pop() #Extracción 
print("Pila luego de la Extracción: ", pila)

pila[0] #Lectura del 1er elemento
print("Lectura del primer elemento: ", pila[0])

pila[len(pila)-1] #Lectura del ultimo elemento
print("Lectura del último elemento: ", pila[len(pila)-1])

pila.clear() #Vaciando la pila
print("Se ha vaciado la pila...", pila)