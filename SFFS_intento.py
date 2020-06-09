# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:40:54 2020

@author: Alvaro
"""

import pandas as pd
import evaluacionRobusta as promedio

datos = pd.read_csv('titanic.csv',sep=",")
variables = datos.columns.tolist()
#variable_predictora = variables[len(variables)-1]
variable_predictora = 'Survived'

def SFFS(datos, variable_predictora):
    variables = datos.columns.tolist()
    variables.remove(variable_predictora)
    k=0
    solucionActual = []
    añadidos = []
    eliminados = []
    print('{:<10}{:>80} {:>10}'.format('Soluciones','Rendimiento','Tamaño'))
    while (len(añadidos) != len(variables) and k != 10):
        # Añadir Mejor Variable
        variableElegida = calcular_mejor_variable(datos, variables, variable_predictora, solucionActual)
        variables.remove(variableElegida)
        solucionActual.append(variableElegida)
        atributosDeLaSolucion = datos[solucionActual]
        gananciaSolucionActual = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucion, 15, 10)
        print('{}{:>80.2f}{:>10}'.format(solucionActual, gananciaSolucionActual, len(solucionActual)))
        añadidos.append[variableElegida]
        
        # Eliminar Peor Variable
       solucion = calcularPeorVariable(solucionActual, gananciaSolucionActual)
       atributosDeLaSolucionNueva = datos[solucion]
       gananciaNuevoConjunto = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionNueva, 15, 10)
        
        

def calcularPeorVariable(solucionActual, gananciaSolucionActual):
    tam = len(solucionActual)
    for i in range(tam):
        solucionTemporal = solucionActual[:]
        solucionTemporal.remove(solucionTemporal[i])
        atributosDeLaSolucionTemp = datos[solucionTemporal]
        gananciaSolucionTemp = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionTemp, 15, 10)
        if(gananciaSolucionTemp>gananciaSolucionActual):
            eliminados.append(solucionTemporal[i])
            solucionActual = solucionTemporal[:]
            gananciaSolucionActual = gananciaSolucionTemp
            break
    return solucionActual
        

def calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual):
    tam = len(variables)
    ac = 0
    solucion_temporal = solucion_actual
    for i in range(tam-1):
        solucion_temporal.append(variables[i])
        atributos_a_probar = datos[solucion_temporal]
        ganancia_del_atributo = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_a_probar,15,10)
        if(ganancia_del_atributo>ac):
            mejor_variable = variables[i]
            ac = ganancia_del_atributo
            solucion_temporal.remove(variables[i])
        else:
            solucion_temporal.remove(variables[i])
    return mejor_variable
        
        
    
    
    