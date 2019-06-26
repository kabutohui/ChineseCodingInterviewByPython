# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个链表，输出该链表中倒数第k个节点。

【解题思路】：

使用双指针，一个先跑到第k个节点，然后第二个指针从头开始与第一个指针同时遍历，直到第一个指针指向空，此时第二个指针就指向倒数第k个节点；
使用递归的回溯法。
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


def findKthToTail(head: ListNode, k: int):
    if not head or k == 0:
        return
    pAhead, pBehind = head, None
    for i in range(k - 1):
        if pAhead.next != None:
            pAhead = pAhead.next
        else:
            return None

    pBehind = head
    while pAhead.next:
        pAhead = pAhead.next
        pBehind = pBehind.next

    print(pBehind.val)


def findKthToTail_Recursive(head, k):
    if not head or k == 0:
        return

    def recursive(head, k):
        if head == None:
            return 0

        i = recursive(head.next, k) + 1

        if i == k:
            print(head.val)

        return i

    recursive(head, k)


# test
head = createLinkList([1, 2, 3, 4, 5, 6])
print("findKthToTail", end=": ")
findKthToTail(head, 2)
print("findKthToTail_Recursive", end=": ")
findKthToTail_Recursive(head, 2)