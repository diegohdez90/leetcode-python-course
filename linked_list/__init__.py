from .node import Node

class LinkedList:
    head = None
    tail = None
    
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            tmp = self.tail
            tmp.pointer = node
            self.tail = node
        self.length += 1
        
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(f'value: {tmp.value}')
            tmp = tmp.pointer


if __name__ == '__main__':
    __all__ =  [
        'LinkedList'
    ]