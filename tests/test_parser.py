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
        ip = 0
        memory[ip] += 1
        ip += 1
        ip -= 1
        memory[ip] = input()[0]
        print(memory[ip])
        while memory[ip] != 0:
            memory[ip] -= 1
            memory[ip] -= 1
            while memory[ip] != 0:
                memory[ip] -= 1
        """
    )

    assert generated == expected.strip()
