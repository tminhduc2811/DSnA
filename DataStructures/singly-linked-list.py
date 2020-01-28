class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

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
    l.head = n

def insert_at_last(l, n):
    temp = l.head
    while temp.next != None:
        temp = temp.next
    temp.next = n

def insert_node_after(n, a):
    n.next = a.next
    a.next = n

def delete(l, n):
    temp = l.head
    if temp == n:
        # Node to be deleted is head of the linked list
        l.head = n.next
        del n
    else:
        while temp != None:
            if temp.next == n: # Node before the node to be deleted
                temp.next = n.next
                del n
                break # Exit the loop after deleting the node
            temp = temp.next

if __name__ == '__main__':
    l = LinkedList(100)
    a = Node(10)
    b = Node(50)
    c = Node(78)
    # Connecting all the nodes
    l.head.next = a
    a.next = b
    b.next = c
    print('Linked list: ', traversal(l))

    # Insert a node at the beginning of the list
    d = Node('Inserted-node')
    insert_at_beginning(l, d)
    print('Linked list after inserting a node at the beginning: ', traversal(l))

    # Insert a node after node b
    e = Node('Node-after-50')
    insert_node_after(e, b)
    print('Linked list after inserting a node after b: ', traversal(l))

    # Insert a node at the end of the list
    f = Node('last-node')
    insert_at_last(l, f)
    print('Linked list after inserting a node at the end: ', traversal(l))

    # Delete node b = 50 
    delete(l, b)
    print('Linked list after delete node b: ', traversal(l))