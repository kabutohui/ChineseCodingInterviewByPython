# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
求1+2+3+...+n。要求不能用乘法除法、for、while、if-else、switch-case等关键字以及条件判断语句A?B:C。

【解题思路】：
【C++】

使用构造函数，创建n个构造函数的实例；
利用虚函数；
利用函数指针；
利用模板类型求解。
'''

# 使用了函数指针，当n减小为0的时候，return 0，其余都是直接相加
def solution_teminator(n):
    return 0

def sum_solution(n):
    d={False: solution_teminator, True: sum_solution}
    return n + d[not not n](n-1)

sum_solution(100)