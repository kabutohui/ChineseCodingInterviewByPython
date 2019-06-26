# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
一个链表中包含环，如何找出环的入口节点。

【解题思路】：

1. 先利用快慢指针，判断该链表中是否有环，并找到环中的一个节点；
2. 从环中的一个节点出发，找到环中节点的数量；
3. 从原链表中的头节点开始，设置两个指针，一个指针指向头节点，
另一个指针先往前移动环中节点的个数相等的步数。然后两个指针同时移动，
当两个指针相等的时候，就找了环的入口节点。
'''


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def findNodeInLoop(head):
    if not head:
        return None

    slow, fast = head, head.next

    while slow != None and fast != None:
        if fast == slow:
            return fast

        slow = slow.next
        fast = fast.next
        if fast != None:
            fast = fast.next

    return None


def findEntryNodeOfLoop(head):
    if not head:
        return None

    nodeInLoop = findNodeInLoop(head)

    if not nodeInLoop:
        return None

    nodesCountInLoop = 1
    pNode = nodeInLoop
    while pNode.next != nodeInLoop:
        pNode = pNode.next
        nodesCountInLoop += 1

    pNode1, pNode2 = head, head

    for i in range(nodesCountInLoop):
        pNode1 = pNode1.next

    while pNode1 != pNode2:
        pNode1 = pNode1.next
        pNode2 = pNode2.next

    return pNode1


# test
def createTestSample():
    A = ListNode("A")
    B = ListNode("B")
    C = ListNode("C")
    D = ListNode("D")
    E = ListNode("E")
    F = ListNode("F")
    A.next = B;
    B.next = C;
    C.next = D;
    D.next = E;
    E.next = F;
    F.next = C;

    return A


head = createTestSample()
meetnode = findEntryNodeOfLoop(head)
print(meetnode.val)