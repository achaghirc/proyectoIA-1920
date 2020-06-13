# -*- coding: utf-8 -*-

from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


class evaluacionRobusta():
    
    def validacionCruzada(datos, variables, N_Exp, Cv):
         variable_evaluable = datos.iloc[:,-1]
         y = variable_evaluable
         X_train,X_test,y_train,y_test = model_selection.train_test_split(variables, y, test_size=0.2, random_state=123)
         score_val = cross_val_score(RandomForestClassifier(n_estimators=N_Exp,random_state=123),X=X_train,y=y_train,cv=Cv,scoring='balanced_accuracy')
         promedio = score_val.mean()
         return promedio
