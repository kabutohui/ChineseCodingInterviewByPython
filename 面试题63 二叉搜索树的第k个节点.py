# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】;
给定一棵二叉搜索树，请找出其中第k大的节点。

【解题思路】：
利用中序遍历的思想遍历得到的结果是排序的。
'''


# define the tree
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Deserialize a tree
def deserializeTree(seria):
    if not seria:
        return None
    number = seria.pop(0)
    if isinstance(number, int):
        root = TreeNode(number)

        root.left = deserializeTree(seria)
        root.right = deserializeTree(seria)

        return root
    else:
        return None


def findKthNode(root, k):
    if not root or k == 0:
        return None

    def kthNodeCore(root, res, k):
        if not root:
            return None

        if root.left != None:
            kthNodeCore(root.left, res, k)

        if len(res) != k:
            res.append(root.val)

        if root.right != None:
            kthNodeCore(root.right, res, k)

    res = []
    kthNodeCore(root, res, k)

    if len(res) < k:
        return "k gather than the number of tree nodes!"

    return res[-1]


# test
# 1. create a tree
root = deserializeTree([5, 3, 2, "$", "$", 4, "$", "$", 7, 6, "$", "$", 8, "$", "$"])
# 2. test find kth node
res = findKthNode(root, 3)
print("The kth node is:", res)