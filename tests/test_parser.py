from transpiler import lexer, parser, nodes


def test_parsing_tokens():

    tokens = [
        lexer.Token(token)
        for token in ["+", ">", "<", ",", ".", "[", "-", "-", "[", "-", "]", "]"]
    ]
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
