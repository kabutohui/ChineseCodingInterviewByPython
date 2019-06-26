# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请实现一个函数用来找出字符流中第一个只出现一次的字符。
如“go”，第一个只出现一次的字符是g；
如“google”第一个只出现一次的字符是l。

【解题思路】：
在python中，利用dict进行统计，遍历两次字符串，第一次统计每个字符出现的次数，第二次找到第一个字符个数为1的字符返回。
'''


def findAppearingOnce(string):
    if not string:
        return None

    count = {}
    for i in string:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1

    for i in string:
        if count[i] == 1:
            return i


# test
findAppearingOnce("google")
