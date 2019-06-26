# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层一行。

【解题思路】：
这就是一个简单的层次遍历，利用队列即可实现。
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


def printTree(root):
    if not root:
        return

    queue = [root]
    currentLayer, nextLayer = 1, 0

    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")

        if node.left != None:
            queue.append(node.left)
            nextLayer += 1
        if node.right != None:
            queue.append(node.right)
            nextLayer += 1

        currentLayer -= 1
        if currentLayer == 0:
            print()
            currentLayer = nextLayer
            nextLayer = 0


# test
# 1. create a tree
root = createTree([8, 6, 10, 5, 7, 9, 11], 0)
# 2. print node by layer
printTree(root)
