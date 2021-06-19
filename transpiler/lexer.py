"""Lexer for tokenizing brainfuck code"""
from typing import List


def tokenize(code: str) -> List[str]:
    """Tokenizes given string of code"""
    tokens = []
    for char in code:
        # Decrement pointer
        if char == "<":
            tokens.append(char)
        # Increment pointer
        elif char == ">":
            tokens.append(char)
        # Increment value at pointer
        elif char == "+":
            tokens.append(char)
        # Decrement value at pointer
        elif char == "-":
            tokens.append(char)
        # Output byte at pointer
        elif char == ".":
            tokens.append(char)
        # Read byte and store it at pointer location
        elif char == ",":
            tokens.append(char)
        # Start loop
        elif char == "[":
            tokens.append(char)
        # End loop
        elif char == "]":
            tokens.append(char)
        else:
            continue
    return tokens
