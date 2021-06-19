"""Parser for constructing a Brainfuck AST"""
from dataclasses import dataclass, field
from typing import List

from transpiler import lexer, nodes


@dataclass
class AbstractSyntaxTree:
    """Abstract syntax tree representing a Brainfuck program"""

    body: List[nodes.Node] = field(default_factory=list)


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
