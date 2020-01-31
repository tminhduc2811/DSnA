"""
! Tree is a non-linear data structure.
* Root → The topmost node of the hierarchy is called the root of the tree.
* Child → Nodes next in the hierarchy are the children of the previous node.
* Parent → The node just previous to the current node is the parent of the current node.
* Siblings → Nodes with the same parent are called siblings.
* Ancestors → Nodes which are higher in the hierarchy are ancestors of a given node.
* Descendents → Nodes which are lower in the hierarchy are descendants of a given node.
* Internal Nodes → Nodes with at least one child are internal nodes.
* External Nodes/Leaves → Nodes which don't have any child are called leaves of a tree.
* Edge → The link between two nodes is called an edge.
* Level → The root of a tree is at level 0 and the nodes whose parent is root are at level 1 and so on.
* Height → The height of a node is the number of nodes (excluding the node) on the longest path from the node to a leaf.
* Height of Tree → Height of a tree is the height of its root.
* Depth → The depth of a node is the number of nodes (excluding the node) on the path from the root to the node.
* Node Degree → It is the maximum number of children a node has.
* Tree Degree → Tree degree is the maximum of the node degrees. So, the tree degree in the above picture is 3.
! Properties of a Tree
* The numbers of nodes in a tree must be a finite and nonempty set.

* There must exist a path to every node of a tree i.e., every node must be connected to some other node.

* There must not be any cycles in the tree. It means that the number of edges is one less than the number of nodes.
! Binary Tree
* Full Binary Tree → A binary tree in which every node has 2 children except the leaves is known as a full binary tree.
* Complete Binary Tree → A binary tree which is completely filled with a possible exception at the bottom level 
* i.e., the last level may not be completely filled and the bottom level is filled from left to right.
* Perfect Binary Tree → In a perfect binary tree, each leaf is at the same level and all the interior nodes have two children.
* parent node i will have left children 2i, and right children 2i + 1
* Maximum number of nodes for all alternative binary trees of the same height and it will be 2^(h+1) - 1

! Binary Tree Traversal
* There are 3 types of traversing the binary tree:
+ Preorder: we first visit the root of a tree, then its left subtree and after visiting the left subtree, the right subtree
+ Postorder: we first visit the left subtree, then the right subtree and at last, the root.
+ Inorder: we first visit the left subtree, then the root and lastly, the right subtree.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self, n):
        self.root = n


def preorder(n):
    if n!= None: # Check if the node is none
        print(' ' + n.data + ' ')
        preorder(n.left)
        preorder(n.right)

def postorder(n):
    if n != None:
        postorder(n.left)
        postorder(n.right)
        print(' ' + n.data + ' ')

def inorder(n):
    if n != None:
        inorder(n.left)
        print(' ' + n.data + ' ')
        inorder(n.right)

if __name__=='__main__':

    """            
    *               D
    *              / \
    *             /   \
    *            /     \
    *           A       F
    *          / \     / \
    *         /   \   /   \
    *        E     B R     T
    *       / \     /     / \
    *      G   Q   V     J   L
    """

    d = TreeNode('D')
    a = TreeNode('A')
    f = TreeNode('F')
    e = TreeNode('E')
    b = TreeNode('B')
    r = TreeNode('R')
    t1 = TreeNode('T')
    g = TreeNode('G')
    q = TreeNode('Q')
    v = TreeNode('V')
    j = TreeNode('J')
    l = TreeNode('L')

    t = Tree(d)

    t.root.right = f
    t.root.left = a
    a.right = b
    a.left = e

    f.right = t1
    f.left = r

    e.right = q
    e.left = g

    r.left = v

    t1.right = l
    t1.left = j

    print('Pre-order:\n')
    preorder(t.root)

    print('Post-order:\n')
    postorder(t.root)

    print('In-order:\n')
    inorder(t.root)