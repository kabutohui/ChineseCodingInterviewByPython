# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个链表的头节点，从尾到头打印每个节点的值。

【解题思路】：
1. 栈： 每读出一个结点的值，压入栈中，最后出栈得到结果；
2. 递归： 每次先答应下一个节点的值再打印自身节点。
'''

# data structure
class LinkNode():
    def __init__(self, val):
        self.val = val
        self.next = None


# Create the Linklist
def createLink(l: list) -> LinkNode:
    if not l:
        return
    p = head = LinkNode(l[0])

    for i in l[1:]:
        p.next = LinkNode(i)
        p = p.next

    return head


def reversePrintLinkByStack(head):
    if not head:
        return
    stack = []
    while head:
        stack.append(head.val)
        head = head.next

    for i in stack[::-1]:
        print(i, end=" ")
    print()


def reversePrintLinkByRecursive(head):
    if head:
        if head.next:
            reversePrintLinkByRecursive(head.next)
        print(head.val, end=" ")


# print linklist
def printLink(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


a = [1, 2, 3, 4, 5]
head = createLink(a)
reversePrintLinkByStack(head)
reversePrintLinkByRecursive(head)

