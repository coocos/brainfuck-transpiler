"""Parser for constructing a Brainfuck AST"""
import ast
from dataclasses import dataclass, field
from typing import List

from transpiler import lexer, nodes


@dataclass
class AbstractSyntaxTree:
    """Abstract syntax tree representing a Brainfuck program"""

    body: List[nodes.Node] = field(default_factory=list)

    def translate(self) -> ast.Module:
        """Translates the AST into a Python AST"""
        memory = ast.Assign(
            targets=[ast.Name(id="memory", ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.List(elts=[ast.Constant(value=0)], ctx=ast.Load()),
                op=ast.Mult(),
                right=ast.Constant(value=30000),
            ),
        )
        pointer = ast.Assign(
            targets=[ast.Name(id="ip", ctx=ast.Store())], value=ast.Constant(value=0)
        )
        expressions = [node.translate() for node in self.body]
        module = ast.Module(body=[memory, pointer] + expressions, type_ignores=[])
        ast.fix_missing_locations(module)  # Generate line numbers for nodes
        return module


def parse(tokens: List[lexer.Token]) -> AbstractSyntaxTree:
    """Parses tokens and constructs an abstract syntax tree"""

    tree = AbstractSyntaxTree()
    stack = [tree.body]

    for token in tokens:

        body = stack[-1]
        if token is lexer.Token.DECREMENT:
            body.append(nodes.DecrementPointer())
        elif token is lexer.Token.INCREMENT:
            body.append(nodes.IncrementPointer())
        elif token is lexer.Token.ADD:
            body.append(nodes.IncrementValue())
        elif token is lexer.Token.SUBTRACT:
            body.append(nodes.DecrementValue())
        elif token is lexer.Token.OUTPUT:
            body.append(nodes.OutputValue())
        elif token is lexer.Token.INPUT:
            body.append(nodes.ReadValue())
        elif token is lexer.Token.LOOP_START:
            loop = nodes.Loop()
            body.append(loop)
            stack.append(loop.body)
        elif token is lexer.Token.LOOP_END:
            stack.pop()
        else:
            raise TypeError(f"Unknown token type: {token}")

    return tree
