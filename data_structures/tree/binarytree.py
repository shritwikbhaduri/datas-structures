from typing import Any, List

from pydantic import Field
from .node import Node


class BinaryTree:
    def __init__(self, data: Any = Field(default=None, description="this is the root node data")):
        self.root = Node(data=data)
        self.depth: int = 0

    def get_depth(self):
        self.depth = 0
        while self.root.left or self.root.right:
            self.depth += 1
        return self.depth

    def add_node(self, data=Field(description="enter the data value for the node")):
        node = self.root
        while node:
            if node.data > data:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(data)
                    break
            if node.data <= data:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(data)
                    break


def print_tree(node):
    node_hierarchy: List = [[node]]
    level: int = 0
    print(str(node.data if node else None))
    while True:
        for _node in node_hierarchy[level]:
            if _node:
                print(str(_node.left.data if _node.left else " ") +
                      ("/\\" if _node.left and _node.right else "\\" if _node.right and not _node.left else "/"
                      if not _node.right and _node.left else "") + str(_node.right.data if _node.right else " "),
                      end=" ")
                node_hierarchy.append(list())
                node_hierarchy[level + 1].append(_node.left if _node.left else None)
                node_hierarchy[level + 1].append(_node.right if _node.right else None)
        level += 1
        print()
        if not any(node_hierarchy[-1]):
            node_hierarchy.remove(node_hierarchy[-1])
            break
