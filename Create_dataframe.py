# Se importa train_test_split del módulo sklearn el cual nos ayudará a dividir nuestro dataframe en el porcentaje deseado.
# En este caso se opta por 70:30. A su vez se importa pandas para abrir nuestros archivos y os para refrescar la terminal
# y darle un aspecto más estético
from re import T
from turtle import mode
from pip import List
from sklearn.model_selection import train_test_split
import pandas as pd
import os

# Se crea la función dataframe_zerro_r la cual nos servirá para dividir nuestro archivo específico para zero-r en un
# porcentaje de 70:30. Siendo 70% para entrenamiento y 30% para prueba
def dataframe_zero_r(iterations):
    # Utilizamos try except para evitar fallos por falta del archivo requerido para funcionar
    try:
        # Se declaran tres variables. aux_train  y aux_test nos ayudarán a calcular la exactitud total de todas las
        # iteraciones. iteration nos ayudará a llevar un control de la cantidad de iteraciones realizadas
        aux_train = 0
        aux_test = 0
        iteration = 1
        df = pd.read_csv("cancer_zero_r.csv")
        df['model'] = df['model'] .str.replace('-', '_')
        while(iteration <= iterations):
            print('\nIteration number: '+str(iteration))
            # Las variables train y test se asignan a la función train_test_split la cual recibe nuestro archivo y una variable
            # con el porcentaje que deseamos para cada uno de los subconjuntos. En este caso indicamos un tamaño de 0.3 para que
            # divida el conjunto en 70:30. A su vez, el conjunto entero se aleatoriza antes de dividrse
            train, test = train_test_split(df, test_size=0.3)
            # Se imprime el subconjunto train y test para poder visualizar la cantidad de filas y verificar que se realizaran
            # correctamente ambos subconjuntos
            print(train)
            print(test)
            print('\n')
            # En ambos subconjuntos se crean nuevas columnas en cada iteración la cual contendrá el valor True o False,
            # dependiendo de si el valor deñ atributo recurrence es igual al del atributo model
            train["errors"] = train["recurrence"] == train["model"]
            test["errors"] = test["recurrence"] == test["model"]
            # Como los valores del nuevo atributo son booleanos se intercambian estos valores por otros de tipo string
            mask = train.applymap(type) != bool
            d = {True: 'TRUE', False: 'FALSE'}
            train = train.where(mask, train.replace(d))
            mask = test.applymap(type) != bool
            d = {True: 'TRUE', False: 'FALSE'}
            test = test.where(mask, test.replace(d))
            # Una vez convertidos a tipo string podemos contabilizar la cantidad de veces que el algoritmo funcionó en
            # ambos subconjuntos para poder calcular la exactitud
            hits_train = train.errors.value_counts().TRUE
            hits_test = test.errors.value_counts().TRUE
            print('Total hits in train subset: '+str(hits_train))
            print('Total hits in test subset: '+str(hits_test)+'\n')
            # Para calcular la exactitud de Zero-R en la iteración en cuestión se divide la cantidad de aciertos entre
            # la cantidad de sentencias del subconjunto y este resultado se multiplica por 100
            print('Accuracy in train subset: '+str("{:.2f}".format((hits_train/train.shape[0])*100))+'%')
            print('Accuracy in test subset: '+str("{:.2f}".format((hits_test/test.shape[0])*100))+'%')
            print('\n\n')
            # Se suma el porcentaje obtenido en la iteración a nuestras variables auxiliares
            aux_train += (hits_train/train.shape[0])*100
            aux_test += (hits_test/test.shape[0])*100
            os.system('pause')
            iteration += 1
        os.system('cls')
        # Obtenemos la exactitud total dividiendo nuestras variables auxiliares entre la cantidad de iteraciones realizadas
        total_accuracy_train = aux_train/iterations
        total_accuracy_test = aux_test/iterations
        print('The total accuracy of Zero-R with a train subset is: '+str("{:.2f}".format(total_accuracy_train))+'%')
        print('The total accuracy of Zero-R with a test subset is: '+str("{:.2f}".format(total_accuracy_test))+'%')
        os.system('pause')
        os.system('cls')
    except FileNotFoundError:
        print("The file 'cancer_zero_r.csv' wasn't found. Check that it is in the right directory or create it first")
        os.system('pause')
        
def dataframe_one_r(iterations):
     # Utilizamos try except para evitar fallos por falta del archivo requerido para funcionar
    try:
        aux_train = 0
        aux_test = 0
        #declaramos una variable para contar las iteraciones y creamos una variable para almacenar el archivo csv
        iteration = 1
        df = pd.read_csv("cancer_one_r.csv")
        #ejecutar el numero de iteraciones indicado
        while(iteration <= iterations):
            #Imprimimos la iteration actual
            print('Iteration number: '+str(iteration))
            #Creamos una lista para almacenar el nombre de cada columna excluyendo la clase
            columnas = df.columns.tolist()
            columnas.pop()
            #Creamos un contador para la posicion de la lista
            contColumns = 0
            #Creamos una lista para almacenar el modelo cuando lo encontremos y su nombre en otra variable
            modelo = []
            nombreModelo = ''
            #Creamos una variable para almacenar el menor numero de errores sobre la regla
            ErrorReglaAux = 1
            #Pasamos por cada instancia
            for i in columnas:
                nombreColumna = columnas[contColumns]
                #creamos una lista con las instancias en la columna ordenadas del valor mas bajo al mas alto
                ListGuide = df[columnas[contColumns]].value_counts().sort_index(ascending=True).keys().tolist()
                #Creamos una variable contador para pasar por cada valor de la instancia
                contValor = 0
                #Creamos una lista para comparar las reglas como si fueran tablas de frecuencia
                eleccion = []
                #Creamos variable para carlcular los errores sobre la regla
                ErrorRegla = 0
                #Pasamos por cada atributo
                for j in ListGuide:
                    #Creamos un indice para apoyarnos en el siguiente for
                    contadorIndex = 0
                    #Creamos variables para contar cuantas veces es recurrente la clase o no
                    VTrue = 0
                    VFalse = 0
                    #Creamos una lista como condicional si el valor de la instancia en su misma fila de la clase es recurrente o no
                    ageList = df[nombreColumna].astype(str) + ' -> ' + df['recurrence']
                    #Hacemos las comparaciones
                    for i in ageList:
                        #Sumamos puntos a la variable correspondiente
                        if(ageList[contadorIndex] == str(ListGuide[contValor]) + ' -> no_recurrence_events'):
                            VFalse += 1
                        elif(ageList[contadorIndex] == str(ListGuide[contValor]) + ' -> recurrence_events'):
                            VTrue += 1
                        #Aumentamos el indice
                        contadorIndex += 1
                    #si fue mas veces no recurrente agregamos a la lista de seleccion su nombre y como regla ponemos que no fue recurrente, se aplica el caso contrario en else
                    #Dependiendo de la regla que le asignemos iremos sumando cada vez que hubo errores de esta misma sumando el VTrue de cada instancia en el atributo
                    if(VFalse > VTrue):
                        eleccion.append(str(ListGuide[contValor]) + ' -> no_recurrence_events')
                        ErrorRegla = ErrorRegla + VTrue
                    else:
                        eleccion.append(str(ListGuide[contValor]) + ' -> recurrence_events')
                        ErrorRegla = ErrorRegla + VFalse
                    #Aumentamos el contador de valor
                    contValor += 1
                ErrorRegla = ErrorRegla / contadorIndex
                #Si el error de la regla del atributo actual es menor a Aux, Aux tomara su valor actual, el modelo sera la lista de eleccion actual y su nomnbre, el nombre de la columna
                if(ErrorRegla < ErrorReglaAux):
                    ErrorReglaAux = ErrorRegla
                    modelo = eleccion
                    nombreModelo = nombreColumna
                #Aumentamos el contador de columnas
                contColumns += 1
            #Imprimimos el nombre del modelo (atributo elegido)
            if iteration == 1:
                print('Model:\nAttribute: ', nombreModelo, '\n')
                #Imprimimos nuestra lista que es nuestro modelo
                cont = 0
                for i in modelo:
                    print(modelo[cont])
                    cont += 1
                #Imprimimos porcentaje de error del modelo con formato de solo dos decimales
                print('\nErrors in the rule: ', "{:.2f}".format(ErrorReglaAux*100), '%')
                #Pausamos para continuar
                os.system('pause')
                os.system('cls')
            #Dividimos el archivo total en train que equivale a un 70% y test en un 30%
            train, test = train_test_split(df, test_size=0.3)
            print(train)
            print(test)  
            print('\n') 
            contTrain = 0
            valoresTotal=0
            ReglaTrue=0
            trainList = train[nombreModelo].astype(str) + ' -> ' + train['recurrence']
            trainList = trainList.tolist()
            for i in trainList:
                contModelo = 0
                MuestraValorLista = str(trainList[contTrain])
                for j in modelo:    
                    if(trainList[contTrain] == str(modelo[contModelo])):
                        MuestraValorLista = MuestraValorLista + ' True'
                        ReglaTrue+=1
                    contModelo+=1
                contTrain+=1
                valoresTotal+= 1
            print('Total hits in train subset:', ReglaTrue, '/', valoresTotal)
            ErrorTrain = ReglaTrue/valoresTotal
            #Creamos contadores para el ciclo, para el numero de valores y el total de veces que se cumple la regla
            contTest = 0
            valoresTotal=0
            ReglaTrue=0
            #Creamos una lista con los valores del dataframe de test solo tomando en cuenta el modelo y recurrencia
            testList = test[nombreModelo].astype(str) + ' -> ' + test['recurrence']
            testList = testList.tolist()
            for i in testList:
                #Creamos un contador para el modelo
                contModelo = 0
                #Creamos un string con el valor actual de la lista de test
                MuestraValorLista = str(testList[contTest])
                for j in modelo:
                    #Comparamos por cada valor del modelo si el valor actual cumple con alguna de las reglas, de ser asi le agregamos True al string y aumentamos ReglaTrue
                    if(testList[contTest] == str(modelo[contModelo])):
                        MuestraValorLista = MuestraValorLista + ' True'
                        ReglaTrue+=1
                    contModelo+=1
                contTest+=1
                valoresTotal+= 1
            #Imprimimos el numero de veces que fue correcta la regla sobre el total de valores de la lista
            print('Total hits in test subset:', ReglaTrue, '/', valoresTotal)
            #Asignamos una variable con el porcentaje de exito       
            ErrorTest = ReglaTrue/valoresTotal
            #Imprimimos el porcentaje de exito de test y train
            print('\nAccuracy in train subset: ' "{:.2f}".format(ErrorTrain*100), '%')
            print('Accuracy in test subset: ' "{:.2f}".format(ErrorTest*100), '%\n')
            aux_train += (ErrorTrain)*100
            aux_test += (ErrorTest)*100          
            #Aumentamos el contador de iteraciones
            iteration += 1
            #Pausamos para continuar
            os.system('pause')
        os.system('cls')
        # Obtenemos la exactitud total dividiendo nuestras variables auxiliares entre la cantidad de iteraciones realizadas
        total_accuracy_train = aux_train/iterations
        total_accuracy_test = aux_test/iterations
        print('The total accuracy of Zero-R with a train subset is: '+str("{:.2f}".format(total_accuracy_train))+'%')
        print('The total accuracy of Zero-R with a test subset is: '+str("{:.2f}".format(total_accuracy_test))+'%')
        os.system('pause')
        os.system('cls')
    except FileNotFoundError:
        print("The file 'cancer_zero_r.csv' wasn't found. Check that it is in the right directory or create it first")
        os.system('pause')