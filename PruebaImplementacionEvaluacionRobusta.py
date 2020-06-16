# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:46:49 2020

@author: amine
"""
import pandas
import evaluacion_robusta_variables as e
import SFFS_en_desarrollo as sffs

datos = pandas.read_csv('titanic.csv',sep=",")

set_ejemplo = {0:'Pclass',1:'SibSp',2:'Is_Married'}
tam = len(set_ejemplo)
df = datos[[set_ejemplo[0],set_ejemplo[tam-2],set_ejemplo[tam-1]]]
atributo = datos[df.columns[0:tam]]
sfsSelected = ['Initial','SibSp','Deck']
dat = datos[sfsSelected]
#print(dat)
set_ejemplo[2] = 'Is_Married'
#print(set_ejemplo)
atributos = datos.loc[:,'SibSp':]
variable_predictora = 'Survived'
N_Exp = 13
Cv=10
#print(e.Evaluacion_robusta.validacion_cruzada(datos,dat,variable_predictora,N_Exp,Cv))
#print(sffs.SFFS.calcular_peor_variable(datos,sfsSelected,variable_predictora))
print(sffs.SFFS.SFFS(datos,variable_predictora))