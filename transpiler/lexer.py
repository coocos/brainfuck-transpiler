"""Lexer for tokenizing Brainfuck code"""
from enum import Enum


class Token(str, Enum):
    """A single code token"""

    DECREMENT = "<"
    INCREMENT = ">"
    ADD = "+"
    SUBTRACT = "-"
    OUTPUT = "."
    INPUT = ","
    LOOP_START = "["
    LOOP_END = "]"


def tokenize(code: str) -> list[Token]:
    """Tokenizes given string of code"""
    tokens = []
    for char in code:
        try:
            tokens.append(Token(char))
        except ValueError:
            pass
    return tokens
