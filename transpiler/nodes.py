"""Abstract syntax tree node definitions"""
import ast
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


class Node(ABC):
    """Base class for all tree nodes"""

    @abstractmethod
    def translate(self) -> Any:
        """Translates the Brainfuck node to a Python node"""


@dataclass
class IncrementPointer(Node):
    """Increments pointer"""

    value: int = 1

    def translate(self) -> ast.AugAssign:
        """Translates > to pointer += 1"""
        return ast.AugAssign(
            target=ast.Name(id="pointer", ctx=ast.Store()),
            op=ast.Add(),
            value=ast.Constant(value=self.value),
        )


@dataclass
class DecrementPointer(Node):
    """Decrements pointer"""

    value: int = 1

    def translate(self) -> ast.AugAssign:
        """Translates < to pointer -= 1"""
        return ast.AugAssign(
            target=ast.Name(id="pointer", ctx=ast.Store()),
            op=ast.Sub(),
            value=ast.Constant(value=self.value),
        )


@dataclass
class IncrementValue(Node):
    """Increments value at pointer"""

    value: int = 1

    def translate(self) -> ast.AugAssign:
        """Translates + to memory[pointer] += 1"""
        return ast.AugAssign(
            target=ast.Subscript(
                value=ast.Name(id="memory", ctx=ast.Load()),
                slice=ast.Name(id="pointer", ctx=ast.Load()),
                ctx=ast.Store(),
            ),
            op=ast.Add(),
            value=ast.Constant(self.value),
        )


@dataclass
class DecrementValue(Node):
    """Decrements value at pointer"""

    value: int = 1

    def translate(self) -> ast.AugAssign:
        """Translates - to memory[pointer] -= 1"""
        return ast.AugAssign(
            target=ast.Subscript(
                value=ast.Name(id="memory", ctx=ast.Load()),
                slice=ast.Name(id="pointer", ctx=ast.Load()),
                ctx=ast.Store(),
            ),
            op=ast.Sub(),
            value=ast.Constant(self.value),
        )


@dataclass
class OutputValue(Node):
    """Outputs value at pointer location"""

    def translate(self) -> ast.Expr:
        """Translates . to print(chr(memory[pointer]))"""
        return ast.Expr(
            ast.Call(
                func=ast.Name(
                    id="print",
                    ctx=ast.Load(),
                ),
                args=[
                    ast.Call(
                        func=ast.Name(id="chr", ctx=ast.Load()),
                        args=[
                            ast.Subscript(
                                value=ast.Name(id="memory", ctx=ast.Load()),
                                slice=ast.Name(id="pointer", ctx=ast.Load()),
                                ctx=ast.Store(),
                            )
                        ],
                        keywords=[],
                    )
                ],
                keywords=[ast.keyword(arg="end", value=ast.Constant(value=""))],
            )
        )


@dataclass
class ReadValue(Node):
    """Reads input value and stores it at pointer location"""

    def translate(self) -> ast.Assign:
        """Translates , to memory[pointer] = ord(input()[0])"""
        return ast.Assign(
            targets=[
                ast.Subscript(
                    value=ast.Name(id="memory", ctx=ast.Load()),
                    slice=ast.Name(id="pointer", ctx=ast.Load()),
                    ctx=ast.Store(),
                )
            ],
            value=ast.Call(
                func=ast.Name(id="ord", ctx=ast.Load()),
                args=[
                    ast.Subscript(
                        value=ast.Call(
                            func=ast.Name(id="input", ctx=ast.Load()),
                            args=[],
                            keywords=[],
                        ),
                        slice=ast.Constant(value=0),
                        ctx=ast.Load(),
                    )
                ],
                keywords=[],
            ),
        )


@dataclass
class Loop(Node):
    """Loops until value at pointer is zero"""

    body: list[Node] = field(default_factory=list)

    def translate(self) -> ast.While:
        """Translates [] to while memory[pointer] != 0:"""
        return ast.While(
            test=ast.Compare(
                left=ast.Subscript(
                    value=ast.Name(id="memory", ctx=ast.Load()),
                    slice=ast.Name(id="pointer", ctx=ast.Load()),
                    ctx=ast.Load(),
                ),
                ops=[ast.NotEq()],
                comparators=[ast.Constant(value=0)],
            ),
            body=[node.translate() for node in simplify(self.body)],
            orelse=[],
        )


def simplify(nodes: list[Node]) -> list[Node]:
    """
    Simplifies a sequence of nodes by merging identical back-to-back statements.

    For example, a Brainfuck sequence like << could be transpiled to multiple repeated
    Python assignments like:

        pointer -= 1
        pointer -= 1

    However, by merging the nodes the sequence can be transpiled more fluently:

        pointer -= 2
    """
    simplifiable_nodes = (
        IncrementPointer,
        DecrementPointer,
        IncrementValue,
        DecrementValue,
    )
    stack = [nodes[0]]
    for node in nodes[1:]:
        if isinstance(node, simplifiable_nodes) and isinstance(node, type(stack[-1])):
            node.value = stack.pop().value + 1
        stack.append(node)
    return stack
