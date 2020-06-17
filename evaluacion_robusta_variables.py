# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:20:00 2020

@author: amine
"""

from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

class evaluacion_robusta():
    
    def validacion_cruzada(datos,variables,N_Exp,Cv):
         variable_evaluable = datos.iloc[:,-1]
         y = variable_evaluable
         X_train,X_test,y_train,y_test = model_selection.train_test_split(variables, y, test_size=0.25, random_state=123)
         score_val = cross_val_score(RandomForestClassifier(n_estimators=N_Exp,random_state=123),X=X_train,y=y_train,cv=Cv,scoring='balanced_accuracy')
         promedio = score_val.mean()
         return promedio