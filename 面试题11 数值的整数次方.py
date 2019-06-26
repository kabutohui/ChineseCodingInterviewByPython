# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：  
实现函数double Power(double base, int exponent),求base的exponent次方。不得使用库函数，同时不需要考虑最大数问题。  

【解题思路】：  
需要考虑exponent为负数和0的情况。
'''


def Power(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1
    if base - 0.0 < 0.0000001 and base - 0.0 > -0.0000001:
        if exponent < 0:
            return "Inf"
        else:
            return 0

    result, flag = 1, 1
    if exponent > 0:
        flag = 0
    else:
        exponent = - exponent

    for i in range(exponent):
        result *= base

    if flag:
        result = 1 / result

    return result


# test
print(Power(0.0, 9))
print(Power(0.0, -10))
print(Power(-10, 3))
print(Power(-10, -2))


# more efficient
def PowerWithUnsignedExponent(base, exponent):
    if exponent == 0:
        return 0
    if exponent == 1:
        return base

    result = PowerWithUnsignedExponent(base, exponent >> 1)
    result *= result
    if exponent & 1 == 1:
        result *= base

    return result


def Power2(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1
    if base - 0.0 < 0.0000001 and base - 0.0 > -0.0000001:
        if exponent < 0:
            return "Inf"
        else:
            return 0

    result, flag = 1, 1
    if exponent > 0:
        flag = 0
    else:
        exponent = - exponent
    # use a more efficient algorithm
    result = PowerWithUnsignedExponent(base, exponent)

    if flag:
        result = 1 / result

    return result


# test
print(Power2(0.0, 9))
print(Power2(0.0, -10))
print(Power2(-10, 3))
print(Power2(-10, -2))