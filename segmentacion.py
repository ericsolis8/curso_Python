# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:57:26 2019

@author: nomameserick
"""

def segmento(secuencia, inicio=None, final=None, paso=None):
#Implementacion basica de segmentacion
    return secuencia[inicio:final:paso]
rima = 'pez uno, pez dos, pez rojo, pez azul'.split()


#rima
#segmento(rima)
#segmento(rima, paso=2)
#segmento (rima, 1, paso=2)
#segmento (rima, inicio=1, final=4, paso=2)