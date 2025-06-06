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
    
    def test_pop(self):
        ll = LinkedList(9)
        item = ll.pop()
        self.assertEqual(item.value, 9)
        self.assertEqual(ll.length, 0)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_empty_pop(self):
        ll = LinkedList(8)
        ll.append(13)
        ll.append(6)
        ll.append(10)
        tmp = ll.pop()
        self.assertEqual(ll.length, 3)
        self.assertEqual(tmp.value, 10)
        
    def test_prepend(self):
        ll = LinkedList(17)
        ll.prepend(5)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 17)
        self.assertEqual(ll.length, 2)
        
        
    def test_prepend_with_pop(self):
        ll = LinkedList(8)
        ll.append(13)
        ll.append(6)
        ll.append(10)
        while(ll.head):
            ll.pop()
        
        ll.prepend(4)
        self.assertEqual(ll.head.value, 4)
        self.assertEqual(ll.tail.value, 4)
        self.assertEqual(ll.length, 1)
    
    def test_pop_first(self):
        ll = LinkedList(23)
        tmp = ll.pop_first()
        self.assertEqual(tmp.value, 23)
        self.assertEqual(ll.length, 0)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
    
    def test_pop_first_with_values(self):
        ll = LinkedList(5)
        ll.append(15)
        ll.append(7)
        ll.append(9)
        tmp = ll.pop_first()
        self.assertEqual(tmp.value, 5)
        self.assertEqual(ll.length, 3)
        self.assertEqual(ll.head.value, 15)

    def test_get(self):
        ll = LinkedList(7)
        ll.append(1)
        ll.append(4)
        ll.append(9)
        ll.append(14)
        
        item = ll.get(2)
        self.assertEqual(item.value, 4)
        item = ll.get(-1)
        self.assertIsNone(item)
        item = ll.get(5)
        self.assertIsNone(item)
        item = ll.get(4)
        self.assertEqual(item.value, 14)
    
    def test_set(self):
        ll = LinkedList(2)
        ll.append(18)
        ll.append(11)
        ll.append(3)
        ll.append(8)
        ll.append(15)
        ll.append(12)
        
        result = ll.set(-1, 6)
        self.assertFalse(result)
        result = ll.set(7, 1)
        self.assertFalse(result)
        result = ll.set(6, 5)
        self.assertTrue(result)
        self.assertEqual(ll.tail.value, 5)
        result = ll.set(0, 9)
        self.assertTrue(result)
        self.assertEqual(ll.head.value, 9)
        result = ll.set(4, 7)
        self.assertTrue(result)
        node = ll.get(4)
        self.assertEqual(node.value, 7)
    
    def test_insert(self):
        ll = LinkedList(7)
        ll.append(2)
        ll.append(15)
        ll.append(8)
        ll.append(12)
        ll.append(4)
        ll.append(9)
        
        result = ll.insert(-1, 3)
        self.assertFalse(result)
        result = ll.insert(8, 14)
        self.assertFalse(result)
        result = ll.insert(7, 6)
        self.assertTrue(result)
        self.assertEqual(ll.tail.value, 6)
        self.assertEqual(ll.length, 8)
        
        result = ll.insert(0, 5)
        self.assertTrue(result)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.length, 9)
        
        result = ll.insert(4, 11)
        node = ll.get(4)
        self.assertTrue(result)
        self.assertEqual(node.value, 11)
        self.assertEqual(ll.length, 10)
    
    
if __name__ == '__main__':
    unittest.main()
