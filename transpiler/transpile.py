#!/usr/bin/env python3
"""Transpiler entry point"""
import ast
import fileinput

from transpiler import lexer, parser


def read_input() -> str:
    """Reads Brainfuck application from file or stdin"""
    return "".join(line for line in fileinput.input())


def transpile() -> str:
    """Transpiles the given input"""
    code = read_input()
    tokens = lexer.tokenize(code)
    tree = parser.parse(tokens)

    return ast.unparse(tree.translate())


if __name__ == "__main__":
    print(transpile())
