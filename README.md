# brainfuck-transpiler

Transpiler for compiling [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) into Python.

## How it works

1. Brainfuck code is tokenized using a lexer
2. A parser constructs an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) from the tokens
3. The constructed Brainfuck syntax tree is translated into a Python syntax tree using the [Python ast module](https://docs.python.org/3/library/ast.html).
