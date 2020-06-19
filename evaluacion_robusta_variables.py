# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:20:00 2020

@author: amine
"""

from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn import tree

class evaluacion_robusta():
    
    def validacion_cruzada(datos,variables,N_Exp,Cv):
         variable_resultado = datos.iloc[:,-1]
         y = variable_resultado
         X_train,X_test,y_train,y_test = model_selection.train_test_split(variables, y, test_size=0.25, random_state=123)
         lista_promedios = []
         #Empezamos en 1 porque max_depth debe ser mayor que 0 y por lo tanto al sumar 1 al principio acabamos 1 iteracion mas tarde N_Exp + 1
         i=1
         while i < N_Exp+1:
             clf = tree.DecisionTreeClassifier(max_depth = i,random_state=123)
             score_val = cross_val_score(estimator=clf,X=X_train,y=y_train,cv=Cv,scoring='balanced_accuracy')
             promedio = score_val.mean()
             lista_promedios.append(promedio)
             i+=1
             if i == N_Exp + 1: 
                 suma_datos = sum(lista_promedios)
                 tam = len(lista_promedios)
                 media_experimentos = suma_datos / tam
         return media_experimentos
    