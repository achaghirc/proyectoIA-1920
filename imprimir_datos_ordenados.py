import pandas
import operator
pandas.set_option('max_colwidth', 800)
pandas.set_option('max_columns', None)


class Imprimir():
    
    def mostrar_datos_en_html(datos):
        datos_tabla = [['Mejor Solucion', 'Tamaño', 'Rendimiento']]
        claves = datos.keys()
        
        for clave in claves: 
            valor = datos[clave]
            length  = len(valor)
            datos_tabla = datos_tabla + [[valor,length,clave]]
        archivo_html = pandas.DataFrame(datos_tabla)
        return archivo_html.to_html()
    
    
    def datos_ordenados(diccionario_resultado):
        diccionario_sorted = sorted(diccionario_resultado.items(),key=operator.itemgetter(0),reverse=True)
        print('\n\t\t\t SOLUCION GUARDADA: ')
        Lista = []
        ListaPrueba = diccionario_sorted[:]
        tam = len(ListaPrueba)
        for i in range(tam-1):
            elemento = ListaPrueba[i]
            if elemento[1] not in Lista:
                Lista.append(elemento[1][:])
            else:
                diccionario_sorted.remove(elemento)
        df = [['Mejor Solucion','Tamaño','Rendimiento']]
        for element in diccionario_sorted:
            df = df + [[str(element[1]),len(element[1]),element[0]]]
        data_frame = pandas.DataFrame(df)
        return data_frame
