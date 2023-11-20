class Error:
    """
    La clase Error es la encargada de manejar los errores dentro del programa
    
    Atributos:
    - cant(int): cantidad de errores.
    """


    def __init__(self):
        """
        Constructor de la clase error, cantidad de errores empieza en 0
        """
        self.cant = 0
    
    def error_no_declarado(self, linea, nom):
        """
        Mensaje cuando no se declara una variable

        Args:
        - linea(int): numero de linea donde está el error
        - nom(str): nombre de la variable
        """
        print(f"Error - Linea {linea}: '{nom}' no esta declarado")
        self.cant += 1

    def error_ya_declarado(self, linea, nom):
        """
        Se muesta un mensaje cuando una variable se declaró anteriormente

        Args:
        - linea(int): numero de linea donde está el error
        - nom(str): nombre de la variable
        """
        print(f"Error - Linea {linea}: '{nom}' ya fue declarada anteriormente")
        self.cant += 1

    def error_retorno(self, linea, nom):
        """
        Despliega error cuando no coincide el retorno

        Args:
        - linea(int): numero de linea donde está el error
        - nom(str): nombre de la variable
        """
        print(f"Error - Linea {linea}: valor de retorno no coincide con la declaracion '{nom}'")
        self.cant += 1

    def error_asignacion(self, linea, nom):
        """
        Despliega un error cuando el tipo de variable es incorrecto

        Args:
        - linea(int): numero de linea donde está el error
        - nom(str): nombre de la variable
        """
        print(f"Error - Linea {linea}: tipo de variable de '{nom}' no coincide con el valor de asignacion")
        self.cant += 1

    def error_comparacion(self, linea, nom):
        """
        Despliega un error cuando no coincide el valor de una variable.

        Args:
        - linea(int): numero de linea donde está el error
        - nom(str): nombre de la variable
        """
        print(f"Error - Linea {linea}: el valor de '{nom}' no coincide con el valor de comparacion")
        self.cant += 1

    def error_operacion(self, linea, nom):
        """
        Se despliega un error cuando el valor no coincide con algún dato de la operación

        Args:
        - linea(int): numero de linea donde está el error
        - nom(str): nombre de la variable
        """
        print(f"Error - Linea {linea}: el valor de '{nom}' no coincide con el valor de algun dato en la operacion")
        self.cant += 1
    
    def error_retorno_void(self, linea, nom):
        """
        Se muestra cuando una función void devuelve algun valor

        Args:
        - linea(int): numero de linea donde está el error
        - nom(str): nombre de la variable
        """
        print(f"Error - Linea {linea}: '{nom}' no puede retornar ningun valor")
        self.cant += 1

    def error_argumentos(self, linea, nom):
        """
        Se muestra cuando la cantidad de argumentos no coincide

        Args:
        - linea(int): numero de linea donde está el error
        - nom: nombre de la variable
        """
        print(f"Error - Linea {linea}: cantidad de argumentos no coincide con '{nom}'")
        self.cant += 1

    def error_parametro(self, linea, nom):
        """
        Se muestra cuando el valor de alguno de los parametros no coincide con la funcion

        Args:
        - linea(int): numero de linea donde está el error
        - nom: nombre de la variable
        """
        print(f"Error - Linea {linea}: el valor de algun parametro no coincide con '{nom}'")
        self.cant += 1
