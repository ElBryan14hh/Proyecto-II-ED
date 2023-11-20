class Tabla_Hash:
        """
        En esta clase se define la tabla hash 
        utilizada a lo largo del proyecto

        Atributos:
        - tabla(dict): diccionario utilizado para simular la tabla hash
        """
        def __init__(self):
                """
                Metodo constructor de Tabla_Hash
                Inicializa la tabla como vacía
                """
                self.tabla = {}

        def agregar(self, tipo, nom):
                """
                El metodo busca agregar objetos a la tabla
                Agrega el elemento a la tabla, sus claves son tipo y nombre

                Args:
                - tipo(str): tipo del objeto a agregar
                - nom(str): nombre del objeto a agregar
                """
                self.tabla[nom] = tipo

        def mostrar_tabla(self):
                """
                La función se encarga de mostrar la tabla y sus elementos
                
                """
                for i in self.tabla:
                        print(f"[{i}] -> {self.tabla[i]}")
