# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
树种两个节点的最低公共祖先是一组题：
题1： 如果输入的是搜索二叉树，找到指定两个节点的最低公共祖先；
题2： 如果输入的是一颗普通的树，但是每个节点都有指向父节点的指针；
题3： 如果输入的是一颗普通的树，且没有指向父节点的指针；

【解题思路】：
题1：
搜索二叉树的左子树的节点比父节点小，右子树的节点比父节点大。这时只需要从根节点出发，和两个节点进行比较，当前节点比两个节点值都大，那么最低公共祖先在左子树上，否则在右子树上。这样找的第一个在两者之间的节点就是最低公共祖先。

题2：
如果输入的是一颗普通的树，但是每个节点都有指向父节点的指针。可以将题目转化为链表的第一个公共节点。每个节点都有指向父节点的指针，那么形成的链表的尾指针都是树的公共节点。那么最低公共祖先就是两个链表的第一个公共节点。

题3：
如果输入的是一颗普通的树，且没有指向父节点的指针。可以利用额外的内存。建立两个链表用于存储从根节点到目标节点的路径，然后找到这两条路径的最后的公共节点就是最低公共祖先。
'''


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class LisNode():
    def __init__(self, val):
        self.val = val
        self.next = None


# Question 1: if the tree is a BST
def findLastCommonParent_BST(root, node1, node2):
    if not root or not node1 or not node2:
        return
    val1, val2 = node1.val, node2.val

    while True:
        if root.val > max(val1, val2):
            root = root.left
        elif root.val < min(val1, val2):
            root = root.right
        else:
            return root


# Quesetion 2: a normal tree with a parent pointer
def findLastCommonParent_parentPtr(root, node1, node2):
    if not root or not node1 or not node2:
        return
    p1, p2 = node1, node2
    len1, len2 = 0, 0

    # calculate the length from node to root
    while p1:
        len1 += 1
        p1 = p1.parent
    while p2:
        len2 += 1
        p2 = p2.parent

    # the two link go the same length
    if len1 > len2:
        for i in range(len1 - len2):
            node1 = node1.parent
    else:
        for i in range(len2 - len1):
            node2 = node2.parent

    # find the first common node
    while node1 != node2:
        node1 = node1.parent
        node2 = node2.parent

    return node1


# Question 3: a normal tree without parent pointer
def findLastCommonParent_WithoutParentPtr(root, node1, node2):
    if not root or not node1 or not node2:
        return

    def findPath(root, node, path):
        if not root:
            return False
        if root == node:
            return True

        path.append(root)

        found = False
        if root.left:
            found = findPath(root.left, node, path)
        if not found and root.right:
            found = findPath(root.right, node, path)
        if not found:
            path.pop(-1)

        return found

    # find the path from root to node1 and node2
    path1, path2 = [], []
    findPath(root, node1, path1)
    findPath(root, node2, path2)

    longPath, shortPath = path1, path2
    if len(path1) < len(path2):
        longPath = path2
        shortPath = path1

    found = False
    for i in range(len(shortPath)):
        if longPath[i] != shortPath[i]:
            found = True
            break

    return shortPath[i - 1] if found else shortPath[i]


# test
# Create  a test sample
def createTestSample():
    '''
         A(5)
        /    \
      B(3)    C(7)
       / \     /  \
    D(2) E(4) F(6) G(8)
      /
    H(1)
    '''
    A = TreeNode(5)
    B = TreeNode(3)
    C = TreeNode(7)
    D = TreeNode(2)
    E = TreeNode(4)
    F = TreeNode(6)
    G = TreeNode(8)
    H = TreeNode(1)
    A.left = B;
    A.right = C;
    B.left = D;
    B.right = E;
    B.parent = A;
    C.left = F;
    C.right = G;
    C.parent = A;
    D.left = H;
    D.parent = B;
    H.parent = D;
    E.parent = B;
    F.parent = C;
    G.parent = C;

    return A, H, E


root, node1, node2 = createTestSample()
# 1. test for the findLastCommonParent_BST
commonNode = findLastCommonParent_BST(root, node1, node2)
print("findLastCommonParent_BST:", commonNode.val)
# 2. test for a common tree with parent pointer
commonNode = findLastCommonParent_parentPtr(root, node1, node2)
print("findLastCommonParent_parentPtr:", commonNode.val)
# 3. test for a common tree without parent pointer
commonNode = findLastCommonParent_WithoutParentPtr(root, node1, node2)
print("findLastCommonParent_WithoutParentPtr:", commonNode.val)