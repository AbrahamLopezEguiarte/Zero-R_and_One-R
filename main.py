# Se importan los archivos que se utilizarán para organizar el código, de manera que no se tenga todo en un solo archivo
# así como el módulo os para darle un aspecto estético más agradable al código al ejecutarse en consola

import Zero_r_creation, Create_dataframe, One_r_creation
import Zero_r_creation, Create_dataframe
import os

# La variable end_program nos ayudará a mantener abierto el programa mientras el usuario lo desee
end_program = False

# Se crean dos funciones las cuales nos ayudarán a ejecutar un archivo u otro según el usuario lo desee
def create_new_zero_r_model():
    print('Creating new csv for zero-r')
    Zero_r_creation.open_and_create_csv()
        
# Se crean dos funciones las cuales nos ayudarán a ejecutar un archivo u otro según el usuario lo desee
def create_new_one_r_model():
    print('Creating new csv for one-r')
    One_r_creation.open_and_create_csv()

# Se pasa el parámetro iterations para poder realizar las iteraciones que el usuario desee al momento de calcular
# el porcentaje de error de zero-r
def use_train_test_with_zero_r(iterations):
    print('\nUsing train-test with zero-r')
    Create_dataframe.dataframe_zero_r(iterations)
# Se pasa el parámetro iterations para poder realizar las iteraciones que el usuario desee al momento de calcular
# el porcentaje de error de one-r
def use_train_test_with_one_r(iterations):
    print('\nUsing train-test with one-r')
    Create_dataframe.dataframe_one_r(iterations)

# Se crea un ciclo while para mantener abierto el programa mientras el usuario lo desee
while(end_program == False):
    # Utilizamos try except para poder mantener abierto el programa en caso de que, al elegir una opción, el usuario
    # ingrese un valor distinto a un integer, evitando fallos en el código
    try:
        # Se imprime un menú para que el usuario decida lo que desea hacer
        menu = int(input('What do you wanna do now?:\n[0]: Create cancer_zero_r.csv file\n[1]: Create cancer_one_r.csv file\n[2]: Implement zero-r\n[3]: Implement one-r\n[4]: End programm\nSelect an option: '))
        # En caso de elegir la primer opción se creará un nuevo archivo csv para trabajar con el algoritmo de Zero-R
        if menu == 0:
            create_new_zero_r_model()
        elif menu == 1:
            create_new_one_r_model()
        elif menu == 2:
            # En el caso de elegir la segunda opción se pedirá que ingrese la cantidad de iteraciones que desea para
            # Probar el algoritmo de Zero-R. De ser 0, un valor negativo, etc. No se le permitirá al usuario proseguir
            iterations = int(input('\nEnter the number of iterations you want to make: '))
            if iterations > 0:
                use_train_test_with_zero_r(iterations)
            else:
                print('You must enter a valid number of iterations')
                os.system('pause')
                os.system('cls')
        # En caso de elegir la tercer opción cerrará el programa
        elif menu == 3:
            # En el caso de elegir la tercera opción se pedirá que ingrese la cantidad de iteraciones que desea para
            # Probar el algoritmo de One-R. De ser 0, un valor negativo, etc. No se le permitirá al usuario proseguir
            iterations = int(input('\nEnter the number of iterations you want to make: '))
            if iterations > 0:
                use_train_test_with_one_r(iterations)
            else:
                print('You must enter a valid number of iterations')
                os.system('pause')
                os.system('cls')
        # En caso de elegir la tercer opción cerrará el programa
        elif menu == 4:
            print('Bye bye')
            end_program = True 
        else:
            print('That is not an option. Try again')
            os.system('pause')
            os.system('cls')
    except ValueError:
        print('You must use integer to select an option. Try again')
        os.system('pause')
        os.system('cls')
        
        
