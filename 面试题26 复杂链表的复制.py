# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复制一个复杂链表。在链表中，每个结点除了有一个m_pNext指针指向下一个节点外，还有一个m_pSibling指向链表中的任意节点或NULL。

【解题思路】：

根据原始链表中的每个节点N创建对应的节点N’，并链接在N的后面；
设置N’的m_pSibling；（假设N指向S，那么N’也要指向S’，而S’就在S的后面）；
将这个长链表拆分成两个链表：把奇数位置上的节点链接起来就是原始链表，把偶数位上的节点连接起来就是复制后的链表；
'''


# define the ComplexListNode
class ComplexListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.sibling = None


# create a complexlink
def createComplexLinkList():
    A = ComplexListNode("A")
    B = ComplexListNode("B")
    C = ComplexListNode("C")
    D = ComplexListNode("D")
    E = ComplexListNode("E")
    A.next = B;
    B.next = C;
    C.next = D;
    D.next = E
    A.sibling = C;
    B.sibling = E;
    D.sibling = B

    return A


# print complexLinkList
def printComplexLinkList(head):
    p = head
    while p:
        if p.sibling:
            print("{0}[{1}]".format(p.val, p.sibling.val), end="->")
        else:
            print("{0}".format(p.val), end="->")
        p = p.next
    print("End")


# Clone ComplexLinkList
def cloneNode(head):
    p = head
    while p:
        clone = ComplexListNode(0)
        clone.val = p.val + "'"
        clone.next = p.next

        p.next = clone
        p = clone.next

    return head


def connectSiblingNodes(head):
    p = head
    while p:
        clone = p.next
        if p.sibling:
            clone.sibling = p.sibling.next
        p = clone.next

    return head


def reconnectNodes(head):
    if not head:
        return
    p = head
    cloneHead = cloneNode = p.next
    p.next = cloneNode.next
    p = p.next

    while p:
        cloneNode.next = p.next
        cloneNode = cloneNode.next
        p.next = cloneNode.next
        p = p.next

    return cloneHead


def clone(head):
    return reconnectNodes(connectSiblingNodes(cloneNode(head)))


# test
head = createComplexLinkList()
printComplexLinkList(clone(head))
# head = cloneNode(head)
# printComplexLinkList(head)
# head = connectSiblingNodes(head)
# printComplexLinkList(head)
# head = reconnectNodes(head)
# printComplexLinkList(head)