# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
从上往下打印出二叉树的每一个节点同一层的节点按照从左到右的顺序打印。

【解题思路】：
使用队列。
'''


# define the tree
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# create a tree
def createTree(nums, index):
    if not nums:
        return None
    if index >= len(nums):
        return None

    root = TreeNode(nums[index])
    root.left = createTree(nums, 2 * index + 1)
    root.right = createTree(nums, 2 * index + 2)

    return root


def printFromTopToBottom(root):
    if not root:
        return
    queue = [root]

    while queue:
        treeNode = queue.pop(0)
        if treeNode.left:
            queue.append(treeNode.left)
        if treeNode.right:
            queue.append(treeNode.right)

        print(treeNode.val, end=" ")

    print()


# test
# 1. create a tree
root = createTree([1, 2, 3, 4, 5, 6], 0)
# print
printFromTopToBottom(root)