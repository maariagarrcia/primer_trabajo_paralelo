
import menu
import helpers
from colorama import Fore
from secuencial import *
from parelelo import main
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
    
            print()



    print(Fore.GREEN  + "Nos vemos otro dia :)")
    print(Fore.WHITE)
       

inicio()