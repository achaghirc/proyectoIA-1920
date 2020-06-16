# -*- coding: utf-8 -*-

import pandas 
import evaluacionRobusta as promedio
import imprimir_datos_ordenados as impdatos


datos = pandas.read_csv('cars.csv',sep=',')
variables = datos.columns.tolist()
variable_predictora = variables[-1]

def SFFS(datos,variable_predictora):
    variables = datos.columns.tolist()
    variables.remove(variable_predictora)
    k=0
    añadidas = []
    eliminadas = []
    solucion_actual = []
    tam = len(variables)
    Lista = []
    Lista_ganancias = []
    diccionario_resultado = {}
    while len(añadidas) < tam-1: 
        variable_elegida = calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual, 15, 10)
        variables.remove(variable_elegida)
        solucion_actual.append(variable_elegida)
        atributos_solucion = datos[solucion_actual]
        ganancia_solucion_actual = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_solucion, 15, 10)
        añadidas.append(variable_elegida)
        if(len(solucion_actual)<=2):
            Lista.append(solucion_actual[:])
            Lista_ganancias.append(ganancia_solucion_actual)
            diccionario_resultado[ganancia_solucion_actual] = Lista[k]
            k += 1
        if(len(solucion_actual)>2):
            solucion_nueva,nueva_ganancia,peor_variable = proceso_de_eliminacion(datos, solucion_actual, variable_predictora, 15, 10, ganancia_solucion_actual,eliminadas,k)
            if(nueva_ganancia > ganancia_solucion_actual):
                ganancia_solucion_actual = nueva_ganancia
                solucion_actual.remove(peor_variable)
                Lista.append(solucion_actual[:])
                Lista_ganancias.append(ganancia_solucion_actual)
                diccionario_resultado[ganancia_solucion_actual] = Lista[k]
                eliminadas.append(peor_variable)
                k +=1
    return impdatos.Imprimir.datos_ordenados(diccionario_resultado)
     
def proceso_de_eliminacion(datos,solucion_actual,variable_predictora,N_Exp,CV,ganancia_solucion_actual,eliminadas,k):
    tam = len(solucion_actual)
    for i in range(tam-1):
        solucion_temporal = solucion_actual[:]
        peor_variable = solucion_temporal[i]
        solucion_temporal.remove(solucion_temporal[i])
        atributos_de_la_solucion_temp = datos[solucion_temporal]
        ganancia_solucion_temp = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_de_la_solucion_temp, 15, 10)
        k +=1
        if(peor_variable not in eliminadas):
            if(ganancia_solucion_temp>ganancia_solucion_actual):
                k=0
                ganancia_solucion_actual = ganancia_solucion_temp     
            if k>=10:
                break
    solucionActual = solucion_temporal[:]
    return solucionActual,ganancia_solucion_actual,peor_variable
        
def calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual,N_Exp,CV):
    tam = len(variables)
    ac = 0
    solucion_temporal = solucion_actual
    for i in range(tam-1):
        solucion_temporal.append(variables[i])
        atributos_a_probar = datos[solucion_temporal]
        ganancia_del_atributo = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_a_probar,N_Exp,CV)
        if(ganancia_del_atributo>ac):
            mejor_variable = variables[i]
            ac = ganancia_del_atributo
        solucion_temporal.remove(variables[i])
    return mejor_variable
                
def calcular_peor_variable(datos,solucion_actual,variable_predictora,N_Exp,CV):
    tam = len(solucion_actual)
    ac = 1 ##Porque como maximo el valor de la ganancia puede ser 1
    solucion_temporal = []
    for i in range(tam): 
        solucion_temporal.append(solucion_actual[i])
        atributos_a_probar = datos[solucion_temporal]
        ganancia_atributo = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_a_probar,N_Exp,CV)
        if(ganancia_atributo < ac): 
            peor_variable = solucion_actual[i]
            ac = ganancia_atributo
        solucion_temporal.remove(solucion_actual[i])
    return peor_variable

print(SFFS(datos, variable_predictora))