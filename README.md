# brainfuck-transpiler

Transpiler for compiling [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) to Python.

[![test](https://github.com/coocos/brainfuck-transpiler/actions/workflows/test.yml/badge.svg)](https://github.com/coocos/brainfuck-transpiler/actions/workflows/test.yml)

## How it works

1. Brainfuck code is tokenized using a lexer
2. A parser constructs an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) from the tokens
3. The constructed Brainfuck syntax tree is translated to a Python syntax tree using the [Python ast module](https://docs.python.org/3/library/ast.html).

## Examples

### Transpiling Brainfuck to Python

The following example reads a Brainfuck program from stdin, transpiles it to Python and prints the resulting program to stdout:

```shell
echo '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.' | poetry run transpiler/transpile.py
```

```python
memory = [0] * 30000
ip = 0
memory[ip] += 8
while memory[ip] != 0:
    ip += 1
    memory[ip] += 4
    while memory[ip] != 0:
        ip += 1
        memory[ip] += 2
        ip += 1
        memory[ip] += 3
        ip += 1
        memory[ip] += 3
        ip += 1
        memory[ip] += 1
        ip -= 4
        memory[ip] -= 1
    ip += 1
    memory[ip] += 1
    ip += 1
    memory[ip] += 1
    ip += 1
    memory[ip] -= 1
    ip += 2
    memory[ip] += 1
    while memory[ip] != 0:
        ip -= 1
    ip -= 1
    memory[ip] -= 1
ip += 2
print(chr(memory[ip]), end='')
ip += 1
memory[ip] -= 3
print(chr(memory[ip]), end='')
memory[ip] += 7
print(chr(memory[ip]), end='')
print(chr(memory[ip]), end='')
memory[ip] += 3
print(chr(memory[ip]), end='')
ip += 2
print(chr(memory[ip]), end='')
ip -= 1
memory[ip] -= 1
print(chr(memory[ip]), end='')
ip -= 1
print(chr(memory[ip]), end='')
memory[ip] += 3
print(chr(memory[ip]), end='')
memory[ip] -= 6
print(chr(memory[ip]), end='')
memory[ip] -= 8
print(chr(memory[ip]), end='')
ip += 2
memory[ip] += 1
print(chr(memory[ip]), end='')
ip += 1
memory[ip] += 2
print(chr(memory[ip]), end='')

```

### Executing the transpiled program

Since the transpiled program is written to stdout, you can execute it directly by piping the result to the Python interpreter:

```shell
echo '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.' | poetry run transpiler/transpile.py | python3

Hello World!
```
