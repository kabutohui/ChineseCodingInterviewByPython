# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
其实现一个函数，用来判断一颗二叉树是不是对称的。

【解题思路】：

定义一个对称前序遍历：根->右->左；
然后同时进行前序遍历和对称前序遍历，每遍历一个节点就进行判断。
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


def isSymmetrical(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 == None or root2 == None:
        return False

    if root1.val != root2.val:
        return False

    return isSymmetrical(root1.left, root2.right) and isSymmetrical(root1.right, root2.left)


# test
# 1. create a symmetrical tree
root = createTree([8, 6, 6, 5, 7, 7, 5], 0)
print("symmetrical tree:", isSymmetrical(root, root))

# 2. create a non-symmetrical tree
root = createTree([8, 6, 9, 5, 7, 7, 5], 0)
print("non-symmetrical tree:", isSymmetrical(root, root))