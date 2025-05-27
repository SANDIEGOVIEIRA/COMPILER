# lexer.py
import ply.lex as lex

# Palavras reservadas
reserved = {
    'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR',
    'func': 'FUNC', 'return': 'RETURN',
    'true': 'TRUE', 'false': 'FALSE',
}

# Lista de tokens (inclui palavras reservadas)
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'AND', 'OR', 'NOT',
] + list(reserved.values())

# Definições de regex para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r':='

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMMA   = r','

t_LE      = r'<='
t_GE      = r'>='
t_EQ      = r'=='
t_NE      = r'!='
t_LT      = r'<'
t_GT      = r'>'

t_AND     = r'&&'
t_OR      = r'\|\|'
t_NOT     = r'!'

# Ignorar espaços e tabs
t_ignore = ' \t'

# Quebra de linha – conta linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Números inteiros e reais
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Erro léxico – coleta em lista no próprio lexer
def t_error(t):
    t.lexer.invalid_tokens.append((t.value[0], t.lineno))
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()
# Lista para relatórios de tokens inválidos
lexer.invalid_tokens = []

# Teste rápido
if __name__ == '__main__':
    sample = '@ foo := 42\nfor(i<10){x:=x+1}$'
    lexer.input(sample)
    for tok in lexer:
        print(tok)
    print('Invalid:', lexer.invalid_tokens)
