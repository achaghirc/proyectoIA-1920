# -*- coding: utf-8 -*-

import pandas as pd
import evaluacionRobusta as promedio

datos = pd.read_csv('titanic.csv',sep=",")
variables = datos.columns.tolist()
#variable_predictora = variables[len(variables)-1]
variable_predictora = 'Survived'


def SFS(datos, variable_predictora, D):
    variables = datos.columns.tolist()
    variables.remove(variable_predictora)
    k=0
    solucion_actual = []
    print('{:<10}{:>80} {:>10}'.format('Soluciones','Rendimiento','Tamaño'))
    while k<D:
        variable_elegida = calcular_mejor_variable(datos, variables, variable_predictora, solucion_actual)
        variables.remove(variable_elegida)
        solucion_actual.append(variable_elegida)
        atributos_de_la_solucion = datos[solucion_actual]
        ganancia_solucion_actual = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_de_la_solucion, 15, 10)
        print('{}{:>80.2f}{:>10}'.format(solucion_actual, ganancia_solucion_actual, len(solucion_actual)))
        k += 1
    return solucion_actual,ganancia_solucion_actual
        
        
        
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




