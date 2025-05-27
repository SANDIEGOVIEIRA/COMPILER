# main.py
import sys
from lexer import lexer
from parser import parser
from semantic import analyze, SymbolTable, SemanticError

def compile_source(source):
    # 1. Léxico: coletar tokens inválidos
    lexer.input(source)
    for _ in lexer:
        pass
    if lexer.invalid_tokens:
        print("=== Relatório de tokens inválidos ===")
        for val, ln in lexer.invalid_tokens:
            print(f"Caractere inválido '{val}' na linha {ln}")
        print()

    # 2. Parsing → AST
    ast_list = parser.parse(source, lexer=lexer)
    print("AST gerada:", ast_list)

    # 3. Semântica
    symtab = SymbolTable()
    for node in ast_list:
        try:
            analyze(node, symtab)
        except SemanticError as e:
            print("Erro semântico em", node, ":", e)
    print("Tabela de símbolos final:", symtab._symbols)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.src>")
        sys.exit(1)
    source = open(sys.argv[1], 'r').read()
    compile_source(source)
