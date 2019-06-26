# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
要求输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求： 不能创建任何新的节点，只能调整树中节点指针的指向

【解题思路】：
对于二叉搜索树使用中序遍历就能得到排序的结果；
利用递归的思想：
当遍历到根节点的时候，将他和左子树的最大节点链接起来；和右子树的最小节点链接起来。

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


# print doubly LinkList
def printDoublyLinkList(head):
    if not head:
        return "Empty doubly Linklist!"

    print("left-to-right:")
    while head.left:
        print(head.val, end="->")
        head = head.left
    print("End\nrigth-to-left:")
    while head.right:
        print(head.val, end="->")
        head = head.right
    print("End")


def convertBST2BoublyLinklist(root):
    if not root:
        return None, None

    l1, r1 = convertBST2BoublyLinklist(root.left)
    left_most = l1 if l1 else root
    l2, r2 = convertBST2BoublyLinklist(root.right)
    right_most = r2 if r2 else root

    root.left = r1
    if r1:
        r1.right = root
    root.right = l2
    if l2:
        l2.left = root

    return left_most, right_most


# test
# 1. create a BST
root = createTree([10, 6, 14, 4, 8, 12, 16], 0)
# 2. convert to  doubly linklist
left_most, right_most = convertBST2BoublyLinklist(root)
# 3. print
printDoublyLinkList(right_most)
