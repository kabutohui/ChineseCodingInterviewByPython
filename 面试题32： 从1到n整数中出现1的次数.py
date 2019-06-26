# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个整数n，要求从1到n这n个整数的十进制表示中1出现的次数。
如输入12，则包含1的数为1， 10， 11， 12，故1出现的次数为5。

【解题思路】：
利用递归的思想：
如234：

0-4： 1的数量是1
4-34： 1的数量10+3X1=13,十位为1的数有10个，然后10位有三种取法1，2，3；只能取1，于是就有10+3X1；
34-234： 百位上是1的个数为： 10(len−1) ，然后第一位可以取1，2，后面两位都可以从0取到9，选择一个位置取1，再将剩下的位置全排列：2X2X10.
【所以1的数量为154】
这里指的注意的是：
如果最高位大于1，那么最高位为1的数量为 10len−1 ;
如果最高位等于1，那么最高位为1的数量为除去最高位的数+1，如123， 最高位为1的数有23+1=24个，即100-123。
'''


def numberOf1(nums):
    if not nums:
        return

    nums = str(nums)
    first = int(nums[0])

    length = len(nums)

    if length == 1 and first == 0:
        return 0
    if length == 1 and first > 0:
        return 1

    numFisrtDigit = 0
    if first > 1:
        numFisrtDigit = 10 ** (length - 1)
    elif first == 1:
        numFisrtDigit = int(nums[1:]) + 1

    numOtherDigits = first * (length - 1) * (10 ** (length - 2))

    numRecursive = numberOf1(nums[1:])

    return numFisrtDigit + numOtherDigits + numRecursive


numberOf1(234)