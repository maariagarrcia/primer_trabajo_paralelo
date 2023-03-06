# primer_trabajo_paralelo

# EJERCICIO PARA DEMOSTRAR QUE EL TIEMPO EN PARALELO ES MENOR AL SECUENCIAL

# Codigo en paralelo
 ```
 ### T E O R I A ###
# multiprocessing es un modulo que permite la ejecucion de procesos en paralelo usando subprocesos
# Pool ofrece un medio conveniente para paralelizar la ejecucion de una funcion en multiples entradas, 
# distribuyendo los datos de  entradas a través de procesos.

# Los procesos en unordenador son todos los programas que se estan ejecutando en el momento.
# Todo proceso parte con un solo hilo principal.
# Un proceso esta compuesto por uno o mas hilos que se ejecutan en paralelo.
# Un proceso puede instanciar otros procesos llamados subprocesos.

# Un subproceso es un proceso que se ejecuta dentro de otro proceso. Los subprocesos
# son una opcion para encapsular los pasos relacionados logicamente dentro de un proceso padre.
# Realizan tareas pragmaticas en segundo plano.
# Los subprocesos estan diseñados para  ayudarse entre sí.

### I M P O R T S ###
from multiprocessing import Pool # Importamos el modulo multiprocessing
from time import sleep # Importamos el modulo time
import random # Importamos el modulo random
import time # Importamos el modulo time
from colorama import Fore # Importamos el modulo colorama

start = time.time() # Iniciamos el contador de tiempo

### F U N C I O N E S ###
def scrape(url): 
    print("starting", url) # Imprimimos por pantalla el inicio de la url
    duration = round(random.random(),3) # Generamos un numero aleatorio entre 0 y 1 con 3 decimales
    sleep(duration) # Hacemos que el programa se duerma durante el tiempo generado
    print("finished", url, "time taken:", duration, "seconds") # Imprimimos por pantalla el final de la url y el tiempo que ha tardado
    return url, duration # Devolvemos la url y el tiempo que ha tardado



### V A R I A B L E S    G L O B A L E S ###
urls = ["a.com", "b.com", "c.com", "d.com"] # creacion de una lista de urls

### M A I N ###

if __name__ == '__main__':
    # Creando un objeto Pool con 4 procesos
    pool = Pool(processes=4)
    # Mapeamos la funcion scrape con la lista de urls
    # Empezamos el proceso de paralelizacion con 4 procesos
    data = pool.map(scrape, urls)
    # Cerramos el proceso
    pool.close()    
    print()
    # Imprimimos por pantalla los resultados
    print(Fore.YELLOW,"RESULTADOS:"+ Fore.WHITE)
    for row in data:
        print(row)
end=time.time() # Paramos el contador de tiempo
print("TIEMPO TOTAL: ",end-start) # Imprimimos por pantalla el tiempo total que ha tardado el programa
print

```

# Codigo en secuencial

```

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

    

```

# CONCLUSIONES
Para demostrarlo hemos guardado 10 veces los tiempos de los dos programas en un csv y hemos comparado el tiempo haciendo una media de los 10 tiempos en paralelo y en secuencial.

```
TIEMPO EN PARALELO,TIEMPO EN SECUENCIAL
"1.364","1.901"
"1.471","2.898"
"1.397","1.276"
"1.648","2.685"
"1.647","1.851"
"1.372","2.221"
"1.147","1.725"
"1.64","3.444"
"1.653","2.02"
"1.309","1.793"
MEDIAS
"1,4648","2,1814"

```



