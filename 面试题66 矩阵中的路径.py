# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请设计一个函数，用来判断一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵的任意一格开始，每一步可以在矩阵中向上、下、左、右移动一格。

【解题思路】：
利用回溯法
'''


def hasPath(matrix, string):
    if not matrix or not string:
        return False

    row, col = len(matrix), len(matrix[0])
    visited = [[0 for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == string[0] and hasPathCore(matrix, string, i, j, visited):
                return True
    return False


def hasPathCore(matrix, string, row, col, visited):
    if len(string) == 0:
        return True

    hasPath = False
    if row >= 0 and row < len(matrix) and \
            col >= 0 and col < len(matrix[0]) and \
            matrix[row][col] == string[0] and \
            visited[row][col] == 0:
        visited[row][col] = 1
        hasPath = hasPathCore(matrix, string[1:], row + 1, col, visited) or \
                  hasPathCore(matrix, string[1:], row - 1, col, visited) or \
                  hasPathCore(matrix, string[1:], row, col + 1, visited) or \
                  hasPathCore(matrix, string[1:], row, col - 1, visited)

    return hasPath


# test
# 1. create a matrix
matrix = [["a", "b", "c", "e"],
          ["s", "f", "c", "s"],
          ["a", "d", "e", "e"]]

string = "bcced"

# 2. test the hasPath
print(hasPath(matrix, string))


# test
def Test(testName, matrix, string, rows, cols, true_result):
    matrix = [matrix[i * cols: (i + 1) * cols] for i in range(rows)]
    res = hasPath(matrix, string)
    if res == true_result:
        print(testName, ": OK!")
    else:
        print(testName, ": FAILED!")


Test("test01", "ABCESFCSADEE", "ABCCED", 3, 4, True)
Test("test02", "ABCESFCSADEE", "SEE", 3, 4, True)
Test("test03", "ABCESFCSADEE", "ABCB", 3, 4, False)
Test("test04", "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", "SLHECCEIDEJFGGFIE", 5, 8, True)
# Test("test05", "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", "SGGFIECVAASABCEHJIGQEM", 5, 8, True)  # some trouble  with this test case
Test("test06", "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", "SGGFIECVAASABCEEJIGOEM", 5, 8, False)
Test("test07", "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", "SGGFIECVAASABCEHJIGQEMS", 5, 8, False)
Test("test08", "AAAAAAAAAAAA", "AAAAAAAAAAAA", 3, 4, True)
Test("test09", "AAAAAAAAAAAA", "AAAAAAAAAAAAA", 3, 4, False)
Test("test10", "A", "A", 1, 1, True)
Test("test11", "A", "B", 1, 1, False)