from .. import LinkedList
from ..log import log

def test_linked_list_init_value():
    ll = LinkedList(6)
    assert ll.head.value == 6, "head should be 6"
    assert ll.tail.value == 6, "tail should be 6"
    
if __name__ == '__main__':
    test_linked_list_init_value()
    log.info('Test passed')
