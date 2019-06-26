# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个正整数数组，把数组中所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
如输入{3， 32， 321}，最小的拼接数为321323。

【解题思路】：
思路一： 使用全排列来做，找出最小的值即可；
思路二： 《剑指offer》---把数组排成最小的数
大致思路：
（1）我们可以先思考只有两个数字的情况： [3,32] ，可以看出来 332>323 因此需要把数组改变为 [32,3] ；
（2）对于有三个数字的情况： [3,32,321] 我们两两进行比较， 332>323 于是，将 3 与 32 交换位置变成 [32,3,321] 而 3321>3213 于是将 3 与 321 继续交换位置到 [32,321,3] ；接着我们继续使用 32 进行比较，由于 32321>32132 将 32与321 进行位置交换为 [321,32,3] 此时，将数组链接起来变成 321323 即为最小的数。
具体思路：
（1）先将数字列表转化成字符串链表，这样便于在一个字符串后面直接加上另外一个字符串。也就是 "3"+"321"="3321" 。
（2）构造一个比较函数，当 str1+str2>str2+str1 时我们认为字符串 str1>str2 。
（3）将字符串列表按照比较函数的规定进行冒泡排序（或其它方法排序），将定义为”大”的字符串放到最后。而”小”的字符串放在前面。最后将字符串列表链接起来，便是所求。
'''


# define the compare function
def compare(str1, str2):
    combine1 = str1 + str2
    combine2 = str2 + str1
    return combine1 > combine2


def printMinNumber(nums):
    if not nums:
        return
    # convert to string
    nums = [str(i) for i in nums]

    # use bubble sort
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if compare(nums[j], nums[j + 1]):
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return "".join(nums)


nums = [32, 32, 321]
nums = [121, 57, 101]
printMinNumber(nums)