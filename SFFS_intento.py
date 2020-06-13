# -*- coding: utf-8 -*-

import pandas as pd
import evaluacionRobusta as promedio
import imprimir_datos_ordenados as impdatos
import operator

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
    i=0
#    print('{:<10}{:>80} {:>10}'.format('Soluciones','Rendimiento','Tamaño'))
    Lista = []
    Lista_ganancias = []
    diccionario_resultado = {}
    while len(añadidos) != tam-1:
        # Añadir Mejor Variable
        variableElegida, añadidos = calcular_mejor_variable(datos, variables, solucionActual, añadidos)
        variables.remove(variableElegida)
        solucionActual.append(variableElegida)
        atributosDeLaSolucion = datos[solucionActual]
        gananciaSolucionActual = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucion, 15, 10)
        Lista.append(solucionActual[:])
        Lista_ganancias.append(gananciaSolucionActual)
        diccionario_resultado[gananciaSolucionActual] = Lista[i]
        i+=1
        # Eliminar Peor Variable
        if(len(solucionActual)>2):
            solucionNueva, eliminados, k = calcularPeorVariable(solucionActual, gananciaSolucionActual, eliminados, k)
            atributosDeLaSolucionNueva = datos[solucionNueva]
            gananciaSolucionNueva = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionNueva, 15, 10)
            if(solucionNueva != solucionActual):
                Lista.append(solucionNueva[:])
                Lista_ganancias.append(gananciaSolucionNueva)
                diccionario_resultado[gananciaSolucionActual] = Lista[i]
                i+=1

    return impdatos.Imprimir.datos_ordenados(diccionario_resultado)

def calcularPeorVariable(solucionActual, gananciaSolucionActual,eliminados, k):
    tam = len(solucionActual)
    for i in range(tam-1):
        solucionTemporal = solucionActual[:]
        solucionTemporal.remove(solucionTemporal[i])
        atributosDeLaSolucionTemp = datos[solucionTemporal]
        gananciaSolucionTemp = promedio.evaluacionRobusta.validacionCruzada(datos,atributosDeLaSolucionTemp, 20, 10)
        k +=1
        if(gananciaSolucionTemp>gananciaSolucionActual):
            k=0
            eliminados.append(solucionTemporal[i])
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


def datos_ordenados(diccionario_resultado):
    diccionario_sorted = sorted(diccionario_resultado.items(),key=operator.itemgetter(0),reverse=True)
    print('{:<10}{:>100} {:>30}'.format('Soluciones','Rendimiento','Tamaño'))
    for element in diccionario_sorted:       
        print(element[1], ' con una ganancia de: ',element[0], ' con tamaño:', len(element[1]))

print(SFFS(datos, variable_predictora))
    
    
    