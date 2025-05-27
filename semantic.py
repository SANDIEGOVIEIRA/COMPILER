# semantic.py
from ast_nodes import (
    Assign, Variable, Number, BoolLiteral,
    BinOp, UnaryOp, If, While, For, Function, Return, Block
)

class SemanticError(Exception):
    pass

class SymbolTable:
    def __init__(self, parent=None):
        self._symbols = {}     # nome -> tipo ou 'func'
        self.parent = parent

    def declare(self, name, t=None):
        if name not in self._symbols:
            self._symbols[name] = t

    def assign(self, name, t):
        if name not in self._symbols:
            raise SemanticError(f"Variável não declarada: '{name}'")
        self._symbols[name] = t

    def lookup(self, name):
        if name in self._symbols:
            return self._symbols[name]
        if self.parent:
            return self.parent.lookup(name)
        raise SemanticError(f"Variável não declarada: '{name}'")

def analyze(node, symtab=None):
    if symtab is None:
        symtab = SymbolTable()

    # Função
    if isinstance(node, Function):
        symtab.declare(node.name, 'func')
        local = SymbolTable(parent=symtab)
        for p in node.params:
            local.declare(p, 'int')
        analyze(node.body, local)
        return symtab

    # Return
    if isinstance(node, Return):
        analyze(node.expr, symtab)
        return symtab

    # Assign
    if isinstance(node, Assign):
        symtab.declare(node.name)
        t = analyze(node.expr, symtab)
        symtab.assign(node.name, t)
        return symtab

    # If
    if isinstance(node, If):
        t = analyze(node.cond, symtab)
        if t != 'bool':
            raise SemanticError(f"Condição do IF deve ser bool, não '{t}'")
        analyze(node.then_branch, symtab)
        if node.else_branch:
            analyze(node.else_branch, symtab)
        return symtab

    # While
    if isinstance(node, While):
        t = analyze(node.cond, symtab)
        if t != 'bool':
            raise SemanticError(f"Condição do WHILE deve ser bool, não '{t}'")
        analyze(node.body, symtab)
        return symtab

    # For
    if isinstance(node, For):
        analyze(node.init, symtab)
        t = analyze(node.cond, symtab)
        if t != 'bool':
            raise SemanticError(f"Condição do FOR deve ser bool, não '{t}'")
        analyze(node.body, symtab)
        analyze(node.post, symtab)
        return symtab

    # Block
    if isinstance(node, Block):
        for st in node.stmts:
            analyze(st, symtab)
        return symtab

    # Expressões
    if isinstance(node, Number):
        return 'int'
    if isinstance(node, BoolLiteral):
        return 'bool'
    if isinstance(node, Variable):
        return symtab.lookup(node.name)
    if isinstance(node, UnaryOp):
        t1 = analyze(node.operand, symtab)
        if node.op == '!' and t1 != 'bool':
            raise SemanticError(f"Operador '!' requer bool, recebeu '{t1}'")
        return 'bool'
    if isinstance(node, BinOp):
        lt = analyze(node.left, symtab)
        rt = analyze(node.right, symtab)
        op = node.op
        if op in ('+', '-', '*', '/'):
            if lt != 'int' or rt != 'int':
                raise SemanticError(f"Operação aritmética inválida entre '{lt}' e '{rt}'")
            return 'int'
        if op in ('<', '<=', '>', '>=', '==', '!='):
            if lt != 'int' or rt != 'int':
                raise SemanticError(f"Comparação inválida entre '{lt}' e '{rt}'")
            return 'bool'
        if op in ('&&', '||'):
            if lt != 'bool' or rt != 'bool':
                raise SemanticError(f"Operação lógica inválida entre '{lt}' e '{rt}'")
            return 'bool'
        raise SemanticError(f"Operador desconhecido: '{op}'")

    raise SemanticError(f"Nó semântico desconhecido: {node}")
