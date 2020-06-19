# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:06:21 2020

@author: amine
"""
from evaluacion_robusta_variables import evaluacion_robusta as evaluacion
from imprimir_datos_ordenados import Imprimir

class SFFS(): 
    
    def algoritmo_sffs(datos,variable_predictora):
        variables = datos.columns.tolist()
        variable_predictora = variables[-1]
        variables.remove(variable_predictora)
        solucion_actual = []
        añadidas = []
        eliminadas = []
        diccionario_resultado = {}
        k = 0
        lista_solucion = []
        lista_ganancia = []
        print('Mostrando Traza ...')
        while len(añadidas) < len(variables): 
            mejor_variable,mejor_solucion_temporal,rendimiento = SFFS.calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual,15,10,añadidas)
            solucion_actual = mejor_solucion_temporal[:]
            añadidas.append(mejor_variable)
            print('La solucion antes de eliminar es ',solucion_actual,'con ganancia de ',rendimiento)
            if(len(solucion_actual)<=2):
                lista_solucion.append(solucion_actual[:])
                lista_ganancia.append(rendimiento)
                diccionario_resultado[rendimiento] = solucion_actual[:]
                k += 1
            if(len(solucion_actual)>2):
                peor_variable,nuevo_rendimiento,solucion_temporal = SFFS.calcular_peor_variable(datos,variable_predictora,solucion_actual,eliminadas)
                print('La peor variable es ',peor_variable,' y el rendimiento al quitarla', nuevo_rendimiento,' la solucion temporal ',solucion_temporal)
                if (nuevo_rendimiento>=rendimiento):    
                    k=0  
                    solucion_actual = solucion_temporal[:]
                    rendimiento = nuevo_rendimiento
                    eliminadas.append(peor_variable)
                    diccionario_resultado[rendimiento] = solucion_actual[:]
                    lista_solucion.append(solucion_actual[:])
                    lista_ganancia.append(rendimiento)
                    print('Solucion tras eliminar es ',solucion_actual,'con ganancia de ',rendimiento,'\n')
                else:    
                    lista_solucion.append(solucion_actual[:])
                    lista_ganancia.append(rendimiento)
                    diccionario_resultado[rendimiento] = solucion_actual[:]
                    print('Solucion sin eliminar es ',solucion_actual,'con ganancia de ',rendimiento,'\n')
                    k += 1
            #Comprobamos la condicion de parada
            if k>=10:
                    print('El programa ha terminado condicion de parada cumplida',k)
                    break
        print('Lista de añadidas ', añadidas)
        print('Lista de eliminadas ', eliminadas,'\n')
        
        for i in range(len(lista_solucion)):
            print('Solucion ',lista_solucion[i],' con ganancia ', lista_ganancia[i], ' con tamaño', len(lista_solucion[i]))
        print('Fin de la Traza.')
        return Imprimir.datos_ordenados(diccionario_resultado)
    
    def calcular_peor_variable(datos,variable_predictora,solucion_actual,eliminadas):
        tam = len(solucion_actual)
        solucion_temporal = solucion_actual[:]
        i = 0
        rendimiento_res = 0
        while i <= tam-1:
            variable = solucion_actual[i]
            if(variable not in eliminadas):
                solucion_temporal.remove(variable)
                atributos_a_probar = datos[solucion_temporal]
                nuevo_rendimiento = evaluacion.validacion_cruzada(datos,atributos_a_probar,15,10)
                if(nuevo_rendimiento>rendimiento_res):
                    peor_variable = variable
                    rendimiento_res = nuevo_rendimiento
                else:
                    i += 1
                solucion_temporal = solucion_actual[:]
                i += 1
            else:
                i += 1
        solucion_temporal.remove(peor_variable)
        return peor_variable,rendimiento_res,solucion_temporal    
        
    def calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual,N_Exp,CV,añadidas):
        tam = len(variables)
        ac = 0
        solucion_temporal = solucion_actual[:]
        i = 0
        while i <= tam-1:
            variable = variables[i]
            if((variable not in solucion_actual) and (variable not in añadidas)):
                solucion_temporal.append(variable)
                atributos_a_probar = datos[solucion_temporal]
                rendimiento = evaluacion.validacion_cruzada(datos,atributos_a_probar,N_Exp,CV)
                if(rendimiento > ac):
                    mejor_variable = variable
                    ac = rendimiento
                    solucion_temporal.remove(variable)
                    i += 1
                else: 
                    i += 1
                    solucion_temporal.remove(variable)
            else:
                i += 1
        solucion_temporal.append(mejor_variable)
        return mejor_variable,solucion_temporal,ac
