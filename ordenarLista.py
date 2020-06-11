# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 00:44:19 2020

@author: Alvaro
"""
import pandas as pd
import evaluacionRobusta as promedio

datos = pd.read_csv('titanic.csv',sep=",")
Lista = [['Initial'], ['Initial', 'SibSp'], ['Initial', 'SibSp', 'Deck'], ['Initial', 'SibSp', 'Deck', 'Embarked']]


def ordenarLista(datos, Lista):
    k = 0
    tam = len(Lista)
    while(k != tam-1):
        primerValor = Lista[k]
        atributosPrimerValor = datos[primerValor]
        ganPrimerValor = promedio.evaluacionRobusta.validacionCruzada(datos,atributosPrimerValor, 15, 10)
        print("Primer Valor:" + str(primerValor))
        print("Ganancia Primer Valor:" + str(ganPrimerValor))
        
        segundoValor = Lista[k+1]
        atributosSegundoValor = datos[segundoValor]
        ganSegundoValor = promedio.evaluacionRobusta.validacionCruzada(datos,atributosSegundoValor, 15, 10)
        print("Primer Valor:" + str(segundoValor))
        print("Ganancia Primer Valor:" + str(ganSegundoValor))
        
        if(ganPrimerValor>ganSegundoValor):
            k+=1
        else:
            Lista.remove(primerValor)
            Lista.remove(segundoValor)
            Lista.insert(k,segundoValor)
            Lista.insert(k+1, primerValor)
            k=0
    return Lista

print("Lista:" + str(ordenarLista(datos, Lista)))