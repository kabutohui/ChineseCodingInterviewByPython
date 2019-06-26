# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
写一个函数，要求输入n，输出斐波那契数列的的第n项。
斐波那契数列定义如下：
f(n)=0,n=01,n=1f(n−1)+f(n−2),n>1
 
f(n)=[1+5√2]n+1−5√2n1+5√2−1−5√2
 
【解题思路】：

递归
迭代
通项公式
实验证明：迭代法要比递归更加高效
'''


# use recursive method
def fibRecursive(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibRecursive(n - 1) + fibRecursive(n - 2)


# use the iterative method
def fibIterative(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1

    first, second = 0, 1

    for i in range(2, n + 1):
        first, second = second, first + second
    return second


# use the function
def fibUseFunction(n):
    return int((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5)


# test
import time

n = 35
start = time.time()
print("Recursive method:", fibRecursive(n), end=" Time consumption=")
end = time.time()
print(end - start)

start = time.time()
print("Iterative method:", fibIterative(n), end=" Time consumption=")
end = time.time()
print(end - start)

start = time.time()
print("Function method:", fibUseFunction(n), end=" Time consumption=")
end = time.time()
print(end - start)