class Node:
    data: str
    child_1: "Node"
    child_2: "Node"

    def __init__(self, data, child_1=None, child_2=None):
        self.data = data
        self.child_1 = child_1
        self.child_2 = child_2

class BinaryTree:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure_first_child(self):
        current_node = self.head
        while (current_node.child_1 is not None ):
                print(f'Parent node: {current_node.data}')
                if current_node.child_1:
                    print(f'First child: {current_node.child_1.data}')
                if current_node.child_2:
                    print(f'Second child: {current_node.child_2.data}')
                    # current_node = current_node.child_2
                    # while (current_node.child_1 is not None):
                    #     print(f'Parent node: {current_node.data}')
                    # if current_node.child_1:
                    #     print(f'First child: {current_node.child_1.data}')
                    # elif current_node.child_2:
                    #     print(f'Second child: {current_node.child_2.data}')
                    # current_node = current_node.child_1
                
                current_node = current_node.child_1
                        # while (current_node.child_2 is not None ):
        #         print(f'Parent node: {current_node.data}')
        #         if current_node.child_1:
        #             print(f'First child: {current_node.child_1.data}')
        #         if current_node.child_2:
        #             print(f'Second child: {current_node.child_2.data}')
                
        #         current_node = current_node.child_2
    
    def print_structure_second_child(self):
        current_node = self.head
        while (current_node.child_2 is not None ):
                print(f'Parent node: {current_node.data}')
                if current_node.child_1:
                    print(f'First child: {current_node.child_1.data}')
                if current_node.child_2:
                    print(f'Second child: {current_node.child_2.data}')
                current_node = current_node.child_2


third_child = Node("I'm the first following child")
fourth_child = Node("I'm the second following child")
fifth_child = Node("I'm the following child for the second node")
first_child = Node("I'm the first child", third_child, fourth_child)
second_child = Node("I'm the second child", fifth_child)
parent_node = Node("I'm the parent node ",first_child, second_child)

binary_tree = BinaryTree(parent_node)

binary_tree.print_structure_first_child()
binary_tree.print_structure_second_child()



