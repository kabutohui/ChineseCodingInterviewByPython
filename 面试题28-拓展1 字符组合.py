# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
如果不是求字符的排列而是求字符的所有组合。即"abc"的所有组合为：a, b, c, ab, ac, bc, abc。

【解题思路】：
对于n个字符求长度为m（m<=n）的组合时，也可以先将字符串分成两个部分：第一个字符和所有字符：

如果组合中不包含第一个字符，就在剩余的n-1个字符中选取m个字符；
如果组合中包含第一个都反映，则在剩余的字符中选取m-1个字符。
'''


def Combine(strings: str):
    if not strings:
        return

    def findAll(strings, m, index, temp):
        if m == 0:
            print(temp, end=" ")
        else:
            for i in range(index, len(strings) - m + 1):
                a = temp.copy()
                a.append(strings[i])
                findAll(strings, m - 1, i + 1, a)

    for i in range(1, len(strings) + 1):
        findAll(list(strings), i, 0, [])


Combine("abc")