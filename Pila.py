from VariablesPila import VariablesPila
 
class Pila:
    """
    En esta clase se define la pila que se utiliza para limitar las variables por sus llaves

    Atributos:
    - stack (list): lista utilizada para representar la pila
    - cont (int): contador usado para seguimiento

    """
      
    def __init__(self):
        """
        Se crea el constructor de la clase pila, inicializa la pila
        como una lista vacía y el contador en 0
        """
        self.stack = []
        self.cont = 0
    
    def agregar(self, c):
        """
        Agrega un elemento a la pila.
        Crea objeto VariablesPila (elemento) y lo agrega a la pila (stack).

        Args:
        - c (str): La clave del elemento a agregar.
        """
        elemento = VariablesPila(c, self.cont)
        self.stack.append(elemento)

    def aumentar(self):
        """
        Aumenta el contador en uno.
        """
        self.cont+=1

    def eliminar(self):
        """
        Elimina elementos de la pila
        Recorre la pila y elimina elementos con su ubicación
        y el valor del contador. Retorna las claves de los elementos eliminados.

        Returns:
        - list: Lista de claves de elementos eliminados.
        """
        vec = []
        for var in reversed(self.stack):
            if(var.ubicacion == self.cont and self.cont != 0):
                vec.append(var.clave)
                self.stack.pop()
            else:
                break
        self.cont-=1
        return vec