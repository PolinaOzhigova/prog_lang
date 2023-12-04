from .parser import Parser
from .ast import Number, BinOp, UnaryOp

class NodeVisitor:
    
    def visit(self):
        pass

class Interpreter(NodeVisitor):
    
    def __init__(self):
        self.parser = Parser()

    def visit(self, node):
        if isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, UnaryOp):
            return self.visit_unaryop(node)
        else:
            raise ValueError("Invalid node")

    def visit_number(self, node):
        return float(node.token.value)

    def visit_unaryop(self, node):
        match node.op.value:
            case "-":
                return -self.visit(node.number)
            case "+":
                return self.visit(node.number)
            case _:
                raise ValueError("Invalid operator")

    def visit_binop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            case _:
                raise ValueError("Invalid operator")

    def eval(self, code, as_tree=False):
        tree = self.parser.parse(code)
        if as_tree:
            return tree
        return self.visit(tree)
