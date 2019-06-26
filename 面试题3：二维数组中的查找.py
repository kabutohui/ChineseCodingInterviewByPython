# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
在一个二维数组中，每一行都按照从左到右递增的顺序排列，每一列按照从上到下的顺序排列。完成一个函数，使得输入一个二维数组和一个整数，判断数组中是否有该整数。

【解题思路】：
每次从左下角或者右上角的数字开始进行比较（书中是从右上角开始）。这里我们选取左下角的数开始比较：
1. 如果左下角的数等于查找数， 则返回True；
2. 如果左下角的数大于查找数， 则比较同一列中的上一个数字；
3. 如果左下角的数小于查找数， 则比较同一行中的右边一位的数字；
'''

def Find(grid, number) -> bool:
    if not grid:
        return False
    row, col = len(grid), len(grid[0])
    cur_i, cur_j = row - 1, 0

    while cur_i >= 0 and cur_j < col:
        if grid[cur_i][cur_j] == number:
            return True
        elif grid[cur_i][cur_j] < number:
            cur_j += 1
        else:
            cur_i -= 1

    return False

grid = [[1, 2, 8, 9],
       [2, 4, 9, 12],
       [4, 7, 10, 13],
       [6, 8, 11, 15]]

grid1 = []

number = 9

Find(grid1, number)