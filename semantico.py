class Entorno:
    def __init__(self):
        self.variables = {}
        self.anidado = False

class Programa:
    def __init__(self, declaraciones, bloque):
        self.declaraciones = declaraciones
        self.bloque = bloque

    def evaluar(self, entorno):
        for declaracion in self.declaraciones:
            declaracion.evaluar(entorno)
        for sentencia in self.bloque:
            sentencia.evaluar(entorno)

class DeclaracionVar:
    def __init__(self, identificador):
        self.identificador = identificador

    def evaluar(self, entorno):
        entorno.variables[self.identificador] = None

class Bloque:
    def __init__(self, sentencias):
        self.sentencias = sentencias

    def evaluar(self, entorno):
        for sentencia in self.sentencias:
            sentencia.evaluar(entorno)

class Asignacion:
    def __init__(self, identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

    def evaluar(self, entorno):
        entorno.variables[self.identificador] = self.expresion.evaluar(entorno)

class EscrituraCadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def evaluar(self, entorno):
        print(self.cadena)

class EscrituraEntero:
    def __init__(self, expresion):
        self.expresion = expresion

    def evaluar(self, entorno):
        print(self.expresion.evaluar(entorno))

class Condicion:
    def __init__(self, expresion, bloque_si, bloque_no=None):
        self.expresion = expresion
        self.bloque_si = bloque_si
        self.bloque_no = bloque_no

    def evaluar(self, entorno):
        if entorno.anidado:
            raise Exception('Sentencias de control anidadas no permitidas')
        entorno.anidado = True
        if self.expresion.evaluar(entorno):
            self.bloque_si.evaluar(entorno)
        elif self.bloque_no is not None:
            self.bloque_no.evaluar(entorno)

class Ciclo:
    def __init__(self, expresion, bloque):
        self.expresion = expresion
        self.bloque = bloque

    def evaluar(self, entorno):
        if entorno.anidado:
            raise Exception('Sentencias de control anidadas no permitidas')
        entorno.anidado = True
        while self.expresion.evaluar(entorno):
            self.bloque.evaluar(entorno)

class Valor:
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self, entorno):
        return self.valor

class Variable:
    def __init__(self, identificador):
        self.identificador = identificador

    def evaluar(self, entorno):
        return entorno.variables[self.identificador]


class Expresion:
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha

    def evaluar(self, entorno):
        izquierda = self.izquierda.evaluar(entorno)
        derecha = self.derecha.evaluar(entorno)

        if self.operador == '+':
            return izquierda + derecha
        elif self.operador == '-':
            return izquierda - derecha
        elif self.operador == '*':
            return izquierda * derecha
        elif self.operador == '/':
            return izquierda / derecha
        elif self.operador == '%':
            return izquierda % derecha
        elif self.operador == '<':
            return izquierda < derecha
        elif self.operador == '>':
            return izquierda > derecha
        elif self.operador == '<=':
            return izquierda <= derecha
        elif self.operador == '>=':
            return izquierda >= derecha
        elif self.operador == '==':
            return izquierda == derecha
        elif self.operador == '!=':
            return izquierda != derecha
        elif self.operador == '||':
            return izquierda or derecha
        elif self.operador == '&&':
            return izquierda and derecha


