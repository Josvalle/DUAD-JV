class Node:
    data:  int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def order_linked_list(self):
        was_change = True
        while was_change:
            current_node = self.head
            was_change = False
            while (current_node.next is not None):
                if current_node.data > current_node.next.data:
                    print(f'Change of data note {current_node.data} is higher than {current_node.next.data}')
                    higher_node = current_node.data
                    current_node.data = current_node.next.data
                    current_node.next.data = higher_node
                    was_change = True
                current_node = current_node.next


third_node = Node(1)
second_node = Node(20, third_node)
first_node = Node(30, second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()
for i in range(0,3):
    linked_list.order_linked_list()
linked_list.print_structure()
