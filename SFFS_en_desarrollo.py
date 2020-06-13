# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:58:09 2020

@author: amine
"""
import pandas 
import evaluacionRobusta as promedio
import tabulate

datos = pandas.read_csv('titanic.csv',sep=',')
variables = datos.columns.tolist()
variable_predictora = variables[-1]

class SFFS():

    def SFFS(datos,variable_predictora,N_Exp,CV):
        variables = datos.columns.tolist()
        variables.remove(variable_predictora)
        k=0
        añadidas = []
        eliminadas = []
        solucion_actual = []
        solucion_temporal = []
        tam = len(variables)
        print('{:<10}{:>80} {:>10}'.format('Soluciones','Rendimiento','Tamaño'))
        while len(añadidas) < tam-1: 
            variable_elegida = SFFS.calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual,N_Exp,CV)
            if(variable_elegida not in solucion_actual and variable_elegida not in añadidas):
                variables.remove(variable_elegida)
                solucion_actual.append(variable_elegida)
                atributos_solucion = datos[solucion_actual]
                ganancia_solucion_actual = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_solucion,N_Exp,CV)
                añadidas.append(variable_elegida)
                print('{}{:>80.2f}{:>10}'.format(solucion_actual, ganancia_solucion_actual, len(solucion_actual)))
                if(len(solucion_actual)>2):
                    print('HE ENTRADO')
                    solucion_actual,ganancia_solucion_actual,eliminadas = SFFS.proceso_de_eliminacion(datos,solucion_actual,
                                                                                                      variable_predictora,N_Exp,CV,ganancia_solucion_actual,eliminadas)
                    print('{}{:>80.2f}{:>10}'.format(solucion_actual, ganancia_solucion_actual, len(solucion_actual)))
            print('Añadidas = ', añadidas,'Eliminadas = ',eliminadas)
     
    def proceso_de_eliminacion(datos,solucion_actual,variable_predictora,N_Exp,CV,ganancia_solucion_actual,eliminadas):
        solucion_temporal = solucion_actual[:]
        peor_variable = SFFS.calcular_peor_variable(datos,solucion_actual,variable_predictora,N_Exp,CV)
        solucion_temporal.remove(peor_variable)
        atributos_sin_peor_variable = datos[solucion_temporal]
        nueva_ganancia = promedio.evaluacionRobusta.validacionCruzada(datos,atributos_sin_peor_variable,N_Exp,CV)
        if(nueva_ganancia > ganancia_solucion_actual): 
            solucion_actual = solucion_temporal
            ganancia_solucion_actual = nueva_ganancia
            eliminadas.append(peor_variable)
        else: 
            solucion_temporal = solucion_actual[:]
        return solucion_actual,ganancia_solucion_actual,eliminadas
        
        
        
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
            else:
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
            else:
                solucion_temporal.remove(solucion_actual[i])
        return peor_variable
