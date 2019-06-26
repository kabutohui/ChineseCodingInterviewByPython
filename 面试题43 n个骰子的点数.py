# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能值出现的概率。

【解题思路】：
递归法： 建立一个6n-n+1的数组存储和为s的点数出现的次数存储到s-n的位置中。【时间效率低】
循环法：
'''


# Method 1
def printProbability(number):
    if number < 1:
        return
    maxSum = number * 6
    probabilities = [0] * (6 * number - number + 1)

    probability(number, probabilities)

    sumProb = sum(probabilities)
    for i in range(number, maxSum + 1):
        print("{0}:{1}".format(i, probabilities[i - number] / sumProb))


def probability(number, prob):
    for i in range(1, 6 + 1):
        prob_recursive(number, number, i, prob)


def prob_recursive(original, current, sum, prob):
    if current == 1:
        prob[sum - original] += 1
    else:
        for i in range(1, 6 + 1):
            prob_recursive(original, current - 1, i + sum, prob)


# Method 2
def printProbability_iterative(number):
    if number < 1:
        return
    prob = [0] * 2
    prob[0] = [0] * (6 * number + 1)
    prob[1] = [0] * (6 * number + 1)

    flag = 0

    for i in range(1, 6 + 1):
        prob[flag][i] = 1

    for k in range(2, number + 1):
        for i in range(k):
            prob[1 - flag][i] = 0
        for i in range(k, k * 6 + 1):
            prob[1 - flag][i] = 0
            for j in range(1, i + 1):
                if j > 6:
                    break
                prob[1 - flag][i] += prob[flag][i - j]
        flag = 1 - flag

    probabilities = prob[flag]
    sumProb = sum(probabilities)
    for i in range(number, 6 * number + 1):
        print("{0}:{1}".format(i, probabilities[i] / sumProb))


# test
print("Method 1:")
printProbability(2)
print("Method 2:")
printProbability_iterative(2)