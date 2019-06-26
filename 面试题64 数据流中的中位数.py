# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
如何得到一个数据流中的中位数？如果数据个数为奇数，那么中位数就是所有数值排序后的中间值；如果数据的个数为偶数，那么中位数就是所有数值排序后中间两个数的平均值。

【解题思路】：

排序的数组【Done】
排序的链表
二叉搜索树
AVL树
最大堆和最小堆
'''


def getMedian(dataStream):
    res = []
    count = 0
    for i in dataStream:
        count += 1
        res.append(i)
        res.sort()

        if count % 2 == 0:
            median = (res[count // 2] + res[count // 2 - 1]) / 2
        else:
            median = res[count // 2]

        print("count=", count, "median=", median)


# test
dataStream = [2, 1, 3, 1, 4, 6, 7, 3, 1, 5, 3]
getMedian(dataStream)