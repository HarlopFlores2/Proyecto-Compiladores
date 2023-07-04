import ply.yacc as yacc
import lexico

from lexico import tokens
from semantico import *

precedence = (
    ('left', 'suma', 'resta'),
    ('left', 'multiplicacion', 'division', 'modulo'),
    ('left', 'menor', 'mayor', 'menor_igual', 'mayor_igual', 'igual', 'diferente'),
    ('left', 'or'),
    ('left', 'and'),
    ('right', 'parentesis_izq', 'parentesis_der'),
    ('left', 'llave_izq', 'llave_der'),
    ('left', 'coma', 'punto_coma'),
)

def p_programa(p):
    '''programa : int declaraciones_var main parentesis_izq parentesis_der llave_izq bloque llave_der'''
    p[0] = Programa(p[2], p[7])


def p_declaraciones_var(p):
    '''declaraciones_var : identificador coma declaraciones_var
                         | identificador punto_coma'''
    if len(p) == 4:
        p[0] = p[1] + ',' + p[3]
    else:
        p[0] = p[1]

def p_bloque(p):
    '''bloque : sentencia bloque
              | sentencia '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_sentencia(p):
    '''sentencia : expresion_asignacion punto_coma
                 | condicion
                 | ciclo
                 | escritura_cadena
                 | escritura_entero'''
    p[0] = p[1]

def p_escritura_cadena(p):
    '''escritura_cadena : puts parentesis_izq cadena parentesis_der punto_coma'''
    p[0] = EscrituraCadena(p[3])

def p_escritura_entero(p):
    '''escritura_entero : putw parentesis_izq expresion parentesis_der punto_coma'''
    p[0] = EscrituraEntero(p[3])

def p_expresion_asignacion(p):
    '''expresion_asignacion : identificador asignacion expresion'''
    p[0] = Asignacion(p[1], p[3])


def p_condicion(p):
    '''condicion : if parentesis_izq expresion parentesis_der llave_izq bloque llave_der
                 | if parentesis_izq expresion parentesis_der llave_izq bloque llave_der else llave_izq bloque llave_der'''
    if len(p) == 8:
        p[0] = Condicion(p[3], p[6])
    else:
        p[0] = Condicion(p[3], p[6], p[10])

def p_ciclo(p):
    '''ciclo : while parentesis_izq expresion parentesis_der llave_izq bloque llave_der'''
    p[0] = Ciclo(p[3], p[6])


def p_expresion(p):
    '''expresion : expresion suma expresion
                 | expresion resta expresion
                 | expresion multiplicacion expresion
                 | expresion division expresion
                 | expresion modulo expresion
                 | expresion mayor expresion
                 | expresion menor expresion
                 | expresion mayor_igual expresion
                 | expresion menor_igual expresion
                 | expresion igual expresion
                 | expresion diferente expresion
                 | expresion or expresion
                 | expresion and expresion
                 | parentesis_izq expresion parentesis_der
                 | identificador
                 | number'''
    if len(p) == 2:
        if p[1] == 'true':
            p[0] = Valor(True)
        elif p[1] == 'false':
            p[0] = Valor(False)
        else:
            p[0] = Variable(p[1])
    elif p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = Expresion(p[1], p[2], p[3])


def p_error(p):
    if p is None:
        print("Error de sintaxis: se alcanzó el final inesperadamente")
    else:
        print("Error de sintaxis en '%s'" % p.value)
    parser.error = 1


parser = yacc.yacc()

def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        fin = 'prueba.txt'
    f = open(fin, 'r')
    data = f.read()
    print(data)
    parser.parse(data, debug=1)