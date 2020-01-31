"""
! Stack is both Abstract Data Type (ADT) and Data Structures
* Stack follows Last In First Out policy. It means that the last item which enter the stack will be removed first
* Operations: Push, Pop, Top, IsEmpty. While Top return the top-most element of a stack without remove it
* Applications of stack:
-- Backtracking algorithms
-- Implement undo/redo functionality in software
-- Check proper opening and closing parenthesis
"""

class StackUsingArray(): # Stack using Array
    def __init__(self, size):
        self.size = size
        self.data = [0]*(size + 1)
        self.top = 0
    def is_empty(self):
        if self.top == 0:
            return True
        return False
    def push(self, data):
        self.top += 1
        if self.top > self.size:
            print('Stack overflow')
            return(-1000)
        else:
            self.data[self.top] = data
    def pop(self, data):
        if self.is_empty():
            print('Stack underflow')
            return(-1000)
        else:
            self.top -= 1
            return self.data[self.top + 1]


class Node():
    def __init__(self, data):
        self.next = None
        self.data = data


class StackUsingLinkedList():
    def __init__(self):
        self.head = None
        self.top = None

    
def traversal(s):
    temp = s.head
    result = ''
    
    while temp != None:
        result += str(temp.data) + '\t'
        temp = temp.next
    return result

def is_empty(s):
    if s.top == None:
        return True
    return False

def push(s, n):
    if is_empty(s):
        s.head = n
        s.top = n
    else:
        s.top.next = n
        s.top = n

def pop(s):
    if is_empty(s):
        print('Stack underflow')
        return(-1000)
    else:
        data = s.top.data
        if s.top == s.head: # Only 1 data
            s.top = None
            s.head = None
        else:
            temp = s.head
            while temp.next != s.top:
                temp = temp.next
            temp.next = None
            del s.top
            s.top = temp
        return data

if __name__=='__main__':
    # stack = StackUsingArray(5)
    # stack.push(10)
    # stack.push(20)
    # stack.push(30)
    # stack.push(40)
    # stack.push(50)
    # stack.push(60)
    # print(stack.data[1:stack.size+1])

    s = StackUsingLinkedList()

    a = Node(10)
    b = Node(20)
    c = Node(30)

    pop(s)
    push(s, a)
    push(s, b)
    push(s, c)

    print(traversal(s))
    pop(s)
    print(traversal(s))