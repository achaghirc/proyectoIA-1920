# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:46:49 2020

@author: amine
"""
import pandas
from SFFS_Final import SFFS
from SFS import SFS

"""
    
1. Ejecutar el archivo, y seguir las introducciones. 
    
   1.1 En la primera entrada introducir cual de los dos metodos se desea ejecutar SFS o SFFS 
   1.2 En la segunda entrada seleccionar uno de los dos archivos csv a elegir entre titanic.csv y BreastCancerDataset.csv
   
   --> Se mostrara la traza de ejecucion del algoritmo en el caso de SFFS y al final la solucion guardada.
    
"""
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
    if eleccion == 'SFFS' and archivo == 'titanic.csv':
        print('Ejecutando SFFS para Titanic...')
        tabla,archivo_html = SFFS.algoritmo_sffs(datos,variable_predictora)
        archivo = open('resultados_titanic.html','w')
        archivo.write(archivo_html)
        archivo.close()
        print(tabla)
        break
    elif eleccion == 'SFFS' and archivo == 'BreastCancerDataset.csv':
        print('Ejecutando SFFS para BreastCancerDataset...')
        tabla,archivo_html = SFFS.algoritmo_sffs(datos,variable_predictora)
        archivo = open('resultados_BreastCancer.html','w')
        archivo.write(archivo_html)
        archivo.close()
        print(tabla)
        break
    
    elif eleccion == 'SFS': 
        D = input('Seleccione la cantidad de variables que desea probar (Si no especifica nada se probarán todas)\n')
        if D == '' and archivo == 'titanic.csv':
            print('Ejecutando SFS con todas las variables para Titanic...')
            D = len(variables)-2 #TODAS LAS ITERACIONES --> Excluyendo la variable resultado. 
            tabla, archivo_sfs = SFS.algoritmo_sfs(datos,variable_predictora,D)
            archivo = open('resultado_sfs_titanic.html','w')
            archivo.write(archivo_sfs)
            archivo.close()
            print(tabla)
            break
        elif D == '' and archivo == 'BreastCancerDataset.csv':
            print('Ejecutando SFS con todas las variables para BreastCancerDataset...')
            D = len(variables)-2 #TODAS LAS ITERACIONES --> Excluyendo la variable resultado. 
            tabla, archivo_sfs = SFS.algoritmo_sfs(datos,variable_predictora,D)
            archivo = open('resultado_sfs_BreastCancer.html','w')
            archivo.write(archivo_sfs)
            archivo.close()
            print(tabla)
            break
        elif D != '' and archivo == 'titanic.csv': 
            print('Ejecutando SFS con el valor D introducido para Titanic...')
            tabla, archivo_sfs = SFS.algoritmo_sfs(datos,variable_predictora,int(D))
            archivo = open('resultado_sfs_titanic.html','w')
            archivo.write(archivo_sfs)
            archivo.close()
            print(tabla)
            break
        elif D != '' and archivo == 'BreastCancerDataset.csv':
            print('Ejecutando SFS con el valor D introducido para BreastCancerDataset...')
            tabla, archivo_sfs = SFS.algoritmo_sfs(datos,variable_predictora,int(D))
            archivo = open('resultado_sfs_BreastCancer.html','w')
            archivo.write(archivo_sfs)
            archivo.close()
            print(tabla)
            break
    else:
        print('Has introducido un nombre de algoritmo incorrecto, vuelve a intentarlo las opciones son SFFS o SFS')
        break
    
