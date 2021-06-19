"""Lexer tests"""
import textwrap

from transpiler import lexer


def test_tokenizing_all_possible_tokens():
    tokens = lexer.tokenize("<>+-.,[]")
    assert tokens == [lexer.Token(token) for token in "<>+-.,[]"]


def test_tokenizing_multiline_code_with_comments():
    tokens = lexer.tokenize(
        textwrap.dedent(
            """
            ++++    Increment cell to 4
            [       Start loop
                -   Decrement value
            ]
            """
        )
    )
    assert tokens == [lexer.Token(token) for token in "++++[-]"]
