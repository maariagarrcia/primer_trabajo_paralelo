### I M P O R T S ###
from multiprocessing import Pool
from time import sleep
import random
import time


start = time.time() # Iniciamos el contador de tiempo

### F U N C I O N E S ###
def scrape(url): 
    print("starting", url) # Imprimimos por pantalla el inicio de la url
    duration = round(random.random(),3) # Generamos un numero aleatorio entre 0 y 1 con 3 decimales
    sleep(duration) # Hacemos que el programa se duerma durante el tiempo generado
    print("finished", url, "time taken:", duration, "seconds") # Imprimimos por pantalla el final de la url y el tiempo que ha tardado
    return url, duration # Devolvemos la url y el tiempo que ha tardado


def secuencial():
    urls = ["a.com", "b.com", "c.com", "d.com"] # variable local
    output = [] # lista vacia
    for url in urls: # recorremos la lista de urls
        result = scrape(url) # llamamos a la funcion scrape
        output.append(result) # añadimos el resultado a la lista vacia


end=time.time() # Paramos el contador de tiempo
print("TIEMPO TOTAL: ",end-start) # Imprimimos por pantalla el tiempo total que ha tardado el programa

### M A I N ###
secuencial()


