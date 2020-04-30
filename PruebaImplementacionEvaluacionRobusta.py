# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:46:49 2020

@author: amine
"""
import pandas
import evaluacion_robusta_variables as e

datos = pandas.read_csv('titanic.csv',sep=",")
atributos = datos.loc[:,'Pclass':'Is_Married']
N_Exp = 1
Cv=5

print(e.Evaluacion_robusta.validacion_cruzada(datos,atributos,N_Exp,Cv))
