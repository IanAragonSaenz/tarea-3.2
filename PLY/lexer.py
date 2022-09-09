import ply.lex as lex

reserved = {
    'program': 'PROGRAM',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
}

tokens = ['SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'MENOR', 'MAYOR', 'NO_IGUAL', 
            'IGUAL', 'PAR_IZQ', 'PAR_DER', 'BRACKET_IZQ', 'BRACKET_DER', 'COMMA', 
            'DOBLE_PUNTO', 'PUNTO_COMMA', 'VAR_INT', 'VAR_FLOAT', 'VAR_ID', 'VAR_STRING'] + list(reserved.values())

t_PUNTO_COMMA = r'\;'
t_DOBLE_PUNTO = r':'
t_COMMA = r'\,'
t_BRACKET_IZQ = r'\{'
t_BRACKET_DER = r'\}'
t_PAR_IZQ = r'\('
t_PAR_DER = r'\)'
t_MAYOR = r'>'
t_MENOR = r'<'
t_NO_IGUAL = r'<>'
t_IGUAL = r'\='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_VAR_STRING = r'\".*\"'
t_ignore = " \t\n"

def t_VAR_ID(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'VAR_ID')
    return t

def t_VAR_FLOAT(t):
    r'[0-9]+(\.[0-9]+)?'
    t.value = float(t.value)
    return t

def t_VAR_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_comment(t):
    r'\//.*'
    pass


def t_error(t):
    print("Lexical error ' {0} ' found in line ' {1} ' ".format(t.value[0], t.lineno))
    t.lexer.skip(1)


lex.lex()