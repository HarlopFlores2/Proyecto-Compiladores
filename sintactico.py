import ply.yacc as yacc
from lexico import tokens
import lexico as lex
from semantico import *

procedence = ( 
    ('left', 'caracteres'),
    ('left', 'identificador'),
    ('right', 'asignacion'),
    ('left', 'or'),
    ('left', 'and'),
    ('left', 'igual', 'diferente'),
    ('left', 'mayor', 'menor', 'mayor_igual', 'menor_igual'),
    ('left', 'suma', 'resta'),
    ('left', 'multiplicacion', 'division', 'modulo'),
    ('left', 'parentesis_izq', 'parentesis_der'),
    ('left', 'llave_izq', 'llave_der'),
    ('left', 'coma', 'punto_coma'),
    ('left', 'int', 'main', 'if', 'else', 'while', 'putw', 'puts')
)

def p_programa(p):
    '''programa : int declaraciones_var main parentesis_izq parentesis_der llave_izq bloque llave_der'''
    p[0] = programa(p[2], p[7])


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
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_sentencia(p):
    '''sentencia : expresion_asignacion punto_coma
                 | condicion
                 | ciclo
                 | escritura
                 | comentario_multilinea'''
    p[0] = p[1]

def p_escritura_cadena(p):
    '''escritura_cadena : puts parentesis_izq cadena parentesis_der punto_coma'''
    p[0] = 'puts(' + p[3] + ')'

def p_escritura_entero(p):
    '''escritura_entero : putw parentesis_izq expresion parentesis_der punto_coma'''
    p[0] = 'putw(' + p[3] + ')'

def p_escritura(p):
    '''escritura : escritura_cadena 
                 | escritura_entero '''
    p[0] = p[1]
    

def p_expresion_asignacion(p):
    '''expresion_asignacion : identificador asignacion expresion'''
    p[0] = p[1] + '=' + str(p[3])


def p_condicion(p):
    '''condicion : if parentesis_izq expresion parentesis_der llave_izq bloque llave_der
                 | if parentesis_izq expresion parentesis_der llave_izq bloque llave_der else llave_izq bloque llave_der'''
    if len(p) == 8:
        p[0] = 'if (' + p[3] + ') {\n' + p[6] + '}\n'
    else:
        p[0] = 'if (' + p[3] + ') {\n' + p[6] + '} else {\n' + p[10] + '}\n'

def p_ciclo(p):
    '''ciclo : while parentesis_izq expresion parentesis_der llave_izq bloque llave_der'''
    p[0] = 'while (' + p[3] + ') {\n' + p[6] + '}\n'


def p_expresion(p):
    '''expresion : expresion suma valor_expresion
                 | expresion resta valor_expresion
                 | expresion multiplicacion valor_expresion
                 | expresion division valor_expresion
                 | expresion modulo valor_expresion
                 | expresion mayor valor_expresion
                 | expresion menor valor_expresion
                 | expresion mayor_igual valor_expresion
                 | expresion menor_igual valor_expresion
                 | expresion igual valor_expresion
                 | expresion diferente valor_expresion
                 | expresion or valor_expresion
                 | expresion and valor_expresion
                 | parentesis_izq expresion parentesis_der
                 | valor_expresion'''

    if len(p) == 4:
        p[0] = p[1] + str(p[2]) + str(p[3]) 
    else:
        p[0] = p[1]



def p_valor_expresion(p):
    '''valor_expresion : identificador
                        | number'''
    p[0] = p[1] 



def p_error(p):
    print("Error de sintaxis en '%s'" % p.type)
    print("Error de sintaxis en '%s'" % p.value)

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


    

