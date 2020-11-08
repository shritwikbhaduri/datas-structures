from data_structures.tree.binarytree import BinaryTree, print_tree
from data_structures.linked_list.singly_linked_list import SinglyLinkedList
# a = BinaryTree(60)
# a.add_node(10)
# a.add_node(1)
# a.add_node(4)
# a.add_node(9)
# a.add_node(10)
# a.add_node(8)
# a.add_node(2)
# a.add_node(7)
# a.add_node(11)
#
# # print(a.get_depth())
# print_tree(a.root)

a = SinglyLinkedList(2)
a.add_node(10)
print(a.add_all_nodes([1, 2, 3, 4, 5, 6, 7, 8]))
a.print()
print(a.get_all_node())

