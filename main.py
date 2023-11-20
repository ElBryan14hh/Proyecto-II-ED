#########################################
#                                       #
#   Universidad Nacional de Costa Rica  #
#   Estructuras de Datos - CII 2023     #
#   Bryan Hernandez - 8 pm              #
#   Santiago Solis - 6 pm               #
#   Felipe Herrrera - 8 pm              #
#   Proyecto #2 - Analizador Semantico  #
#                                       #
#########################################

from analizador import Analizador

if __name__ == "__main__":
   
    analizador = Analizador()
    
    archivo = "codigo.txt"
    analizador.leer_archivo(archivo)