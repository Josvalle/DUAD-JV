class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def push(self,node):
        self.head = node

    def pop(self):
        self.head = self.head.next




third_node = Node("I'm the third node")
second_node = Node("I'm the second node", third_node)
first_node = Node("I'm the first node", second_node)

stack = Stack(first_node)
stack.print_structure()

fourth_node = Node('I am the fourth node', stack.head)
print('Pushing')
stack.push(fourth_node)
stack.print_structure()

print('Pushing')

fifth_node = Node('I am the fifth node', stack.head)
stack.push(fifth_node)
stack.print_structure()

stack.pop()
print('Removing')
stack.print_structure()