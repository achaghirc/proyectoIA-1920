
import operator

class Imprimir():
    def datos_ordenados(diccionario_resultado):
        diccionario_sorted = sorted(diccionario_resultado.items(),key=operator.itemgetter(0),reverse=True)
        print('\n\t\t\t\t\t SOLUCION GUARDADA: ')
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