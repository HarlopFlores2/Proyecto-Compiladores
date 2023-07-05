import lexico
import sintactico
import ply.lex as lex
import ply.yacc as yacc
import sys

if len(sys.argv) != 2:
    print("Uso: python test.py <archivo_de_codigo_fuente>")
    sys.exit(1)

path = sys.argv[1]

with open(path, 'r') as file:
    codigo_fuente = file.read()

# Crear lexer y parser
lexer = lex.lex(module=lexico)
parser = yacc.yacc(module=sintactico)

# Analizar el código fuente
try:
    result = parser.parse(codigo_fuente, lexer=lexer)
    if result is not None:
        print("Compilación exitosa!")
        print("Generacion de Codigo Intermedio: ")
    for i, line in enumerate(sintactico.c3d, start=1):
        print(f"L{i}: {line}")
except Exception as e:
    print("Error durante la compilación:", str(e))
    sys.exit(1)
