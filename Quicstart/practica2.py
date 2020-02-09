# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:06:36 2019

@author: nomameserick
"""

cola = [] #creación
cola.append("Argentina") #apilamiento
cola.append("Uruguay")
cola.append("Brazil")
cola.append("Paraguay")
cola.append("Venezuela")
print("Primeras inserciones ", cola)

cola.pop(0) #Extracción 
print("cola luego de la Extracción: ", cola)

cola[0] #Lectura del 1er elemento
print("Lectura del primer elemento: ", cola[0])

cola[len(cola)-1] #Lectura del ultimo elemento
print("Lectura del último elemento: ", cola[len(cola)-1])

cola.clear() #Vaciando la pila
print("Se ha vaciado la cola...", cola)