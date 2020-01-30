"""
    * Singly linked list is more suitable when we have limited memory and searching for elements is not our priority
    * When the limitation of memory is not our issue, and insertion, deletion task doesn't happend frequently
"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self, data):
        a = Node(data)
        self.head = a

def traversal(l):
    temp = l.head
    result = ''
    while temp != None:
        result += str(temp.data) + '\t'
        temp = temp.next
    return result

def insert_at_beginning(l, n):
    n.next = l.head
    l.head.prev = n    
    l.head = n

def insert_at_last(l, n):
    temp = l.head
    while temp.next != None:
        temp = temp.next
    temp.next = n
    n.prev = temp

def insert_node_after(n, a):
    n.next = a.next
    n.next.prev = n
    n.prev = a
    a.next = n

def delete(l, n):
    if n.prev == None: # If n is head
        l.head = n.next
    else: # n is not head
        n.prev.next = n.next
    if n.next != None:
        n.next.prev = n.prev
    del n

if __name__=='__main__':
    l = LinkedList(20)
    a = Node('node-a')
    b = Node('node-b')
    c = Node('node-c')
    
    # Connecting all nodes
    l.head.next = a
    a.next = b
    a.prev = l.head
    b.next = c
    b.prev = a
    c.prev = b
    print('Linked list: ', traversal(l))
    # Insert a node at the beginning of the list
    d = Node('Inserted-node')
    insert_at_beginning(l, d)
    print('Linked list after inserting a node at the beginning: ', traversal(l))

    # Insert a node after node b
    e = Node('Node-after-b')
    insert_node_after(e, b)
    print('Linked list after inserting a node after b: ', traversal(l))

    # Insert a node at the end of the list
    f = Node('last-node')
    insert_at_last(l, f)
    print('Linked list after inserting a node at the end: ', traversal(l))

    # Delete node b = 50 
    delete(l, b)
    print('Linked list after delete node b: ', traversal(l))
