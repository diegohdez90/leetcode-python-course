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
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        tmp = self.head
        prev = self.head
        while tmp.pointer:
            prev = tmp
            tmp = tmp.pointer
        self.tail = prev
        self.tail.pointer = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp
    
    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.pointer = self.head
            self.head = node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = tmp.pointer
        tmp.pointer = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return tmp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.pointer
        
        return tmp
    
    def set(self, index, value):
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        tmp = self.get(index - 1)
        node = Node(value)
        
        node.pointer = tmp.pointer
        tmp.pointer = node
        self.length += 1
        return True
    
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(f'value: {tmp.value}')
            tmp = tmp.pointer


if __name__ == '__main__':
    __all__ =  [
        'LinkedList'
    ]