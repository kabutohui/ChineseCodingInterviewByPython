# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
给定一个数组 A[0,1,...,n−1] ，请构建一个数组 B[0,1,...,n−1] ，其中B的元素 B[i]=A[0]∗A[1]∗...∗A[i−1]∗A[i+1]∗...∗A[n−1] 。不能使用除法

【解题思路】：

可以将 B[i] 拆成两个部分：
B[i]=A[0]∗A[1]∗...∗A[i−1]∗A[i+1]∗...∗A[n−1]
    =(A[0]∗A[1]∗...∗A[i−1])∗(A[i+1]∗...∗A[n−1])
    =C[i]∗D[i]
    其中：C[i]=A[0]∗A[1]∗...∗A[i−1]
          D[i]=A[i+1]∗...∗A[n−1]
          
C[i]可以自上而下的计算： C[i]=C[i−1]∗A[i−1] ，其中： C[0]=1 
D[i]可以自下而上的计算： D[i]=D[i+1]∗A[i+1] ，其中： D[n−1]=1 
'''


def multipy(A):
    if not A:
        return

    B = [0] * len(A)

    B[0] = 1
    for i in range(1, len(A)):
        # calculate C[i]
        B[i] = B[i - 1] * A[i - 1]

    temp = 1
    for i in range(len(A) - 2, -1, -1):
        temp = temp * A[i + 1]
        B[i] = B[i] * temp

    return B


# test
A = [1, 2, 3, 4, 5]
print(multipy(A))