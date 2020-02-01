"""
BINARY SEARCH TREE
* Values of all the nodes of the left subtree of any node of the tree are smaller than the value of the node.
* Values of all the nodes of the right subtree of any node are greater than the value of the node.
*
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def minimum(self, x): # To find minimum from the subtree of node X
        while x.left != None:
            x = x.left
        return x

    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y

        if y == None: # Newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

    def transplant(self, u, v): # u-v- remove u by v
        # Case 1: deleted node doesn't have any parent -> v will be the new root
        if u.parent == None:
            # Set v as root
            self.root = v
        # Case 2: if u is the left child of its parent, then v will be the left child of u's parent
        elif u == u.parent.left:
            u.parent.left = v
        # Case 3: Opposite to case 2
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
    
    def delete(self, z):
        # If the node has only one child, then we can replace it with its child cuz that wont affect the property of the bst
        # Case 1: If there is no left child of the node z, we will replace it will the right child
        if z.left == None:
            self.transplant(z, z.right)
        # Case 2: There is no right child
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z: # If y is not the direct child of z, we need to transplant the right child of y with y
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
        
    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)

if __name__ == '__main__':
    t = BinarySearchTree()

    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(100)
    e = Node(90)
    f = Node(40)
    g = Node(50)
    h = Node(60)
    i = Node(70)
    j = Node(80)
    k = Node(150)
    l = Node(110)
    m = Node(120)

    t.insert(a)
    t.insert(b)
    t.insert(c)
    t.insert(d)
    t.insert(e)
    t.insert(f)
    t.insert(g)
    t.insert(h)
    t.insert(i)
    t.insert(j)
    t.insert(k)
    t.insert(l)
    t.insert(m)
    # Full tree
    print('Full tree:\n')
    t.inorder(t.root)
    t.delete(a)
    t.delete(m)
    print('After deleting\n')
    t.inorder(t.root)


