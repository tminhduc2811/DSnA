"""
* A queue follows FIFO (First-in, First out) policy
* Operations:
# Enqueue → Enqueue is an operation which adds an element to the queue, add an item to the tail of the queue
# Dequeue → It is similar to the pop operation of stack i.e., it returns and deletes the front element from the queue
# isEmpty → It is used to check whether the queue has any element or not.
# isFull → It is used to check whether the queue is full or not.
# Front → It is similar to the top operation of a stack i.e., it returns the front element of the queue (but don’t delete it).
"""

class Queue():
    def __init__(self, size):
        self.head = 1
        self.tail = 1
        self.Q = [0]*(size + 1)
        self.size = size

    def isEmpty(self):
        if self.head == self.tail:
            return True
        return False

    def isFull(self):
        next_tail = self.tail + 1
        # print('a', next_tail)
        if (next_tail > self.size + 1) & (self.head == 1):
            next_tail = 0
        if self.head == next_tail + 1:
            return True
        return False

    def enqueue(self, data):
        if self.isFull():
            print('Queue Overflow')
        else:
            self.Q[self.tail] = data
            # print(self.Q)
            if self.tail == self.size + 1:
                self.tail = 1
            else:
                self.tail += 1
    
    def dequeue(self):
        if self.isEmpty():
            print('Queue Underflow')
            return -1000
        else:
            q = self.Q[self.head]
            if self.head == self.size + 1:
                self.head = 1
            else:
                self.head += 1
            return q
    
    # def show(self):
    #     i = self.head
    #     while i < self.tail:
    #         print(self.Q[i])
    #         i += 1
    #         if i > self.size:
    #             i = 1

if __name__=='__main__':
    q = Queue(10)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    q.enqueue(100)
    print(q.Q)
    # q.enqueu
    # e(110)
    # q.show()
    print(q.dequeue(), q.head)