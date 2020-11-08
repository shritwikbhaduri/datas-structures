from typing import Any, List

from data_structures.linked_list.node import Node


class SinglyLinkedList:
    """
    This class is responsible for handling all operations related to linked list
    """

    def __init__(self, data: Any = None):
        self.__head: Node = Node(data=data)
        self.__tail: Node = self.__head
        self.__length: int = 1

    def get_list_length(self):
        node = self.__head
        while node.next_node:
            self.__length += 1
            node = node.next_node
        return self.__length

    def get_node(self, data) -> List[Node]:
        """
        iterates over the whole list and returns all the nodes with the given data.
        :param data:
        :return list of nodes holding given value:
        """
        node = self.__head
        final_list = list()
        while node != self.__tail:
            if node.data == data:
                final_list.append(node)
        return final_list

    def get_all_node(self) -> List:
        """
        returns a list of all node data present in the singly linked list.
        :return list of data present in singly linked list:
        """
        final_list = list()
        node = self.__head
        while node != self.__tail:
            final_list.append(node.data)
            node = node.next_node
        return final_list

    def add_node(self, data: Any) -> Node:
        """
        adds a node with the given data at the end of the linked list and returns the update tail node
        :param data: holds the value for the node
        :return tail node: pointer to last node
        """
        node = self.__tail
        node.next_node = Node(data=data)
        self.__tail = node.next_node
        return self.__tail

    def add_all_nodes(self, data_list: List):
        """
        adds the elements for the given `data_list` in a singly linked list
        :param data_list: list of values that needs to be added to the list
        :return: status_flag and message
        """
        node = self.__tail
        success: bool = False
        message: str = ""
        try:
            for data in data_list:
                node.next_node = Node(data=data)
                node = node.next_node
            success = True
            message = "added successfully"
        except RuntimeError as e:
            success = False
            message = f"error in adding node:{e}"
        finally:
            return success, message

    def delete_first_node(self):
        """
        deletes the first node
        :return: returns new head
        """
        node = self.__head
        self.__head = node.next_node

    def delete_last_node(self):
        """
        deletes the last node
        :return:  returns new tail
        """
        node = self.__head
        while node.next_node.next_node:
            node = node.next
        node.next_node = None
        self.__tail = node

    def delete_node(self, data: Any, all_matched: bool = False):
        """
        deletes the node with the data and condition. by default `all_matched` and `last_matched` are `False`.
        :param data: data of the node to be deleted.
        :param all_matched: bool flag, default is false, if true all matched nodes will be deleted
        :return: status_flag, message
        """
        node = self.__head
        delete_count: int = 0
        if node.data == data:
            self.delete_first_node()
            return "successful", f"first node with value {data} removed"
        while node:
            if not all_matched and node.next_node.data == data:
                node.next_node = node.next_node.next_node
                return "successful", f"first matched node with value {data} removed"
            if all_matched and node.next_node.data == data:
                node.next_node = node.next_node.next_node
        return "successful", f"{delete_count} nodes with value {data} removed"

    def print(self, offset: int = 0):
        """
        prints the given singly linked list
        :param offset: gives the number of values to be skipped from printing
        :return: None
        """
        node = self.__head
        while node:
            if offset:
                offset -= 1
                node = node.next_node
                continue
            print(node.data, end=f"{'->' if node.next_node else ''}")
            node = node.next_node
