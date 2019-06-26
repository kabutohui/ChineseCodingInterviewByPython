# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入两个整数序列，第一个表示栈的压入序列，请判断第二个序列是否为改栈的弹出序列。
假设压入栈的所有数字均不相等！

【解题思路】：
利用辅助栈，模拟进栈与出栈。
'''

def isPopOrder(pushes, pops):
    if not pushes or not pops or len(pushes) != len(pops):
        return False

    push_stack = []
    while pops:
        val = pops.pop(0)
        if push_stack and push_stack[-1] == val:
            push_stack.pop(-1)
        else:
            while pushes:
                nums = pushes.pop(0)
                if nums == val:
                    break
                else:
                    push_stack.append(nums)

    if not pops and not push_stack:
        return True
    else:
        return False


# test
pops = [4, 5, 3, 2, 1]
pushes = [1, 2, 3, 4, 5]
isPopOrder(pushes, pops)
