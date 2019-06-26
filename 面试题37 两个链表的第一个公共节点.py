# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入两个链表，找出他们的第一个公共节点。

【解题思路】：
方案一： 利用栈的思想，返回最后一个相同的节点；
方案二： 遍历链表得到长度，再将长链表遍历到短链表一样的长的位置，同时开始遍历，直到找到第一个相同的节点。
'''


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


# Method 1: use stack
def findFirstCommonNode_stack(head1, head2):
    if not head1 or not head2:
        return

    stack1, stack2 = [], []
    while head1:
        stack1.append(head1)
        head1 = head1.next

    while head2:
        stack2.append(head2)
        head2 = head2.next

    while stack1 and stack2:
        s1, s2 = stack1.pop(-1), stack2.pop(-1)
        if s1 == s2 and stack1[-1] != stack2[-1]:
            return s1

    return "No such Node!"


# Method 2: use length
def findFirstCommonNode_length(head1, head2):
    if not head1 or not head2:
        return
    p1, p2 = head1, head2

    # calculate the length of each linklist
    len1, len2 = 0, 0
    while p1:
        len1 += 1
        p1 = p1.next
    while p2:
        len2 += 1
        p2 = p2.next

    # go to the same length
    if len1 > len2:
        for i in range(len1 - len2):
            head1 = head1.next
    else:
        for i in range(len2 - len1):
            head2 = head.next

    while head1 and head2 and head1 != head2:
        head1 = head1.next
        head2 = head2.next

    return head1


# test
def createTestSample():
    A = ListNode("A")
    B = ListNode("B")
    C = ListNode("C")
    D = ListNode("D")
    E = ListNode("E")
    F = ListNode("F")
    G = ListNode("G")
    A.next = B;
    B.next = C;
    C.next = F;
    F.next = G;
    D.next = E;
    E.next = F;
    F.next = G;

    return A, D


head1, head2 = createTestSample()
common_stack = findFirstCommonNode_stack(head1, head2)
common_length = findFirstCommonNode_length(head1, head2)
print("Use stack:", common_stack.val)
print("Use length:", common_length.val)