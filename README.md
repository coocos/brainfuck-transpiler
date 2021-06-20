# brainfuck-transpiler

Transpiler for compiling [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) into Python.

## How it works

1. Brainfuck code is tokenized using a lexer
2. A parser constructs an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) from the tokens
3. The constructed Brainfuck syntax tree is translated into a Python syntax tree using the [Python ast module](https://docs.python.org/3/library/ast.html).

## Example

Given a simple Brainfuck program like this which prints "Hello world!":

```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```

The transpiler will produce a Python program like this:

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
print(chr(memory[ip]))
ip += 1
memory[ip] -= 3
print(chr(memory[ip]))
memory[ip] += 7
print(chr(memory[ip]))
print(chr(memory[ip]))
memory[ip] += 3
print(chr(memory[ip]))
ip += 2
print(chr(memory[ip]))
ip -= 1
memory[ip] -= 1
print(chr(memory[ip]))
ip -= 1
print(chr(memory[ip]))
memory[ip] += 3
print(chr(memory[ip]))
memory[ip] -= 6
print(chr(memory[ip]))
memory[ip] -= 8
print(chr(memory[ip]))
ip += 2
memory[ip] += 1
print(chr(memory[ip]))
ip += 1
memory[ip] += 2
print(chr(memory[ip]))
```
