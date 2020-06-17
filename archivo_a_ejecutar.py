# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:46:49 2020

@author: amine
"""
import pandas
from SFFS import SFFS
from SFS import SFS

eleccion = input('¿Qué algoritmo quieres ejecutar SFS o SFFS?, introduce cuál:\n')
archivo = input('Introduce el nombre del archivo ( Puede ser titanic.csv o BreastCancerDataset.csv): \n')

while archivo != '' and eleccion != '': 
    if archivo == 'titanic.csv' or archivo == 'BreastCancerDataset.csv':
        datos = pandas.read_csv(archivo,',')
        variables = datos.columns.tolist()
        variable_predictora = variables[len(variables)-1]
    else:
        print('Has introducido un nombre de archivo incorrecto, vuelve a intentarlo con las opciones indicadas')
        break
    if eleccion == 'SFFS':
        print('Ejecutando SFFS...')
        print(SFFS.algoritmo_sffs(datos,variable_predictora))
        break
    elif eleccion == 'SFS': 
        print('Ejecutando SFS')
        D = len(variables)-2 #TODAS LAS ITERACIONES --> Excluyendo la variable resultado. 
        print(SFS.algoritmo_sfs(datos,variable_predictora,D))
        break
    else:
        print('Has introducido un nombre de algoritmo incorrecto, vuelve a intentarlo las opciones son SFFS o SFS')
        break
    
