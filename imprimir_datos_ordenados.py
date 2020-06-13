"""
Created on Fri Jun 12 18:44:19 2020

@author: Amine
"""
import operator

class Imprimir():
    def datos_ordenados(diccionario_resultado):
        diccionario_sorted = sorted(diccionario_resultado.items(),key=operator.itemgetter(1),reverse=True)
        print('{:<10}{:>100} {:>30}'.format('Soluciones','Rendimiento','Tamaño'))
        for element in diccionario_sorted:       
            print(element[1], ' con una ganancia de: ',element[0])