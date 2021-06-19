"""Node definitions for an abstract syntax tree"""
from abc import ABC
from dataclasses import dataclass, field
from typing import List


class Node(ABC):
    """Node in abstract syntax tree"""


@dataclass
class IncrementPointer(Node):
    """Increments pointer"""

    pass


@dataclass
class DecrementPointer(Node):
    """Decrements pointer"""

    pass


@dataclass
class IncrementValue(Node):
    """Increments value at pointer"""

    pass


@dataclass
class DecrementValue(Node):
    """Decrements value at pointer"""

    pass


@dataclass
class OutputValue(Node):
    """Outputs byte at pointer location"""

    pass


@dataclass
class ReadValue(Node):
    """Reads one byte of input and stores it at pointer location"""

    pass


@dataclass
class Loop(Node):
    body: List[Node] = field(default_factory=list)
