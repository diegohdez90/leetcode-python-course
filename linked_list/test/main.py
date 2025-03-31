from linked_list import LinkedList
from log import log

def test_linked_list_init_value():
    ll = LinkedList(6)
    assert ll.head.value == 6, "head should be 6"
    assert ll.tail.value == 6, "tail should be 6"
    assert ll.length == 1, 'length must be 1'

def test_linked_list_append():
    ll = LinkedList(6)
    ll.append(2)
    assert ll.head.value == 6, "head should be 6"
    assert ll.tail.value == 2, "tail should be 2"
    assert ll.head.pointer.value == 2, 'head value 6 pointer to 2'
    assert ll.length == 2, 'length must be 2'

def test_linked_list_append_multiple_values():
    ll = LinkedList(6)
    ll.append(8)
    ll.append(14)
    ll.append(9)
    assert ll.head.value == 6, "head should be 6"
    assert ll.tail.value == 9, "tail should be 9"
    assert ll.head.pointer.value == 8, 'head value 6 pointer to 8'
    assert ll.length == 4, 'length must be 4'

if __name__ == '__main__':
    test_linked_list_init_value()
    test_linked_list_append()
    test_linked_list_append_multiple_values()
    log.info('Test passed')
