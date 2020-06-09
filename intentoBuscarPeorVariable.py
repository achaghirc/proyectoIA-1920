# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:47:22 2020

@author: Alvaro
"""
import pandas as pd
import evaluacionRobusta as promedio

datos = pd.read_csv('titanic.csv',sep=",")
variables = datos.columns.tolist()
#variable_predictora = variables[len(variables)-1]
variable_predictora = 'Survived'
solucionActual = ['Initial', 'SibSp', 'Deck', 'Fare_cat','Alone']

      
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

def calcularPeorVariable(solucionActual, gananciaSolucionActual):
    tam = len(solucionActual)
    for i in range(tam):
        solucionTemporal = solucionActual[:]
        solucionTemporal.remove(solucionTemporal[i])
        atributosDeLaSolucionTemp = datos[solucionTemporal]
        gananciaSolucionTemp = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionTemp, 15, 10)
        if(gananciaSolucionTemp>gananciaSolucionActual):
            solucionActual = solucionTemporal[:]
            gananciaSolucionActual = gananciaSolucionTemp
            break
    return solucionActual

variable_elegida = calcular_mejor_variable(datos, variables, variable_predictora, solucionActual)
solucionActual.append(variable_elegida) 
atributosDeLaSolucion = datos[solucionActual]
gananciaSolucionActual = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucion, 15, 10)

print(solucionActual)
print(gananciaSolucionActual)

variablesNuevas = calcularPeorVariable(solucionActual, gananciaSolucionActual)
print(variablesNuevas)
