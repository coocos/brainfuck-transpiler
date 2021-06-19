"""Parser for constructing a Brainfuck AST"""
from dataclasses import dataclass, field
from typing import List

from . import nodes


@dataclass
class AbstractSyntaxTree:
    """Abstract syntax tree representing a Brainfuck program"""

    body: List[nodes.Node] = field(default_factory=list)


def parse(tokens: List[str]) -> AbstractSyntaxTree:
    """Parses tokens and constructs an abstract syntax tree"""

    tree = AbstractSyntaxTree()
    stack = [tree.body]

    for token in tokens:
        body = stack[-1]
        if token == "<":
            body.append(nodes.DecrementPointer())
        elif token == ">":
            body.append(nodes.IncrementPointer())
        if token == "+":
            body.append(nodes.IncrementValue())
        elif token == "-":
            body.append(nodes.DecrementValue())
        if token == ".":
            body.append(nodes.OutputValue())
        elif token == ",":
            body.append(nodes.ReadValue())
        elif token == "[":
            loop = nodes.Loop()
            body.append(loop)
            stack.append(loop.body)
        elif token == "]":
            stack.pop()

    return tree
