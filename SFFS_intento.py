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
    tam = len(variables)
    print("Tamaño Variables:")
    print(tam)
    print('{:<10}{:>80} {:>10}'.format('Soluciones','Rendimiento','Tamaño'))
    while k != 10:
        while len(añadidos) != tam-1:
        # Añadir Mejor Variable
            variableElegida, añadidos = calcular_mejor_variable(datos, variables, solucionActual, añadidos)
            variables.remove(variableElegida)
            solucionActual.append(variableElegida)
            atributosDeLaSolucion = datos[solucionActual]
            gananciaSolucionActual = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucion, 15, 10)
            print('{}{:>80.2f}{:>10}'.format(solucionActual, gananciaSolucionActual, len(solucionActual)))
           
        # Eliminar Peor Variable
        solucionNueva, eliminados, k = calcularPeorVariable(solucionActual, gananciaSolucionActual, eliminados, k)
        atributosDeLaSolucionNueva = datos[solucionNueva]
        gananciaSolucionNueva = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionNueva, 15, 10)
        print('{}{:>80.2f}{:>10}'.format(solucionNueva, gananciaSolucionNueva, len(solucionNueva)))
    return solucionNueva, gananciaSolucionNueva

def calcularPeorVariable(solucionActual, gananciaSolucionActual,eliminados, k):
    tam = len(solucionActual)
    for i in range(tam-1):
        solucionTemporal = solucionActual[:]
        solucionTemporal.remove(solucionTemporal[i])
        atributosDeLaSolucionTemp = datos[solucionTemporal]
        gananciaSolucionTemp = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionTemp, 20, 10)
        k +=1
        print("k:")
        if(gananciaSolucionTemp>gananciaSolucionActual):
            k=0
            eliminados.append(solucionTemporal[i])
#            solucionActual = solucionTemporal[:]
            gananciaSolucionActual = gananciaSolucionTemp     
        if k>=10:
            break
    solucionActual = solucionTemporal[:]
    return solucionActual, eliminados, k
        

def calcular_mejor_variable(datos, variables, solucion_actual, añadidos):
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
    añadidos.append(mejor_variable)
    return mejor_variable, añadidos

print(SFFS(datos, variable_predictora))
    
    
    