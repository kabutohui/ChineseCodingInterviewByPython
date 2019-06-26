# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
地上有一个m行n列的方格。一个机器人从坐标（0，0）的格子开始移动，它每一次可以向上、下、左、右移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
如当k=18时，可以进入方格（35， 37），因为3+5+3+7=18=k；但是不能进入方格（35， 38），因为3+5+3+8=19>k。
请问机器人可以到达多少个格子？

【解题思路】：
回溯法
'''


def movingCount(rows, cols, k):
    if rows <= 0 or cols <= 0:
        return 0

    visited = [[0 for i in range(cols)] for j in range(rows)]

    count = movingCountCore(rows, cols, k, visited, 0, 0)

    return count


def movingCountCore(rows, cols, k, visited, row, col):
    count = 0
    if check(rows, cols, k, visited, row, col):
        visited[row][col] = 1
        count = 1 + movingCountCore(rows, cols, k, visited, row - 1, col) + \
                movingCountCore(rows, cols, k, visited, row + 1, col) + \
                movingCountCore(rows, cols, k, visited, row, col - 1) + \
                movingCountCore(rows, cols, k, visited, row, col + 1)
    return count


def check(rows, cols, k, visited, row, col):
    if row >= 0 and row < rows and \
            col >= 0 and col < cols and \
            getSum(row) + getSum(col) <= k and \
            visited[row][col] == 0:
        return True
    return False


def getSum(num):
    Sum = 0
    while num > 0:
        Sum += (num % 10)
        num = num // 10

    return Sum


# test
def test(testName, k, rows, cols, expected):
    count = movingCount(rows, cols, k)
    if count == expected:
        print(testName, " OK!")
    else:
        print(testName, " FAILED!")


test("Test1", 5, 10, 10, 21)
test("Test2", 15, 20, 20, 359)
test("Test3", 10, 1, 100, 29)
test("Test4", 10, 1, 10, 10)
test("Test5", 15, 100, 1, 79)
test("Test6", 15, 10, 1, 10)
test("Test7", 15, 1, 1, 1)
test("Test8", -10, 10, 10, 0)