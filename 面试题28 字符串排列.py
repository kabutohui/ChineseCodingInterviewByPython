# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个字符串，打印出该字符串中所有字符的全排列，例如输入abc，输出abc, acb, bac, bca, cab, cba。

【解题思路】：

把字符串分成两个部分，一部分是字符串的第一个字符，另一个是字符串后的所有字符。
拿第一个字符与后面的字符逐个交换。
'''


def Permutation(strings: str):
    if not str:
        return

    def findAll(strings, index):
        if index >= len(strings):
            print("".join(strings), end=" ")
        else:
            for i in range(index, len(strings)):
                temp = strings[i]
                strings[i] = strings[index]
                strings[index] = temp

                findAll(strings, index + 1)

                # recovery
                temp = strings[i]
                strings[i] = strings[index]
                strings[index] = temp

    findAll(list(strings), 0)


Permutation("abc")