# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
在一个排序的链表中，如何删除重复的节点？

【解题思路】：
设置两个指针，一个指向当前，一个指向前一个节点，如果当前的节点与下一个节点的值相等，那么这两个节点应该被删除。
'''


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteDuplication(head):
    if not head:
        return

    pPreNode, pNode = None, head

    while pNode != None:
        pNext = pNode.next
        needDelete = False

        if pNext != None and (pNext.val == pNode.val):
            needDelete = True

        if not needDelete:
            pPreNode = pNode
            pNode = pNode.next
        else:
            value = pNode.val
            pToBeDel = pNode
            while pToBeDel != None and (pToBeDel.val == value):
                pNext = pToBeDel.next
                pToBeDel = pNext

            if pPreNode == None:
                head = pNext
            else:
                pPreNode.next = pNext
            pNode = pNext

    return head


# test
def createLinkList(nums):
    if not nums:
        return None

    p = head = ListNode(nums[0])

    for i in nums[1:]:
        p.next = ListNode(i)
        p = p.next

    return head


def printLink(head):
    if not head:
        return
    while head:
        print(head.val, end="->")
        head = head.next
    print("End")


# before
head = createLinkList([1, 2, 3, 3, 4, 4, 5])
printLink(head)
# after
head = createLinkList([1, 1, 2, 3, 3, 3, 4, 4, 5, 5])
head = deleteDuplication(head)
printLink(head)
