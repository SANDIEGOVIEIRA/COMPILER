# parser.py
import ply.yacc as yacc
from lexer import tokens, lexer
from ast_nodes import (
    Number, BoolLiteral, Variable,
    BinOp, UnaryOp, Assign,
    If, While, For, Function, Return, Block
)

start = 'program'
precedence = (
    ('right', 'NOT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    '''program : program statement
               | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# Função
def p_statement_func(p):
    'statement : FUNC ID LPAREN param_list RPAREN statement'
    p[0] = Function(p[2], p[4], p[6])

def p_param_list(p):
    '''param_list : param_list COMMA ID
                  | ID
                  | empty'''
    if len(p) == 2 and p[1] is None:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_empty(p):
    'empty :'
    p[0] = None

# Return
def p_statement_return(p):
    'statement : RETURN expression SEMI'
    p[0] = Return(p[2])

# Atribuição
def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMI
                 | ID ASSIGN expression'''
    p[0] = Assign(p[1], p[3])

# If / Else
def p_statement_if(p):
    'statement : IF LPAREN expression RPAREN statement'
    p[0] = If(p[3], p[5], None)

def p_statement_if_else(p):
    'statement : IF LPAREN expression RPAREN statement ELSE statement'
    p[0] = If(p[3], p[5], p[7])

# While
def p_statement_while(p):
    'statement : WHILE LPAREN expression RPAREN statement'
    p[0] = While(p[3], p[5])

# For
def p_statement_for(p):
    'statement : FOR LPAREN ID ASSIGN expression SEMI expression SEMI ID ASSIGN expression RPAREN statement'
    init = Assign(p[3], p[5])
    cond = p[7]
    post = Assign(p[9], p[11])
    p[0] = For(init, cond, post, p[13])

# Bloco
def p_statement_block(p):
    'statement : LBRACE program RBRACE'
    p[0] = Block(p[2])

# Expressões binárias
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = BinOp(p[2], p[1], p[3])

# Operador unário NOT
def p_expression_not(p):
    'expression : NOT expression'
    p[0] = UnaryOp(p[1], p[2])

# Agrupamento
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Número
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = Number(p[1])

# Booleano
def p_expression_bool(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = BoolLiteral(p[1].upper() == 'TRUE')

# Variável
def p_expression_id(p):
    'expression : ID'
    p[0] = Variable(p[1])

def p_error(p):
    if p:
        print(f"Syntax error at {p.type} ('{p.value}') line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
