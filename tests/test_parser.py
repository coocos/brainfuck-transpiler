from transpiler import parser
from transpiler import nodes


def test_parsing_tokens():

    tokens = ["+", ">", "<", ",", ".", "[", "-", "-", "[", "-", "]", "]"]
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
