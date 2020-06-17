
import operator

class Imprimir():
#SFS    diccionario_resultado = {0.783015649294719: ['Initial'], 0.783015649294719: ['Initial'], 0.8003290099220333: ['Initial', 'SibSp'], 0.8109964540197098: ['Initial', 'SibSp', 'Deck'], 0.814634020157276: ['Initial', 'SibSp', 'Deck', 'Title']}
#SFFS    diccionario_resultado = {0.783015649294719: ['Initial'], 0.8003290099220333: ['Initial', 'SibSp'], 0.8109964540197098: ['Initial', 'SibSp', 'Deck'], 0.814634020157276: ['Initial', 'SibSp', 'Deck', 'Title'], 0.8140808696041255: ['Initial', 'SibSp', 'Deck', 'Title', 'Embarked'], 0.8222903173484569: ['Initial', 'SibSp', 'Deck', 'Title'], 0.8121592447173842: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex'], 0.8143357718939115: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone'], 0.8089389185319418: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat'], 0.8048804769735002: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size'], 0.7995231942906361: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size', 'Pclass'], 0.7905153416781324: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size', 'Pclass', 'Age_band'], 0.8011994250366344: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size', 'Pclass'], 0.7863113415438997: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size', 'Pclass', 'Parch'], 0.7797421893352126: ['Initial', 'SibSp', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size', 'Pclass', 'Fare'], 0.7940410472387216: ['Initial', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size', 'Pclass', 'Fare'], 0.7788548553083438: ['Initial', 'Deck', 'Title', 'Sex', 'Alone', 'Fare_cat', 'Family_Size', 'Pclass', 'Fare', 'Age']}
  
    def datos_ordenados(diccionario_resultado):
        diccionario_sorted = sorted(diccionario_resultado.items(),key=operator.itemgetter(0),reverse=True)
#        print('{:<10}{:>100} {:>30}'.format('Soluciones','Rendimiento','Tamaño'))
        print('\n Solución:')
        Lista = []
        ListaPrueba = diccionario_sorted[:]
        tam = len(ListaPrueba)
        for i in range(tam-1):
            elemento = ListaPrueba[i]
            if elemento[1] not in Lista:
                Lista.append(elemento[1][:])
            else:
                diccionario_sorted.remove(elemento)
                
        for element in diccionario_sorted:       
            print('===============================================================================================================================')
            print(element[1], ' con una ganancia de: ',element[0], ' con tamaño ',len(element[1]))
            
#    print(datos_ordenados(diccionario_resultado))