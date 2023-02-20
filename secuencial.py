# La programación secuencial se entiende como una metodología que basa 
# su funcionamiento en tener acciones o instrucciones que sigan a 
# otras de forma secuencial. Así pues, en este mecanismo se pueden 
# presentar múltiples operaciones de inicio a fin, así como las 
# operaciones de asignación o de cálculo, entre otras.

# Por lo tanto, para que se pueda entender la programación secuencial,
# es necesario que se conozca el concepto de algoritmo. Este es un
# conjunto de instrucciones que se ejecutan de forma secuencial,
# es decir, una detrás de otra, para resolver un problema.

# Desde el principio hemos programado de forma secuencial, como por
# ejemplo, los bucles for, que se ejecutan de forma secuencial,
# es decir, una instrucción detrás de otra.


### I M P O R T S ###
from multiprocessing import Pool
from time import sleep
import random
import time
from secuencial import *
from colorama import Fore
start = time.time() # Iniciamos el contador de tiempo

### F U N C I O N E S ###
def scrape(url): 
    print("starting", url) # Imprimimos por pantalla el inicio de la url
    duration = round(random.random(),3) # Generamos un numero aleatorio entre 0 y 1 con 3 decimales
    sleep(duration) # Hacemos que el programa se duerma durante el tiempo generado
    print("finished", url, "time taken:", duration, "seconds") # Imprimimos por pantalla el final de la url y el tiempo que ha tardado
    return url, duration # Devolvemos la url y el tiempo que ha tardado


def secuenciall():
    urls = ["a.com", "b.com", "c.com", "d.com"] # variable local
    output = [] # lista vacia
    for url in urls: # recorremos la lista de urls
        result = scrape(url) # llamamos a la funcion scrape
        output.append(result) # añadimos el resultado a la lista vacia

    


