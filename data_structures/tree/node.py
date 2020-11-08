from typing import Any

from pydantic import BaseModel, Field


# class NodeModel(BaseModel):
#     num_references: int = Field(gt=0, lt=50, default=0, description="specifies the number of child node to be "
#                                                                     "referenced")
#     data: Any = Field(default=None, description="holds the data for the node")


# class Node:
#     """
#     this class is responsible for node creation and operations.
#     """

    # def __init__(self, num_references, data):
    #     self.num_references = num_references
    #     self.data = data

    # @staticmethod
    # def generate_node(num_of_nodes, data: Any = None):
    #     return Node(data=data)


class Node:
    """
    this class is responsible for binary node creation and operations.
    """

    def __init__(self, data):
        self.data: Any = data
        self.left: Node = None
        self.right: Node = None


