# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
0，1，2，3，...，n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈中删除第m个数字。求圆圈中剩下的最后一个数字。
例如由0，1，2，3，4这5个数字组成一个环，从0开始每次删除第3个数字，则删除的前4个数字是2， 0， 4， 1，最后剩下的一个数字是3

【解题思路】：
这是有名的约瑟夫环问题

用环形链表模拟圆圈；
分析被删除数据的规律:
a. 首先定义一个函数f(m,n)，表示每次在n个数字0~n-1中每次删除第m个数字最后剩下的数字，删除的数字为k=(m-1)%n;
b. 下次应该从序列k+1, k+2, ... , n-1, 0, 1, ..., k-1中删除第m个数字，起映射关系可以写为： P(x)=(x−k−1)%n 。如果映射前的数是x，那么映射后的数就是(x-k-1)%n，其逆映射为 P−1(x)=(x+K+1)%n ;
c.  f(n,m)=f′(n−1,m)=P−1[f(n−1,m)]=[f(n−1,m)+k+1]%n=[f(n−1,m)+m]%n 
d. 递推公式可以写为：
f(n,m)={0,       n=1[f(n−1,m)+m]%n, n>1
'''


# Method 1： use circle linklist（list instead）
def lastRemaining(n, m):
    if n < 1 or m < 1:
        return

    nums = [i for i in range(n)]

    index = 0
    while len(nums) > 1:
        index = (index + m - 1) % len(nums)
        nums.remove(nums[index])

    return nums[0]


# Method 2
def lastRemaining2(n, m):
    if n < 1 or m < 1:
        return

    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i

    return last


# test
import time

start = time.time()
print("Method 1:", lastRemaining(40000, 997), end="  time=")
end = time.time()
print(end - start)

start = time.time()
print("Method 2:", lastRemaining2(40000, 997), end="  time=")
end = time.time()
print(end - start)