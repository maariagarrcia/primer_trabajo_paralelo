
import menu
import helpers
from colorama import Fore
from secuencial import *
from parelelo import *
from leer_csv import iniciar
import time


def inicio():
    finalizar= False
    helpers.clear() #Limpia la terminal

    while (not finalizar):
        opcion = menu.menu()
        if opcion==1:
            secuenciall()
            end=time.time() # Paramos el contador de tiempo
            print("TIEMPO TOTAL: ",end-start) # Imprimimos por pantalla el tiempo total que ha tardado el programa

            print()

        elif opcion==2:

            iniciar()            
            print()

        elif opcion==3:
            # ejecutar el programa en paralelo
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
            print()



    print(Fore.GREEN  + "Nos vemos otro dia :)")
    print(Fore.WHITE)
       

inicio()