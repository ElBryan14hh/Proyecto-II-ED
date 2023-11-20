from Tabla_Hash import Tabla_Hash
from Error import Error
from Pila import Pila

class Analizador:
    """
    La clase Analizador es la encargada de la lectura
    de los archivos, así como identificar variables, funciones, condicionales 
    y ciclos "while"

    Atributos:
    tablita(Tabla_Hash): tabla usada para almacenar variables con su nombre y tipo
    error(Error): objeto encargado de mostrar errores en caso de encontrar
    pila(Pila): stack usado para llaves
    funcion(str): guarda el nombre de la función que se analiza
    tabla_funciones(Tabla_Hash): es la tabla hash encargada de almacenar funciones
    """
    def __init__(self):
        """
        Este es el metodo constructor del Analizador
        Crea nuevos atributos y los inicializa como vacíos
        """
        self.tablita = Tabla_Hash()
        self.error = Error()
        self.pila = Pila()
        self.funcion = ""
        self.tabla_funciones = Tabla_Hash()

    def tipo_dato(self, tipo, val):
        """
        El metodo tipo_dato se encarga de comparar y 
        verificar si corresponde al tipo de dato necesario.

        Args:
        - tipo(str): tipo de dato que se debe verificar
        - val(str): funciona como una llave dentro de la tabla hash

        Returns: 
        - bool: True si el tipo de dato corresponde, Falso en caso contrario
        """
        try:
            if(val in self.tablita.tabla):
                tipo2 = self.tablita.tabla[val]
                if(tipo2 != tipo):
                    raise
            elif(tipo == "string"):
                if(val.count('"') != 2):
                    raise
            elif(tipo == "int"):
                p = int(val)
            else:
                p = float(val)
        except:
            return False
        return True

    def variables(self, linea, numLinea):
        """
        El metodo se encarga de manejar como se declaran las variables.
        Se encarga de comprobar que las variables estén correctas y las 
        agrega a la tabla hash.

        Args:
        - linea(str): corresponde a la línea de código que se lee
        - numLinea(int): numero de línea actual en el archivo
        """
        palabra = linea.split()
        salir = False
        try:
            if(palabra[1] in self.tablita.tabla):
                self.error.error_ya_declarado(numLinea, palabra[1])
                return
            pal = palabra[3]
            pal2 = palabra[3:]
            p = "".join(pal2)
            p = self.remplazar_en_linea(p).split()
            if(p[0] in self.tabla_funciones.tabla):
                params = self.tabla_funciones.tabla[p[0]]
                vals = p[1:]
                if(len(params) != len(vals)):
                    self.error.error_argumentos(numLinea, p[0])
                else:
                    for i in range (0, len(params)):
                        if(self.tipo_dato(params[i], vals[i]) == False):
                            self.error.error_parametro(numLinea, p[0])
                            break
                if(palabra[0] != self.tablita.tabla[p[0]]):
                    raise
            else:
                if(palabra[0] == "int"):
                    i = int(pal)
                elif(palabra[0] == "float"):
                    i = float(pal)
                elif(palabra[0] == "string"):
                    try:
                        i = float(pal)
                        salir = True
                    except:
                        salir = False
                else:
                    raise
                if(salir):
                    raise
            self.tablita.agregar(palabra[0], palabra[1])
            self.pila.agregar(palabra[1])
        except:
            self.error.error_asignacion(numLinea, palabra[1])

    def remplazar_en_linea(self, linea):
        """
        Remueve caracateres de las lineas de código

        Args:
        - linea(str): linea de codigo actual, debe procesarse

        Returns:
        - lin(str): linea de codigo sin los caracteres reemplazados
        """
        lin = linea.replace('(',' ')
        lin = lin.replace(')',' ')
        lin = lin.replace('{',' ')
        lin = lin.replace('}',' ')
        lin = lin.replace(',',' ')
        lin = lin.replace('+', ' ')
        lin = lin.replace('<', ' ')
        lin = lin.replace('>', ' ')
        lin = lin.replace('=', ' ')
        lin = lin.replace('!', ' ')
        lin = lin.replace('-', ' ')
        lin = lin.replace('*', ' ')
        lin = lin.replace('/', ' ')
        lin = lin.replace('%', ' ')
        return lin
    
    def funciones(self, linea, numLinea):
        """
        Se encarga de definir las funciones en el código

        Args:
        - linea(str): linea de archivo, tiene la definicion de la funcion
        - numLinea(int): numero de linea actual en el archivo
        """
        palabra = linea.split()
        vec = []
        pal = ""
        for i in range (0, len(palabra) - 1, 2):
            if(palabra[i + 1] not in self.tablita.tabla):
                if(i == 0):
                    pal = palabra[i + 1]
                    self.funcion = palabra[1]
                else:
                    vec.append(palabra[i])
                if(i == 2):
                    self.pila.aumentar()
                self.tablita.agregar(palabra[i], palabra[i + 1])
                self.pila.agregar(palabra[i + 1])
            else:
                self.error.error_ya_declarado(numLinea, palabra[i + 1])
        if(pal != ""):
            self.tabla_funciones.agregar(vec, pal)
            
    '''
    Nombre de la funcion: funcion_reservadas
    
    Parametros que recibe: Una linea y el numero de la misma
    
    Parametros que retorna: 
    
    Proceso que realiza la funcion: 
    Esta función se encarga de analizar y procesar líneas 
    de código que contienen las palabras clave "if" o "while". 
    Incrementa un contador en una pila, verifica si la palabra clave 
    está en una tabla de símbolos, y luego intenta convertir el valor 
    siguiente de acuerdo con el tipo especificado en la tabla de símbolos. 
    Si hay algún error en la conversión o si la palabra clave no está en 
    la tabla de símbolos, llama a métodos de manejo de errores específicos.
    '''
    def funcion_reservadas(self, linea, numLinea):
        palabra = linea.split()
        if(palabra[0] == "if" or "while"):
            self.pila.aumentar()
            pal = palabra[1]
            if(pal in self.tablita.tabla):
                tipo = self.tablita.tabla[pal]
                try:
                    if(tipo == "int"):
                        i = int(palabra[2])
                    elif(tipo == "float"):
                        i = float(palabra[2])
                    elif(tipo == "string"):
                        try:
                            if('.' in pal):
                                i = float(palabra[2])
                            else:
                                i = int(palabra[2]) 
                            raise
                        except:
                            return
                    else:
                        raise
                except:
                    self.error.error_comparacion(numLinea, pal)
            else:
                self.error.error_no_declarado(numLinea, palabra[1])
                
    '''
    Nombre de la funcion: operaciones
    
    Parametros que recibe: Una linea y el numero de la misma
    
    Parametros que retorna: 
    
    Proceso que realiza la funcion: 
    Esta función se encarga de realizar operaciones numéricas en variables 
    previamente declaradas, verificando la compatibilidad de tipos y 
    manejando errores si es necesario.
    '''
    
    def operaciones(self, linea, numLinea):
        palabra = linea.split()
        pal = palabra[0]
        if(pal in self.tablita.tabla):
            tipo = self.tablita.tabla[pal][0]
            if(tipo == "int" or "float"):
                try:
                    for i in range (1, len(palabra)):
                        if(palabra[i] in self.tablita.tabla):
                            tipo2 = self.tablita.tabla[palabra[i]][0]
                            if(tipo2 != "int" and tipo2 != "float"):
                                raise
                        elif(tipo == "int"):
                            p = int(palabra[i])
                        else:
                            p = float(palabra[i])
                except:
                    self.error.error_operacion(numLinea, pal)
        else:
            self.error.error_no_declarado(numLinea, pal)
            
    '''
    Nombre de la funcion: asignaciones
    
    Parametros que recibe: Una linea y el numero de la misma
    
    Parametros que retorna: 
    
    Proceso que realiza la funcion: 
    Esta función se encarga de procesar líneas de código que 
    realizan asignaciones a variables, verificando la existencia de las 
    variables, los tipos de datos y manejando errores durante la asignación.
    
    '''
    def asignaciones(self, linea, numLinea):
        palabra = linea.split()
        pal = palabra[0]
        if(pal in self.tablita.tabla):
            tipo = self.tablita.tabla[pal]
            if(tipo == "int" or "float" or "string"):
                try:
                    if(palabra[1] in self.tablita.tabla):
                        tipo2 = self.tablita.tabla[palabra[1]]
                        if(tipo2 != "int" and tipo2 != "float" and tipo2 != "string"):
                            raise
                    elif(tipo == "string"):
                        if(palabra[1].count('"') != 2):
                            raise
                    elif(tipo == "int"):
                        p = int(palabra[1])
                    else:
                        p = float(palabra[1])
                except:
                    self.error.error_asignacion(numLinea, pal)
        else:
            self.error.error_no_declarado(numLinea, pal)
    
    '''
    Nombre de la funcion: valor_retorno
    
    Parametros que recibe: Una linea y el numero de la misma
    
    Parametros que retorna: 
    
    Proceso que realiza la funcion: 
    Esta funcion verifica el tipo de retorno de la funcion designada.
    Si la funcion designada fuese de tipo "void", nuestra funcion se encargara de verificar
    que no haya un valor de retorno. Si la función no es "void", verifica si el valor de 
    retorno especificado es válido en términos de tipo y contenido, y maneja los errores 
    correspondientes llamando a métodos específicos.
    
    '''

    def valor_retorno(self, linea, numLinea):
        palabra = linea.split()
        tipo = self.tablita.tabla[self.funcion]
        if(tipo == "void"):
            if(len(palabra) == 1):
                return
            else:
                self.error.error_retorno_void(numLinea, self.funcion)
        else:
            val = palabra[1]
            try:
                if(val in self.tablita.tabla):
                    
                    if(self.tablita.tabla[val] == tipo):
                        return
                    else:
                        raise
                else:
                    try:
                        f = float(val)
                    except:
                        if(val.count('"') != 2):
                            self.error.error_no_declarado(numLinea, self.funcion)
                        else:
                            raise
                    if(tipo == "int"):
                        i = int(val)
            except:
                self.error.error_retorno(numLinea, self.funcion)
    
    '''
    Nombre de la funcion: fin_funcion
    
    Parametros que recibe: Nada
    
    Parametros que retorna: 
    
    Proceso que realiza la funcion: 
    Esta función se encarga de limpiar o eliminar las variables locales
    al finalizar una función, asegurándose de que las variables locales ya no estén 
    presentes en la tabla de símbolos después de que la función haya concluido su ejecución.
    
    '''
    
    def fin_funcion(self):
        vec = self.pila.eliminar()
        for i in vec:
            del self.tablita.tabla[i]
            
    '''
    Nombre de la funcion: leer_Archivo
    
    Parametros que recibe: El archivo a leer 
    
    Parametros que retorna: 
    
    Proceso que realiza la funcion: 
    Esta funcion se encarga de abrir el archivo a leer, iterar sobre cada linea del archivo 
    y luego de esto, comienza a entrar en las otras funciones de esta clase dependiendo del 
    contenido de cada linea. 
    Seguidamente, el metodo se encarga de imprimir la cantidad de erroes existentes y en el 
    caso de no haber errores, este imprimira un mensaje notificando lo anterior. Por ultimo, 
    se encarga de mostrar la tabla de simbolos. 
    
    ''' 
    
    def leer_archivo(self, archivo):
        n = 1
        with open(archivo, "r") as f:
            for linea in f:
                lin = self.remplazar_en_linea(linea)
                lin2 = lin.split()
                lin3 = linea.split()
                if('=' in linea and lin2[0] != "if" and lin2[0] != "while"):
                    if(lin2[0] != "int" and lin2[0] != "string" and lin2[0] != "float"):
                        if('+' in linea or '/' in linea or '-' in linea or '*' in linea or '%' in linea):
                            self.operaciones(lin, n)
                        else:
                            self.asignaciones(lin, n)
                    else:
                        self.variables(linea, n)
                elif('(' in linea and ')' in linea):
                    if(lin2[0] == "if" or lin2[0] == "while"):
                        self.funcion_reservadas(lin, n)
                    else:
                        self.funciones(lin, n)
                elif('=' in linea):
                    self.asignaciones(lin, n)
                elif(lin3 != []):
                    if(lin3[0] == "return"):
                        self.valor_retorno(linea, n)
                    elif(lin3[0] == "}"):
                        self.fin_funcion()
                n+=1
        print(f"\nErrores -> [{self.error.cant}]")
        if(self.error.cant == 0):
            print("El codigo se ha compilado correctamente!")
        self.tablita.mostrar_tabla()

