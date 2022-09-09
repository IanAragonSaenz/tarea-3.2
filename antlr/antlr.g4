grammar antlr;
// Ian Aragon A01177009

// Gramatica:

programa: PROGRAM VAR_ID PUNTO_COMMA vars_pos bloque;

vars_pos: vars 
    | ;
vars: VAR vars_start;
vars_start: vars_id DOBLE_PUNTO tipo PUNTO_COMMA vars_add;
vars_id: VAR_ID vars_more;
vars_more: COMMA vars_id 
    | ;
vars_add: vars_start 
    | ;

tipo: INT 
    | FLOAT;

bloque: BRACKET_IZQ bloque_dentro BRACKET_DER;
bloque_dentro: estatuto bloque_dentro 
    | ;

estatuto: asignacion 
    | condicion 
    | escritura;

asignacion: VAR_ID IGUAL expresion PUNTO_COMMA;

expresion: exp expresion_relop;
expresion_relop: MAYOR exp 
    | MENOR exp 
    | NO_IGUAL exp 
    | ;

escritura: PRINT PAR_IZQ escritura_exp PAR_DER PUNTO_COMMA;
escritura_exp: expresion escritura_pos 
    | VAR_STRING escritura_pos;
escritura_pos: COMMA escritura_pos 
    | ;

condicion: IF PAR_IZQ expresion PAR_DER bloque condicion_pos PUNTO_COMMA;
condicion_pos: ELSE bloque 
    | ;

exp: termino exp_pos;
exp_pos: SUMA exp 
    | RESTA exp 
    | ;

termino: factor termino_pos;
termino_pos: MULTIPLICACION termino 
    | DIVISION termino 
    | ;

factor: PAR_IZQ expresion PAR_DER 
    | factor_pos var_cte;
factor_pos: SUMA 
    | RESTA 
    | ;

var_cte: VAR_ID 
    | VAR_INT 
    | VAR_FLOAT;





// Lexer:

SUMA: '+';
RESTA: '-';
MULTIPLICACION: '*';
DIVISION: '/';
MENOR: '<';
MAYOR: '>';
NO_IGUAL: '<>';
IGUAL: '=';
PAR_IZQ: '(';
PAR_DER: ')';
BRACKET_IZQ: '{';
BRACKET_DER: '}';
COMMA : ',';
DOBLE_PUNTO: ':';
PUNTO_COMMA:  ';';
INT: 'int';
FLOAT: 'float';
IF: 'if';
ELSE: 'else';
VAR: 'var';
PRINT: 'print';
PROGRAM : 'program';
VAR_INT: DIGITS;
VAR_FLOAT: DIGITS(.DIGITS)?;
VAR_ID: [_a-zA-Z][_a-zA-Z0-9]*;
VAR_STRING: '"'~('\r'|'"')*'"';
DIGITS: DIGIT+;
DIGIT: [0-9];
WHITESPACE: [ \t\r\n]+ -> skip;
