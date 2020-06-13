# -*- coding: utf-8 -*-
import pandas as pd
import evaluacionRobusta as promedio


datos = pd.read_csv('titanic.csv',sep=",")
Lista = [['Initial'], ['Initial'], ['Initial', 'SibSp'], ['Initial', 'SibSp', 'Deck'], ['Initial', 'SibSp', 'Deck', 'Embarked']]


def ordenarLista(datos, Lista):
    k = 0
    Lista2 = []
    for i in Lista:
        if i not in Lista2:
            Lista2.append(i) 
    tam = len(Lista2)
    while(k != tam-1):
        primerValor = Lista2[k]
        atributosPrimerValor = datos[primerValor]
        ganPrimerValor = promedio.evaluacionRobusta.validacionCruzada(datos,atributosPrimerValor, 15, 10)
        
        segundoValor = Lista2[k+1]
        atributosSegundoValor = datos[segundoValor]
        ganSegundoValor = promedio.evaluacionRobusta.validacionCruzada(datos,atributosSegundoValor, 15, 10)
        
        if(ganPrimerValor>ganSegundoValor):
            k+=1
        else:
            Lista2.remove(primerValor)
            Lista2.remove(segundoValor)
            Lista2.insert(k,segundoValor)
            Lista2.insert(k+1, primerValor)
            k=0
    return Lista2

print("Lista:" + str(ordenarLista(datos, Lista)))