# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个矩阵，按照从外向里顺时针的顺序依次打印出每一个数字。如：
1 2 3
4 5 6
7 8 9
打印结果为： 1 2 3 6 9 8 7 4 5

【解题思路】：

按照一圈一圈的思想来进行打印，每次打印的起始位置是对角元素。
使用 columns > start2 and row > start2 来判断该元素有没有被打印。
'''


def printMatrixCircle(nums):
    if not nums:
        return
    row, col = len(nums), len(nums[0])

    start = 0
    while row > start * 2 and col > start * 2:
        printCircle(nums, start, row, col)
        start += 1
    print("End")


def printCircle(nums, start, row, col):
    endX = row - start
    endY = col - start

    # from left to right
    for i in range(start, endY):
        print(nums[start][i], end="->")

    # up to down
    if start < endX - 1:
        for i in range(start + 1, endX):
            print(nums[i][endY - 1], end="->")

    # left to right
    if start < endX - 1 and start < endY - 1:
        for i in range(endY - 1 - 1, start - 1, -1):
            print(nums[endX - 1][i], end="->")

    # down to up
    if start < endY - 1 and start < endX - 1:
        for i in range(endX - 1 - 1, start, -1):
            print(nums[i][start], end="->")


# test
nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

nums2 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]

nums3 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

nums4 = [[1, 2, 3]]

nums5 = [[1],
         [2],
         [3]]

nums6 = [[1]]

printMatrixCircle(nums)
printMatrixCircle(nums2)
printMatrixCircle(nums3)
printMatrixCircle(nums4)
printMatrixCircle(nums5)
printMatrixCircle(nums6)