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
```


