# -*- coding: utf-8 -*-

import evaluacion_robusta_variables as promedio
import imprimir_datos_ordenados as impdatos

#archivo = input('Introduce el nombre del archivo ( Puede ser titanic.csv o BreastCancerDataset): \n')
#datos = pandas.read_csv(archivo,sep=',')
#variables = datos.columns.tolist()
#variable_predictora = variables[-1]
class SFFS():
    
    def algoritmo_sffs(datos,variable_predictora):
        variables = datos.columns.tolist()
        variables.remove(variable_predictora)
        k=0
        i = 0 #Contador para añadir la entrada i de la Lista en el diccionario con la clave ganancia_solucion_actual correspondiente
        añadidas = []
        eliminadas = []
        solucion_actual = []
        tam = len(variables)
        Lista = []
        Lista_ganancias = []
        diccionario_resultado = {}
        print("Traza:")
        archivo = open('resultado.txt','w')
        while len(añadidas) < tam-1: 
            variable_elegida = SFFS.calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual, 15, 10)
            variables.remove(variable_elegida)
            solucion_actual.append(variable_elegida)
            atributos_solucion = datos[solucion_actual]
            ganancia_solucion_actual = promedio.evaluacion_robusta.validacion_cruzada(datos,atributos_solucion, 15, 10)
            añadidas.append(variable_elegida)
            if(len(solucion_actual)<=3):
                Lista.append(solucion_actual[:])
                Lista_ganancias.append(ganancia_solucion_actual)
                diccionario_resultado[ganancia_solucion_actual] = Lista[i]
                k += 1
                i += 1
                archivo.write(str(solucion_actual)+'\n')
            if(len(solucion_actual)>2):
                print('Solucion antes del proceso de eliminacion: ',solucion_actual)
                solucion_nueva,nueva_ganancia,peor_variable,k = SFFS.proceso_de_eliminacion(datos, solucion_actual, variable_predictora, 15, 10, ganancia_solucion_actual,eliminadas,k)
                print('Y la peor variable de todas es: ',peor_variable,'Con ganancia al eliminarla de ',nueva_ganancia)
                print('Y la antigua ganancia es',ganancia_solucion_actual)
                if(nueva_ganancia > ganancia_solucion_actual):
                    print('Por tanto he entrado')
                    ganancia_solucion_actual = nueva_ganancia
                    print('Y la solucion actual queda de la siguiente manera\n:',solucion_actual)                  
                    solucion_actual.remove(peor_variable)
                    Lista.append(solucion_actual[:])
                    Lista_ganancias.append(ganancia_solucion_actual)
                    diccionario_resultado[ganancia_solucion_actual] = Lista[i]
                    print('Diccionario acumulado -->',diccionario_resultado)
                    eliminadas.append(peor_variable)
                    k +=1
                    i +=1
                    archivo.write(str(solucion_actual)+'\n')
        print('Añadidas',añadidas,'\n')
        print('Eliminadas',eliminadas,'\n')
        archivo.close()
        return impdatos.Imprimir.datos_ordenados(diccionario_resultado)
     
    def proceso_de_eliminacion(datos,solucion_actual,variable_predictora,N_Exp,CV,ganancia_solucion_actual,eliminadas,k):
        tam = len(solucion_actual)
#        print('Tamaño proceso eliminacion: ',tam)
        for i in range(tam):
            solucion_temporal = solucion_actual[:]
            peor_variable = solucion_temporal[i]
            solucion_temporal.remove(solucion_temporal[i])
            atributos_de_la_solucion_temp = datos[solucion_temporal]
            ganancia_solucion_temp = promedio.evaluacion_robusta.validacion_cruzada(datos,atributos_de_la_solucion_temp, 15, 10)
#            print('Solucion temporal durante el proceso de eliminacion:',solucion_temporal,' peor variable',peor_variable,'iteracion',i)
            if(peor_variable not in eliminadas):
                if(ganancia_solucion_temp>ganancia_solucion_actual):
                    k=0
                    ganancia_solucion_actual = ganancia_solucion_temp
                if k>=10:
                    break
        solucion_actual = solucion_temporal[:]
        k += 1 
        return solucion_actual,ganancia_solucion_actual,peor_variable,k
        
    def calcular_mejor_variable(datos,variables,variable_predictora,solucion_actual,N_Exp,CV):
        tam = len(variables)
        ac = 0
        solucion_temporal = solucion_actual
        for i in range(tam):
            solucion_temporal.append(variables[i])
            atributos_a_probar = datos[solucion_temporal]
            ganancia_del_atributo = promedio.evaluacion_robusta.validacion_cruzada(datos,atributos_a_probar,N_Exp,CV)
            if(ganancia_del_atributo>ac):
                mejor_variable = variables[i]
                ac = ganancia_del_atributo
            solucion_temporal.remove(variables[i])
        return mejor_variable
"""            
    def calcular_peor_variable(datos,solucion_actual,variable_predictora,N_Exp,CV):
        tam = len(solucion_actual)
        ac = 1 ##Porque como maximo el valor de la ganancia puede ser 1
        solucion_temporal = []
        for i in range(tam): 
            solucion_temporal.append(solucion_actual[i])
            atributos_a_probar = datos[solucion_temporal]
            ganancia_atributo = promedio.evaluacion_robusta.validacion_cruzada(datos,atributos_a_probar,N_Exp,CV)
            if(ganancia_atributo < ac): 
                peor_variable = solucion_actual[i]
                ac = ganancia_atributo
            solucion_temporal.remove(solucion_actual[i])
        return peor_variable
"""
#    print(SFFS(datos, variable_predictora))