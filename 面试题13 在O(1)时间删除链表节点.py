# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该节点。
void deleteNode(ListNode* pListHead, ListNode* pToBeDeleted)

【解题思路】：
从三个方面来考虑：

如果待删除节点不是尾结点：将该节点的值由下一个节点的值来代替，然后指向下下个节点；
如果待删除节点是尾结点同时也是头节点，链表中只有一个节点： 将头节点置为NULL；
如果是尾巴节点，则需要遍历到尾节点前的一个节点，然后进行删除操作。
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


# Delete a node in O(1)
def deleteNode(head: ListNode, toBeDeleted: ListNode) -> ListNode:
    if not head or not toBeDeleted:
        return
    if toBeDeleted.next != None:
        toBeDeleted.val = toBeDeleted.next.val
        toBeDeleted.next = toBeDeleted.next.next
    elif head == toBeDeleted:
        head = None
    else:
        p = head
        while p.next != toBeDeleted:
            p = p.next
        p.next = None

    return head


# test
# 1. create a linklist
head = createLinkList([1, 2, 3, 4, 5])
printLinkList(head)
# 2. delete a node in the middle of linklist
toBeDeleted = head.next.next
newhead = deleteNode(head, toBeDeleted)
printLinkList(newhead)
# 3. delete a node in bottom of the linklist
toBeDeleted = head.next.next.next
newhead = deleteNode(head, toBeDeleted)
printLinkList(newhead)
# 4. test a one node linklist
head = createLinkList([1])
newhead = deleteNode(head, head)
printLinkList(newhead)