red = 'Red'
black = 'Black'

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = red
        self.parent = None


class RedBlackBSTree:
    def __init__(self):
        nil_node = TreeNode(0)
        nil_node.color = black
        self.NIL = nil_node
        self.root = self.NIL


    def left_rotate(self, x): # ! 4 nodes will be changed: x, x.right, x.right.left, x.parent
        y = x.right
        x.right = y.left # Because y is the right child of x, so the left child of y will be greater than x
        # If left child of y is not None, we set its parent as x
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        # If x.parent is None, it means that x used to be the root
        # In this case, we set y as the new root        
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left: # x is the left child, we set y the left child of its parent
            x.parent.left = y
        else: # x is the right child
            x.parent.right = y
        # Then, set y's parent as x's parent
        
        y.left = x.left
        x.parent = y

    def right_rotate(self, x): # ! 4 nodes will be changed: x, x.left, x.left.right, x.parent
        y = x.left 
        x.left = y.right # y < x, so the right child of y will also be less than x
        # If right child of y is not None, we set its parent as x
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent  
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    
    def fix_inserted_node(self, z):
        #! There are total 6 cases, each 3 of them is opposite the other
        while z.parent.color == red:
            # Group case 1, z.parent is the left child
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right # Uncle of z
                if y.color == red: # Case 1
                    z.parent.color = black
                    z.parent.parent.color = red
                    y.color = black
                    # We just fix the violation for z, but there maybe violation for z.parent.parent
                    # So we need to check it again
                    z = z.parent.parent 
                else: # Case 2 or case 3, uncle of z is black
                    # Case 2: z is the right child
                    if z == z.parent.right:
                        z = z.parent
                        # Turn case 2 to case 3
                        self.left_rotate(z)
                    # Case 3:
                    z.parent.color = black
                    z.parent.parent.color = red
                    self.right_rotate(z.parent.parent)
            else: # z parent is the right child
                y = z.parent.parent.right                   
                if y.color == red:
                    z.parent.color = black
                    y.color = black
                    z.parent.parent.color = red
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = black
                    z.parent.parent.color = red
                    self.left_rotate(z.parent.parent)
        self.root.color = black

    def insert(self, z):
        y = self.NIL #variable for the parent of the added node
        temp = self.root

        while temp != self.NIL:
            y = temp
            if z.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        z.parent = y

        if y == self.NIL: #newly added node is root
            self.root = z

        elif z.data < y.data: #data of child is less than its parent, left child
            y.left = z
        else:
            y.right = z
            print('z', z.data)

        z.right = self.NIL
        z.left = self.NIL

        self.fix_inserted_node(z)

    def inorder(self, n):
        if n != self.NIL:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)


if __name__=='__main__':
    t = RedBlackBSTree()

    a = TreeNode(10)
    b = TreeNode(20)
    c = TreeNode(30)
    d = TreeNode(100)
    e = TreeNode(90)
    f = TreeNode(40)
    g = TreeNode(50)
    h = TreeNode(60)
    i = TreeNode(70)
    j = TreeNode(80)
    k = TreeNode(150)
    l = TreeNode(110)
    m = TreeNode(120)

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

    t.inorder(t.root)