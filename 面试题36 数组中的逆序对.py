# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
在数组中的两个数字如果前面的一个数字大于后面的一个数字，则这两个数字组成一个逆序对。输入一个逆序对，求出这个数组中逆序对的个数。

【解题思路】：
利用归并排序的方式统计数组中的逆序对。
'''


def inversePairs(data):
    if not data:
        return
    copy = data.copy()
    return inversePairsCore(data, copy, 0, len(data) - 1)


def inversePairsCore(data, copy, start, end):
    #     print("start:", start, "end:", end, "copy:", copy)
    if start == end:
        copy[start] = data[start]
        return 0

    length = (end - start) // 2

    left = inversePairsCore(copy, data, start, start + length)
    right = inversePairsCore(copy, data, start + length + 1, end)

    # 前半段最后一个数字的下标
    i = start + length
    # 后半段最后一个数字的下标
    j = end
    indexCopy = end
    count = 0

    while i >= start and j >= (start + length + 1):
        if data[i] > data[j]:
            copy[indexCopy] = data[i]
            indexCopy -= 1;
            i -= 1;
            count += j - start - length
        else:
            copy[indexCopy] = data[j]
            indexCopy -= 1;
            j -= 1;

    while i >= start:
        copy[indexCopy] = data[i]
        indexCopy -= 1;
        i -= 1;
    while j >= start + length + 1:
        copy[indexCopy] = data[j]
        indexCopy -= 1;
        j -= 1;

    print("start:", start, "end:", end, "left:", left, "right:", right, "count:", count, "copy:", copy)
    return left + right + count


# test
# data = [1, 2, 3, 4, 7, 6, 5]
data = [7, 5, 6, 4]
inversePairs(data)