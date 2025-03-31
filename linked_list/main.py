import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from linked_list import LinkedList

if __name__ == '__main__':
    ll = LinkedList(7)
    print(ll.head.value)
    print(ll.tail.value)
    ll.append(10)
    print(ll.tail.value)
    ll.print_list()
