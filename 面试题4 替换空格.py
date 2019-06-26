# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】:
实现一个函数，将字符串中的每个空格替换为"%20"。

【解题思路】：
这个题如果用python做，直接替换就行。

这里采书上的做法：
1. 先统计空格的个数；
2. 设置两个指针，一个指向原字符串的末尾，一个指向新字符串的末尾；
3. 遇到空格就替换为"%20"
'''


def ReplaceBlank(s: str) -> str:
    if not s:
        return
        # 统计字符串中空格的长度
    numberOfBlank = 0
    for i in range(len(s)):
        if s[i] == " ":
            numberOfBlank += 1

    indexOfNew = len(s) + numberOfBlank * 2 - 1
    indexOfOrigin = len(s) - 1
    s = s + " " * numberOfBlank * 2
    s = list(s)
    while indexOfOrigin >= 0 and indexOfNew > indexOfOrigin:
        if s[indexOfOrigin] == " ":
            s[indexOfNew] = '0'
            indexOfNew -= 1
            s[indexOfNew] = '2'
            indexOfNew -= 1
            s[indexOfNew] = '%'
            indexOfNew -= 1
        else:
            s[indexOfNew] = s[indexOfOrigin]
            indexOfNew -= 1
        indexOfOrigin -= 1
    s = "".join(s)
    return s


def ReplaceBlankPy(s: str) -> str:
    if not s:
        return
    s = list(s)

    def replace(char):
        if char == " ":
            return "%20"
        else:
            return char

    s = list(map(replace, s))

    return "".join(s)

s = "    We are     happy "
print("ReplaceBlank:", ReplaceBlank(s))
print("ReplaceBlankPy:", ReplaceBlankPy(s))