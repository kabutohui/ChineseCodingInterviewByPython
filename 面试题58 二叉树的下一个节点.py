# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
给定一个二叉树和其中的一个结点，如何找出中序遍历的顺序的下一个节点。结点除了有两个分别指向左右子节点以外的指针外，还有一个指向父节点的指针。
【解题思路】：

如果结点有右子树，那么下一个节点就是它右子树中最左子节点；
如果节点没有右子树，如果他是父节点的左子节点，那么下一个节点就是父节点；
如果没有右子树，且为父节点的右子节点，则沿着指向父节点的指针一直向上遍历，直到找到一个是他父节点的左子节点的节点就是下一个节点。
'''


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def getNextNode(node):
    if not node:
        return None

    pNext = None

    # if the node has a right child
    if node.right != None:
        right = node.right
        while right.left:
            right = right.left
        pNext = right

    # if the node has a parent but don't have a right child
    elif node.parent != None:
        current = node
        parent = node.parent
        # find a parent and the parent is the left child of another node
        while parent != None and (current == parent.right):
            current = parent
            parent = parent.parent

        pNext = parent

    return pNext


# test
def createTestSamples():
    '''
            A
          /   \
         B     C
       /      / \
       D     E  F
    '''
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    E = TreeNode("E")
    F = TreeNode("F")

    A.left = B;
    A.right = C;
    B.left = D;
    B.parent = A;
    C.left = E;
    C.right = F;
    C.parent = A;
    D.parent = B;
    E.parent = C;
    F.parent = C;

    return A, B, C, D, E, F


A, B, C, D, E, F = createTestSamples()
# in-order traversal： D->B->A->E->C->F
Anext = getNextNode(A)
Bnext = getNextNode(B)
Cnext = getNextNode(C)
Dnext = getNextNode(D)
Enext = getNextNode(E)
Fnext = getNextNode(F)
print("A next:", Anext.val)
print("B next:", Bnext.val)
print("C next:", Cnext.val)
print("D next:", Dnext.val)
print("E next:", Enext.val)
print("F next:", Fnext)