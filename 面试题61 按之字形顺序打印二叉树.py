# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请实现一个函数，按照之字形顺序打印二叉树，即第一行从左到右，第二行从右到左以此类推。

【解题思路】：
与60题类似，这个题可以使用双栈的解题思路，当前层出栈，并将下一层的节点压入另一个栈。需要注意的是：
一个栈用于存奇数层，所以是先压入左节点，再压入右节点；
另一个栈用于村偶数层，要先压入右节点，再压如左节点。
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


def printTreeAsZhi(root):
    if not root:
        return None

    stack = [[root], []]
    current, next = 0, 1

    layerFlag = True

    while stack[0] or stack[1]:
        node = stack[current].pop(-1)
        print(node.val, end=" ")

        if current == 0:
            if node.left:
                stack[next].append(node.left)
            if node.right:
                stack[next].append(node.right)
        else:
            if node.right:
                stack[next].append(node.right)
            if node.left:
                stack[next].append(node.left)

        if len(stack[current]) == 0:
            print()
            current = 1 - current
            next = 1 - next


# test
# 1. create a tree
root = createTree([i for i in range(1, 16)], 0)
# 2. print node by layer
printTreeAsZhi(root)