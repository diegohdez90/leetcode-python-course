import unittest
from linked_list import LinkedList
from log import log
class test_linked_list(unittest.TestCase):
    
    def test_constructor(self):
        ll = LinkedList(6)   
        self.assertEqual(ll.head.value, 6)
        self.assertEqual(ll.tail.value, 6)
        self.assertEqual(ll.length, 1)

if __name__ == '__main__':
    unittest.main()