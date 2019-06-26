# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树，并返回重建后二叉树的根节点。
假设两个遍历的结果中没有重复的数字。

【解题思路】：
1. 从前序遍历中找到第一个结果作为根节点；
2. 在中序遍历中找到这个值，则这个值左边的值是左子节点；右边则是右子节点；
3. 利用递归，采用同样的方法重构二叉树。
'''


# Define functions for binary tree
class treeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# preOrder function
def preOrder(root):
    if not root:
        return
    print(root.val, end="->")
    preOrder(root.left)
    preOrder(root.right)


# inOrder function
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val, end="->")
    inOrder(root.right)


# Construct the binary tree
def constructBinaryTree(preOrder: list, inOrder: list) -> treeNode:
    if not preOrder or not inOrder or (len(preOrder) != len(inOrder)):
        return

    def construct(preOrder, inOrder):
        if not preOrder:
            return None

        # build root node
        root = treeNode(preOrder[0])

        # find the root node in the inOrder
        for i in range(len(inOrder)):
            if inOrder[i] == root.val:
                break

        # build left tree
        root.left = construct(preOrder[1:len(inOrder[:i]) + 1], inOrder[:i])
        # build right tree
        root.right = construct(preOrder[len(inOrder[:i]) + 1:], inOrder[i + 1:])

        return root

    return construct(preOrder, inOrder)


#  test
pre = [1, 2, 4, 7, 3, 5, 6, 8]
ino = [4, 7, 2, 1, 5, 3, 8, 6]
root = constructBinaryTree(pre, ino)
print("PreOrder:")
preOrder(root)
print("None\nInOrder:")
inOrder(root)
print("None")