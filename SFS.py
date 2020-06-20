# -*- coding: utf-8 -*-

import evaluacion_robusta_variables as promedio
import imprimir_datos_ordenados as impdatos


class SFS():
    
    def algoritmo_sfs(datos, variable_predictora, D):
        variables = datos.columns.tolist()
        variables.remove(variable_predictora)
        k=0
        solucion_actual = []
        Lista = []
        diccionario_resultado = {}
        while k<D:
            variable_elegida = SFS.calcular_mejor_variable(datos, variables, variable_predictora, solucion_actual)
            variables.remove(variable_elegida)
            solucion_actual.append(variable_elegida)
            atributos_de_la_solucion = datos[solucion_actual]
            ganancia_solucion_actual = promedio.evaluacion_robusta.validacion_cruzada(datos,atributos_de_la_solucion, 15, 10)
            Lista.append(solucion_actual[:])
            diccionario_resultado[ganancia_solucion_actual] = Lista[k]
            k += 1
        archivo_sfs = impdatos.Imprimir.mostrar_datos_en_html(diccionario_resultado)
        tabla = impdatos.Imprimir.datos_ordenados(diccionario_resultado) 
        return tabla,archivo_sfs


    def calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual):
        tam = len(variables)
        ac = 0
        solucion_temporal = solucion_actual
        for i in range(tam-1):
            solucion_temporal.append(variables[i])
            atributos_a_probar = datos[solucion_temporal]
            ganancia_del_atributo = promedio.evaluacion_robusta.validacion_cruzada(datos,atributos_a_probar,15,10)
            if(ganancia_del_atributo>ac):
                mejor_variable = variables[i]
                ac = ganancia_del_atributo
                solucion_temporal.remove(variables[i])
            else:
                solucion_temporal.remove(variables[i])
        return mejor_variable





