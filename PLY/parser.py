# Grammar declaration

def p_program(p):
    '''programa : PROGRAM VAR_ID PUNTO_COMMA vars_pos bloque'''
    p[0] = "Aceptado"


def p_vars_pos(p):
    '''vars_pos : vars 
                | empty'''


def p_vars(p):
    '''vars : VAR vars_start'''

def p_vars_start(p):
    '''vars_start : vars_id DOBLE_PUNTO tipo PUNTO_COMMA vars_add'''

def p_vars_id(p):
    '''vars_id : VAR_ID vars_more'''


def p_vars_more(p):
    '''vars_more : COMMA vars_id 
                | empty'''


def p_vars_add(p):
    '''vars_add : vars_start 
                | empty'''


def p_tipo(p):
    '''tipo : INT 
            | FLOAT'''


def p_bloque(p):
    '''bloque : BRACKET_IZQ bloque_dentro BRACKET_DER'''


def p_bloque_dentro(p):
    '''bloque_dentro : estatuto bloque_dentro 
                    | empty'''


def p_estatuto(p):
    '''estatuto : asignacion 
                | condicion 
                | escritura'''


def p_asignacion(p):
    '''asignacion : VAR_ID IGUAL expresion PUNTO_COMMA'''


def p_expresion(p):
    '''expresion : exp expresion_relop'''


def p_expresion_relop(p):
    '''expresion_relop : MAYOR exp 
                        | MENOR exp 
                        | NO_IGUAL exp 
                        | empty'''


def p_escritura(p):
    '''escritura : PRINT PAR_IZQ escritura_exp PAR_DER PUNTO_COMMA'''


def p_escritura_exp(p):
    '''escritura_exp : expresion escritura_pos 
                    | VAR_STRING escritura_pos'''


def p_escritura_pos(p):
    '''escritura_pos : COMMA escritura_pos 
                    | empty'''


def p_condicion(p):
    '''condicion : IF PAR_IZQ expresion PAR_DER bloque condicion_pos PUNTO_COMMA'''


def p_condicion_pos(p):
    '''condicion_pos : ELSE bloque 
                    | empty'''


def p_exp(p):
    '''exp : termino exp_pos'''

def p_exp_pos(p):
    '''exp_pos : SUMA exp 
                | RESTA exp 
                | empty'''


def p_termino(p):
    '''termino : factor termino_pos'''


def p_termino_pos(p):
    '''termino_pos : MULTIPLICACION termino 
                    | DIVISION termino 
                    | empty'''


def p_factor(p):
    '''factor : PAR_IZQ expresion PAR_DER 
                | factor_pos var_cte'''


def p_factor_pos(p):
    '''factor_pos : SUMA 
                | RESTA 
                | empty'''


def p_var_cte(p):
    '''var_cte : VAR_ID 
                | VAR_INT 
                | VAR_FLOAT'''

def p_error(p):
    print("Syntax error in input! - {} ".format(p))


def p_empty(p):
    '''empty :'''
    pass


import sys
import ply.yacc as yacc

from lexer import tokens

yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        f = open(file, 'r')
        data = f.read()
        f.close()
        if yacc.parse(data) == "Aceptado":
            print("Aceptado")
