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
         variable_evaluable = datos.iloc[:,-1]
         y = variable_evaluable
         X_train,X_test,y_train,y_test = model_selection.train_test_split(variables, y, test_size=0.25, random_state=123)
         lista_promedios = []
         #Empezamos en 1 porque max_depth debe ser mayor que 0 y por lo tanto al sumar 1 al principio acabamos 1 iteracion mas tarde N_Exp + 1
         i=1
         while i < N_Exp+1:
             clf = tree.DecisionTreeClassifier(max_depth = i,random_state=123)
             score_val = cross_val_score(estimator=clf,X=X_train,y=y_train,cv=Cv,scoring='balanced_accuracy')
             lista_promedios.append(score_val)
             i+=1
         promedio = evaluacion_robusta.calculo_del_promedio(lista_promedios,Cv)
         return promedio
     
    def calculo_del_promedio(lista_promedios,Cv):
#
        datos = sum(lista_promedios)
        len_lista = float(len(lista_promedios))
#        print('El tamaño es',len_lista,'\n')
        intermedio = datos / len_lista
#        print('El conjunto intermedio',intermedio,'\n')
        suma_datos = sum(intermedio)
#        print('La suma de datos es:',suma_datos)
        promedio = suma_datos / Cv
#        print('El resultado es:',promedio)
        return promedio