# ast_nodes.py

class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'Number({self.value})'

class BoolLiteral(ASTNode):
    def __init__(self, value: bool):
        self.value = value
    def __repr__(self):
        return f'BoolLiteral({self.value})'

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Variable({self.name})'

class BinOp(ASTNode):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
    def __repr__(self):
        return f'BinOp({self.op}, {self.left}, {self.right})'

class UnaryOp(ASTNode):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    def __repr__(self):
        return f'UnaryOp({self.op}, {self.operand})'

class Assign(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    def __repr__(self):
        return f'Assign({self.name}, {self.expr})'

class If(ASTNode):
    def __init__(self, cond, then_branch, else_branch):
        self.cond = cond
        self.then_branch = then_branch
        self.else_branch = else_branch
    def __repr__(self):
        return f'If({self.cond}, {self.then_branch}, {self.else_branch})'

class While(ASTNode):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body
    def __repr__(self):
        return f'While({self.cond}, {self.body})'

class For(ASTNode):
    def __init__(self, init, cond, post, body):
        self.init = init
        self.cond = cond
        self.post = post
        self.body = body
    def __repr__(self):
        return f'For({self.init}, {self.cond}, {self.post}, {self.body})'

class Function(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params    # list of parameter names
        self.body = body        # Block
    def __repr__(self):
        return f'Function({self.name}, {self.params}, {self.body})'

class Return(ASTNode):
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f'Return({self.expr})'

class Block(ASTNode):
    def __init__(self, stmts):
        self.stmts = stmts
    def __repr__(self):
        return f'Block({self.stmts})'
