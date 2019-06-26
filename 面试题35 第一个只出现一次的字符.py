# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
在字符串中找出第一个只出现一次的字符。如输入“abaccdeff”，输出“b”。

【解题思路】：
建立一个dict，用于存储字符串中各个字符出现的次数；然后再遍历一次字符串，直到找到第一个字符个数为1的字符输出。
'''


def firstNotRepeatingChar(strings):
    if not strings:
        return
    charCounter = {}
    for s in strings:
        if s not in charCounter.keys():
            charCounter[s] = 1
        else:
            charCounter[s] += 1

    for s in strings:
        if charCounter[s] == 1:
            return s

    return "No such character!"


# test
firstNotRepeatingChar("abaccdeff")