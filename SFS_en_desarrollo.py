# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:24:19 2020

@author: amine
"""

import pandas 
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import evaluacion_robusta_variables as promedio_atributo

df = pandas.read_csv('titanic.csv',sep=",")
df_atributos = pandas.read_csv('titanic.csv').columns.tolist()
variable_predictora = df_atributos[len(df_atributos)-1]
df_atributos.remove(variable_predictora)
variable_predictora = 'Survived'
#atributos = df.loc[:,'Pclass':'Sex']
#print(variable_predictora)
tamaño = len(df_atributos)
set_atributos = set()

def sfs_en_desarrollo(df,target_name,D):
    atributos = df.columns.tolist()
    atributos.remove(target_name)
    solucion_actual = []
    solucion_tabla = []
    k = 0 
    ganancias = []
    print('{:<10}{:>80} {:>10}'.format('Soluciones','Rendimiento','Tamaño'))
    while k <D:
        variable_elegida = calcular_mejor_variable(df,atributos,target_name,solucion_actual)
        atributos.remove(variable_elegida)
        solucion_actual.append(variable_elegida)
        atributos_de_la_solucion = df[solucion_actual]
        ganancia_solucion_actual = promedio_atributo.Evaluacion_robusta.validacion_cruzada(df,atributos_de_la_solucion,target_name,1,5)
        print('{}{:>80.2f}{:>10}'.format(solucion_actual,ganancia_solucion_actual,len(solucion_actual)))
        k += 1
    
    return solucion_actual,ganancia_solucion_actual

def calcular_mejor_variable(datos,atributos,variables_predictora,solucion_actual):
    tam = len(atributos)
    ac = 0
    solucion_temporal = solucion_actual
    for i in range(tam-1):
        solucion_temporal.append(atributos[i])
        atributos_a_probar = datos[solucion_temporal]
        ganancia_del_atributo = promedio_atributo.Evaluacion_robusta.validacion_cruzada(datos,atributos_a_probar,variable_predictora,10,20)
        if(ganancia_del_atributo>ac):
            mejor_variable = atributos[i]
            ac = ganancia_del_atributo
            solucion_temporal.remove(atributos[i])
        else:
            solucion_temporal.remove(atributos[i])
    return mejor_variable
print(sfs_en_desarrollo(df,variable_predictora,4))
#solucion_actual = ['Initial']
#df_atributos.remove('Initial')
#print(calcular_mejor_variable(df,df_atributos,variable_predictora,solucion_actual))
#solucion_actual = ['Initial']
#print(calcular_primera_mejor_variable(df,df_atributos,variable_predictora,solucion_actual))