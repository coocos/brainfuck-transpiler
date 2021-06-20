"""Parser tests"""
import ast
import textwrap
from transpiler import lexer, parser, nodes


def test_parsing_tokens():

    tokens = [lexer.Token(token) for token in "+><,.[--[-]]"]
    tree = parser.parse(tokens)

    assert tree.body == [
        nodes.IncrementValue(),
        nodes.IncrementPointer(),
        nodes.DecrementPointer(),
        nodes.ReadValue(),
        nodes.OutputValue(),
        nodes.Loop(
            [
                nodes.DecrementValue(),
                nodes.DecrementValue(),
                nodes.Loop([nodes.DecrementValue()]),
            ]
        ),
    ]


def test_tree_translation():

    tokens = [lexer.Token(token) for token in "+><,.[--[-]]"]
    tree = parser.parse(tokens)

    generated = ast.unparse(tree.translate()).strip()
    expected = textwrap.dedent(
        """
        memory = [0] * 30000
        pointer = 0
        memory[pointer] += 1
        pointer += 1
        pointer -= 1
        memory[pointer] = ord(input()[0])
        print(chr(memory[pointer]), end='')
        while memory[pointer] != 0:
            memory[pointer] -= 2
            while memory[pointer] != 0:
                memory[pointer] -= 1
        """
    )

    assert generated == expected.strip()
