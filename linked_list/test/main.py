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

def test_pop_linked_list_values():
    ll = LinkedList(15)
    ll.append(3)
    ll.append(11)
    ll.append(7)
    tmp = ll.pop()
    assert ll.tail.value == 11, "tail should be 11"
    assert tmp.value == 7, "tmp should be 7"
    tmp = ll.pop()
    assert ll.tail.value == 3, "tail should be 3"
    assert tmp.value == 11, "tmp should be 11"
    tmp = ll.pop()
    assert ll.tail.value == 15, "tail should be 15"
    assert tmp.value == 3, "tmp should be 3"
    tmp = ll.pop()
    assert ll.tail == None, "tail should be None"
    assert tmp.value == 15, "tmp should be 15"

def test_prepend():
    ll = LinkedList(4)
    ll.prepend(7)
    assert ll.tail.value == 4, "tail should be 4"
    assert ll.head.value == 7, "tmp should be 7"

def test_prepend_empty_ll():
    ll = LinkedList(4)
    _ = ll.pop()
    ll.prepend(8)
    assert ll.tail.value == 8, "tail should be 8"
    assert ll.head.value == 8, "tmp should be 8"


if __name__ == '__main__':
    test_linked_list_init_value()
    test_linked_list_append()
    test_linked_list_append_multiple_values()
    test_pop_linked_list_values()
    test_prepend()
    test_prepend_empty_ll()
    log.info('Test passed')
