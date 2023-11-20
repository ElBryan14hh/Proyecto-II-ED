class VariablesPila:
    """
    Esta clase representa las variables utilizadas en la pila.

    Atributos:
    - clave (str): La clave de la variable.
    - ubicacion (str): La ubicación de la variable en la pila
    """
    def __init__(self, c, u):
        """
        Es el método constructor de la clase VariablesPila

        Args:
        c(str): clave
        u(str): ubicación de la variable

        """        
        self.clave = c
        self.ubicacion = u