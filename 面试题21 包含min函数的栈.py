# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。在该栈中调用min、push和pop的时间复杂度都是O(1)。

【解题思路】：
使用辅助栈来保存当前状况下的最小值。
'''


class myStack():
    def __init__(self):
        self.stack = []
        self.min = []
        self.count = 0

    def pop(self):
        if self.count == 0:
            print("The stack is empty!")
        else:
            print(self.stack.pop(-1))
            self.min.pop(-1)
            self.count -= 1

    def push(self, val):
        if self.count == 0:
            self.stack.append(val)
            self.min.append(val)
        else:
            self.stack.append(val)
            self.min.append(min(self.min[-1], val))
        self.count += 1

    def minValue(self):
        if self.count == 0:
            print("The stack is empty!")
        else:
            print("The minimize value of the stack is :", self.min[-1])


# test
t = myStack()
t.pop()
t.push(1)
t.push(2)
t.push(0)
t.push(4)
t.minValue()
t.pop()
t.minValue()
t.pop()
t.minValue()
t.pop()
t.minValue()