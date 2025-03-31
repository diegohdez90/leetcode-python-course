import unittest
from linked_list import LinkedList
from log import log
class test_linked_list(unittest.TestCase):
    
    def test_constructor(self):
        ll = LinkedList(6)   
        self.assertEqual(ll.head.value, 6)
        self.assertEqual(ll.tail.value, 6)
        self.assertEqual(ll.length, 1)
        
    def test_append(self):
        ll = LinkedList(9)
        ll.append(16)
        self.assertEqual(ll.head.value, 9)
        self.assertEqual(ll.head.pointer.value, 16)
        self.assertEqual(ll.tail.value, 16)
        self.assertEqual(ll.length, 2)

if __name__ == '__main__':
    unittest.main()
