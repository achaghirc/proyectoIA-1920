# -*- coding: utf-8 -*-

import pandas as pd
import evaluacionRobusta as promedio
import operator
import imprimir_datos_ordenados as impdatos

datos = pd.read_csv('C:/Users/amine/OneDrive - UNIVERSIDAD DE SEVILLA/TERCERO DE CARRERA/Segundo Cuatrimestre/IA/ProyectoIA-1920/proyectoIA-1920/titanic.csv')
variables = datos.columns.tolist()
#variable_predictora = variables[len(variables)-1]
variable_predictora = 'Survived'


def SFS(datos, variable_predictora, D):
    variables = datos.columns.tolist()
    variables.remove(variable_predictora)
    k=0
    solucion_actual = []
    Lista = []
    Lista_ganancias = []
    diccionario_resultado = {}
    while k<D:
        variable_elegida = calcular_mejor_variable(datos, variables, variable_predictora, solucion_actual)
        variables.remove(variable_elegida)
        solucion_actual.append(variable_elegida)
        atributos_de_la_solucion = datos[solucion_actual]
        ganancia_solucion_actual = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_de_la_solucion, 15, 10)
#        print('{}{:>80.2f}{:>10}'.format(solucion_actual, ganancia_solucion_actual, len(solucion_actual)))
        
        Lista.append(solucion_actual[:])
        Lista_ganancias.append(ganancia_solucion_actual)
        diccionario_resultado[ganancia_solucion_actual] = Lista[k]
        k += 1
    return impdatos.Imprimir.datos_ordenados(diccionario_resultado)


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
print(SFS(datos, variable_predictora, 4))




