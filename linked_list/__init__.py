from .node import Node

class LinkedList:
    head = None
    tail = None
    
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1


if __name__ == '__main__':
    __all__ =  [
        'LinkedList'
    ]