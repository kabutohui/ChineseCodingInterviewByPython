# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入两个递增的排序链表，合并这两个链表使得新链表中的节点仍然是递增的。

【解题思路】：
使用递归的思想：

先判断两个头节点，其值小的作为头节点；
再判断头节点的下一个节点与前一个链表头节点的大小。
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


def mergeTwoSortedLinkList(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1

    pMergeHead = None

    if head1.val < head2.val:
        pMergeHead = head1
        pMergeHead.next = mergeTwoSortedLinkList(head1.next, head2)
    else:
        pMergeHead = head2
        pMergeHead.next = mergeTwoSortedLinkList(head1, head2.next)

    return pMergeHead


# test
# 1. create two linklist
head1 = createLinkList([1, 3, 5, 7])
head2 = createLinkList([2, 4, 6, 8])
# 2. merge
mergeHead = mergeTwoSortedLinkList(head1, head2)
# 3. print merge linklist
printLinkList(mergeHead)