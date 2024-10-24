class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def push_left(self,node):
        self.head = node

    def pop_left(self):
        if self.head:
            self.head = self.head.next
    
    def push_right(self,node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node

    def pop_right(self):
        if self.head:
            current_node = self.head

            while current_node.next.next is not None:
                current_node = current_node.next
                
            current_node.next = None

third_node = Node("I'm the third node")
second_node = Node("I'm the second node", third_node)
first_node = Node("I'm the first node", second_node)

double_ended_queue = DoubleEndedQueue(first_node)
double_ended_queue.print_structure()

fourth_node = Node("I'm the fourth node", first_node)

print('Push left ')

double_ended_queue.push_left(fourth_node)

double_ended_queue.print_structure()

fifth_node = Node("I'm the fifth node")

print('Push right ')

double_ended_queue.push_right(fifth_node)

double_ended_queue.print_structure()

print('Pop left')

double_ended_queue.pop_left()
double_ended_queue.print_structure()

print('Pop right')

double_ended_queue.pop_right()

double_ended_queue.print_structure()












