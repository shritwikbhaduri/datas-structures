from typing import Any


class Node:
    """
    this class is responsible for singly linked list node creation and operations.
    """

    def __init__(self, data, next_node=None):
        self.data: Any = data
        self.next_node: Node = next_node


class DoubleNode(Node):
    def __init__(self, data, next_node=None, previous_node=None):
        super().__init__(data, next_node)
        self.previous_node: Node = previous_node
