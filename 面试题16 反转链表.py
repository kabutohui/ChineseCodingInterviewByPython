# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

【解题思路】：

定义三个指针，一个指向当前，一个指向上一个节点，一个指向下一个节点；
每次将当前节点的next指向上一个节点，并保存下一个节点；
直到输出最后一个节点作为反转链表的头节点。
'''


# define the linklist
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


# create a linklist
def createLinkList(li: list) -> ListNode:
    if not li:
        return
    p = head = ListNode(li[0])

    for i in li[1:]:
        p.next = ListNode(i)
        p = p.next

    return head


# print linklist
def printLinkList(head: ListNode):
    if not head:
        print("This is an empty linklist!")
        return
    while head:
        print(head.val, end="->")
        head = head.next
    print(None)


# reverse the linklist
def reverseLinkList(head: ListNode) -> ListNode:
    pReverseHead = None
    pNode = head
    pPrev = None
    while pNode:
        pNext = pNode.next
        if not pNext:
            pReverseHead = pNode
        pNode.next = pPrev
        pPrev = pNode
        pNode = pNext
    return pReverseHead


# test
# 1. create link list
head = createLinkList([1, 2, 3, 4, 5])
# 2. reverse the link list
reverse = reverseLinkList(head)
# 3. print the link list
printLinkList(reverse)