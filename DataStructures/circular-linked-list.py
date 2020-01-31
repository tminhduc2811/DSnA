"""
! There are also many applications of a circular linked list like:

* Data that need to be run turn by turn
* Develop other data structures like Queue.
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList():
    def __init__(self, key):
        z = Node(key)
        z.next = z
        self.last = z


def insert_after(n, a):
    n.next = a.next
    a.next = n

def insert_at_last(l, n):
    n.next = l.last.next
    l.last.next = n
    l.last = n

def delete(l, n):
    temp = l.last
    while temp.next != n:
        temp = temp.next
    if n == l.last: # If n is the last node
        if n.next == n: # If n is the only node in the list
            l.last = None
        else: # More than one node and last node
            temp.next = n.next
            l.last = temp
    else: # If n is not the last node, we just need to delete it and don't have to care about the last pointer
        temp.next = n.next
    del n

def traversal(l):
    temp = l.last
    result = str(temp.data) + '\t'
    temp = temp.next
    while temp != l.last:
        result += str(temp.data) + '\t'
        temp = temp.next
    return result

if __name__=='__main__':
    l = CircularLinkedList(10)
    a = Node(20)
    b = Node(30)
    c = Node(40)

    l.last.next = a
    a.next = b
    b.next = c
    c.next = l.last

    print('Circular linked list: ', traversal(l))

    z = Node(50)
    insert_after(z, c)
    z = Node(25)
    insert_after(z, a)
    z = Node(100)
    insert_at_last(l, z)

    print('After inserting: ', traversal(l))
    delete(l, l.last)
    delete(l, b)

    print('After deleting: ', traversal(l))