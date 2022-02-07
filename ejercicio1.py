import os
import pprint

descargas_path = 'C:/Users/Usuario/Downloads'
ficheros = os.listdir(descargas_path)


for fichero in ficheros:

    pprint.pprint(fichero)

