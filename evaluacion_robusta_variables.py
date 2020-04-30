# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:20:00 2020

@author: amine
"""

import pandas
from sklearn import datasets,svm, metrics,preprocessing, model_selection
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

class Evaluacion_robusta():
    
    def obtener_promedio(datos,atributos,N_Exp,Cv):
        
            y = datos.iloc[:,'Survived'].values
        
       # objetivo = datos['Survived']
       # codific_atributos = preprocessing.OrdinalEncoder()
       # codific_atributos.fit(atributos)
       # codific_atributos.fit(atributos)
       # atributos_codific = codific_atributos.transform(atributos)
       # codific_objetivo = preprocessing.LabelEncoder()
       # objetivo_codificado = codific_objetivo.fit_transform(objetivo)
            X_train,X_test,y_train,y_test = model_selection.train_test_split(atributos,y,test_size=0,random_state=0)
       # datos_entrenados = svm.SVC(kernel='linear', C=1).fit(X_train,y_train)
       # for i in range(N_Exp):
            clasifier = RandomForestClassifier(n_estimators=300,random_state=0)
            
            score_val = cross_val_score(estimator=classifier,X=X_train,y=y_train,cv=Cv,scoring='balanced_accuracy')
       #     ac = 0
       #     for j in range(len(score_val)):
       #         promedio = ac + score_val[j]
       #         ac = promedio
            print(score_val)
       # print(promedio/len(score_val))
       # return "El promedio de estos atributos es: ",promedio
    def validacion_cruzada(datos,atributos,N_Exp,Cv):
        y = datos.loc[:,'Survived']
        X_train,X_test,y_train,y_test = model_selection.train_test_split(atributos,y,test_size=0.2,random_state=123)
        score_val = cross_val_score(RandomForestClassifier(n_estimators=N_Exp,random_state=0),X=X_train,y=y_train,cv=Cv,scoring='balanced_accuracy')
        ac = 0
        for j in range(len(score_val)):
            score = ac + score_val[j]
            ac = score
        promedio = score/len(score_val)
        return promedio