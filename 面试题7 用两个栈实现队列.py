# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
用两个栈实现一个队列，实现这个队列的删除头部deleteHead和插入尾部appendTail的功能。

【解题思路】：
构造两个栈：stack1， stack2：
1. 从队列中删除一个头节点： 先将数据压入到stack1中， 要删除头节点的时候，将stack1中的元素出栈再压入到stack2中，这时stack2栈顶的元素就是头节点；
2. 插入一个为尾节点：直接将数据压入到stack1中。
'''


class myQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, val):
        self.stack1.append(val)
        print("The %d is added to tail of the queue" % val)

    def deleteHead(self):
        if self.stack2:
            print("The head is deleted from the queue, the head value is:", self.stack2.pop(-1))
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
            if not self.stack2:
                print("The queue is empty!")
                return
            print("The head is deleted from the queue, the head value is:", self.stack2.pop(-1))


# test
q = myQueue()
# delete head from an empty queue
print("# delete head from an empty queue")
q.deleteHead()
# add [1,2,3] to the queue, and then delete the head
print("# add [1,2,3] to the queue, and then delete the head")
for i in [1, 2, 3]:
    q.appendTail(i)
q.deleteHead()

# add [4, 5] to the queue, and the delete the head twice
print("# add [4, 5] to the queue, and the delete the head twice")
for i in [4, 5]:
    q.appendTail(i)
for i in range(2):
    q.deleteHead()

# delete the head 3 times
print("# delete the head 3 times")
for i in range(3):
    q.deleteHead()