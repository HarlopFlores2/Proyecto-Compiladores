class programa:
    def __init__(self, declaraciones, bloque):
        self.declaraciones = declaraciones
        self.bloque = bloque

    def __str__(self):
        return self.declaraciones + self.bloque
    
class declaraciones_var:
    def __init__(self, identificador, declaraciones_var):
        self.identificador = identificador
        self.declaraciones_var = declaraciones_var

    def __str__(self):
        return self.identificador + ',' + self.declaraciones_var
    
class bloque:
    def __init__(self, sentencia, bloque):
        self.sentencia = sentencia
        self.bloque = bloque

    def __str__(self):
        return self.sentencia + self.bloque
    
class sentencia:
    def __init__(self, expresion_asignacion):
        self.expresion_asignacion = expresion_asignacion

    def __str__(self):
        return self.expresion_asignacion
    

class escritura_cadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def __str__(self):
        return 'puts(' + self.cadena + ')'
    
class escritura_entero:
    def __init__(self, expresion):
        self.expresion = expresion

    def __str__(self):
        return 'putw(' + self.expresion + ')'
    
class escritura: # only puts and putw
    def __init__(self, escritura_cadena, escritura_entero):
        self.escritura_cadena = escritura_cadena
        self.escritura_entero = escritura_entero
    
    def __str__(self):
        if self.escritura_cadena == None:
            return self.escritura_entero
        else:
            return self.escritura_cadena
    
class expresion_asignacion:
    def __init__(self, identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

    def __str__(self):
        return self.identificador + '=' + str(self.expresion)
    
class condicion:
    def __init__(self, expresion, bloque, bloque_else):
        self.expresion = expresion
        self.bloque = bloque
        self.bloque_else = bloque_else
    
    def __str__(self):
        if self.bloque_else == None:
            return 'if (' + self.expresion + ') {\n' + self.bloque + '}\n'
        else:
            return 'if (' + self.expresion + ') {\n' + self.bloque + '} else {\n' + self.bloque_else + '}\n'
        
class ciclo:
    def __init__(self, expresion, bloque):
        self.expresion = expresion
        self.bloque = bloque

    def __str__(self):
        return 'while (' + self.expresion + ') {\n' + self.bloque + '}\n'
    
class expresion:
    def __init__(self, expresion):
        self.expresion = expresion

    def __str__(self):
        return self.expresion
    
class valor_expresion:
    def __init__(self, identificador, number):
        self.identificador = identificador
        self.number = number

    def __str__(self):
        if self.identificador == None:
            return self.number
        else:
            return self.identificador

    

