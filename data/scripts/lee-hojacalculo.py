# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:53:04 2019

@author: nomameserick
"""

# Estas dos líneas son necesarias solo si GemPy no está instalado 
import  sys, os 
sys.path.append("../../ ..")

# Importando GemPy 
import gempy as gp

# Incrustar figuras de matplotlib en los cuadernos 
%matplotlib inline

# Importar bibliotecas auxiliares 
import  numpy as np 
import  matplotlib.pyplot as plt

geo_model  =  gp . create_model ( 'Tutorial_ch1-1_Basics' )

data_path =  '../ ..' 
# Importar los datos de archivos CSV y establecer la extensión y resolución 
gp . init_data ( geo_model ,  [ 0 , 2000. , 0 , 2000. , 0 , 2000. ], [ 50 , 50 , 50 ],  
      path_o  =  data_path + "/data/input_data/tut_chapter1/simple_fault_model_orientations.csv" , 
      path_i  =  data_path + "/data/input_data/tut_chapter1/simple_fault_model_points.csv" , default_values = True ); 