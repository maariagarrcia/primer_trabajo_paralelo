# leer csv

import csv
import os
from colorama import Fore



# leer solo las priemras 11  filas
def leer_csv():
    archivo = open('data.csv')
    reader = csv.reader(archivo, delimiter=',')
    for row in reader:
        print(row)
        if reader.line_num == 11:
            break




def leer_csv1():
    archivo = open('data.csv')
    reader = csv.reader(archivo, delimiter=',')
    for row in reader:
        pass
    print(row)

def iniciar():

    print(Fore.YELLOW+"Hemos recogido los datos siguientes que hacen referencia a los 10 primeros tiempos que ha tardado el programa en ejecutarse en paralelo y en secuencial: " + Fore.WHITE)
    leer_csv()
    print()
    
    print(Fore.YELLOW+"Hemos hecho la media de los datos anteriores para demostrar que programar en paralelo nos ahorra tiempo: "+ Fore.WHITE)
    leer_csv1()
    