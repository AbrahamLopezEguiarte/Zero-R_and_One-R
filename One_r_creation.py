# Se importan los módulos pandas (para abrir el archivo csv y poder realizar operaciones con este), random para poder crear
# la descripción del modelo con One-R en caso de que haya un empate en la cantidad de instancias con el mismo valor de la clase
# y os para poder hacer un refresco en la terminal y darle un aspecto más estético
import pandas as pd
import random
import os
# Definimos la función open_and_create_csv la cual nos servirá para abrir el csv original y con este crear un nuevo archivo
# que utilizaremos para utilizar el algoritmo de one-r
def open_and_create_csv():
	# Se crea un string vacío el cual servirá para crear la descripción del modelo con One-R
	value = ''
	# Abrimos el archivo cancer.csv y lo asignamos a la variable df. A su vez, ignoramos las filas 2 y 3 las cuales
	# contienen información que no nos es de utilidad para implementar nuestros algoritmos
	df = pd.read_csv("cancer.csv", skiprows=[1,2])
	# Imprimimos su contenido para verificar que se haya abierto correctamente
	print(df)
	# Reemplazamos los guiones medios por guiones bajos para poder manipular la información correctamente
	df['recurrence'] = df['recurrence'] .str.replace('-', '_')
	# Sobreescribimos nuestro archivo para guardar los cambios agregados. En caso de ya existir el archivo cancer_one_r
	# lo sobreescribirá también
	df.to_csv ("cancer_one_r.csv", index = False, header=True)
	print('New file created')
	os.system('pause')
	os.system('cls')