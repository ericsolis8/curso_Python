# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:02:11 2019

@author: nomameserick
"""

D = {'a': 1, 'b': 1.2, 'c': 1j}
for clave, valor in D.iteritems():
    print('Clave: %s con valor: %s' % (clave, valor))
    