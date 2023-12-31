import ply.lex as lex

reservadas = {
    'main': 'main',
    'if': 'if',
    'else': 'else',
    'while': 'while',
    'putw': 'putw',
    'puts': 'puts',
    'int': 'int'
}

tokens = [
    'punto_coma',
    'coma',
    'parentesis_izq',
    'parentesis_der',
    'llave_izq',
    'llave_der',
    'suma',
    'resta',
    'multiplicacion',
    'division',
    'modulo',
    'menor',
    'mayor',
    'menor_igual',
    'mayor_igual',
    'igual',
    'diferente',
    'or',
    'and',
    'asignacion',
    'identificador',
    'number',
    'cadena'
] + list(reservadas.values())

# Tokens
t_punto_coma = r';'
t_coma = r','
t_parentesis_izq = r'\('
t_parentesis_der = r'\)'
t_llave_izq = r'\{'
t_llave_der = r'\}'
t_suma = r'\+'
t_resta = r'-'
t_multiplicacion = r'\*'
t_division = r'/'
t_modulo = r'%'
t_menor = r'<'
t_mayor = r'>'
t_menor_igual = r'<='
t_mayor_igual = r'>='
t_igual = r'=='
t_diferente = r'!='
t_or = r'\|\|'
t_and = r'&&'
t_asignacion = r'='

# Ignored characters (spaces and tabs and newlines)
t_ignore = ' \t\n'

# comentarios de multiples lineas /* */
def t_comentario_multilinea(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_number(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_cadena(t):
    r'\'[^\']*\''
    t.value = str(t.value)
    return t

def t_identificador(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in reservadas:
        t.type = reservadas[t.value]
    else:
        t.type = 'identificador'
    return t

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    print("Linea: %d" % t.lexer.lineno)
    print("Ubicación: %d" % t.lexer.lexpos)  # proporciona la ubicación exacta del error
    t.lexer.skip(1)

lexer = lex.lex()