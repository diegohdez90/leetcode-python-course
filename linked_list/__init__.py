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
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 2:
            tmp = self.tail
            self.head.pointer = None
            self.tall = self.head
        else:
            tmp = self.head
            prev = self.head
            while tmp.pointer != None:
                prev = tmp
                tmp = tmp.pointer
            self.tail = prev
            self.tail.pointer = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp
        
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(f'value: {tmp.value}')
            tmp = tmp.pointer


if __name__ == '__main__':
    __all__ =  [
        'LinkedList'
    ]