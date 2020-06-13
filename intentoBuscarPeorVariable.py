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
solucionActual = ['Initial', 'SibSp', 'Deck', 'Fare_cat','Title', 'Sex']

def calcularPeorVariable(solucionActual, gananciaSolucionActual):
    tam = len(solucionActual)
    for i in range(tam):
        solucionTemporal = solucionActual[:]
        solucionTemporal.remove(solucionTemporal[i])
        atributosDeLaSolucionTemp = datos[solucionTemporal]
        gananciaSolucionTemp = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionTemp, 20, 10)
        if(gananciaSolucionTemp>gananciaSolucionActual):
            solucionActual = solucionTemporal[:]
            gananciaSolucionActual = gananciaSolucionTemp
            break
    return solucionActual

print(solucionActual)
atributosDeLaSolucion = datos[solucionActual]
gananciaSolucionActual = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucion, 15, 10)
print(gananciaSolucionActual)

variablesNuevas = calcularPeorVariable(solucionActual, gananciaSolucionActual)
print(variablesNuevas)
