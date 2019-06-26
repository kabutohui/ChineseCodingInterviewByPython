# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请实现一个字符串用来判断字符串是否包含数值（包括整数和小数）。
如字符串“+100”， “5e2”， “-123”， “3.1416”以及“-1E-16”都表示数值；
如字符串“12e”，“1a3.14”，“1.2.3”，“+-5”，“12e+5.4”都不是。

【解题思路】：
表示数值的字符串遵循以下规则：
[sign]integral−digits[.[fractional−digits]][e|E[sign]exponential−digits]
 
其中：

[] 中的部分表示可有可无的部分；
integral-digits，fractional-digits，exponential-digits表示n个0-9之间的数字；
[sign]表示可有可无的正负号；
e|E表示10的n次方。
'''


def isNumeric(string: str) -> bool:
    if not string:
        return False
    if len(string) == 0:
        return False

    index, length = 0, len(string)
    flag = False
    # scan the first character, is the [sign]?
    if string[index] == "+" or string[index] == "-":
        index += 1
    if not string[index].isdigit():
        return False
    if index == length:
        return False

    # scan the integral-digits
    index = scan(string, index)

    if index == length - 1:
        if string[index].isdigit() or string[index] == '.':
            return True
        else:
            return False

    # scan the "."
    if string[index] == '.':
        index += 1
        if index < length - 1:
            # scan the digit behind the '.'
            index = scan(string, index)
            if index == length - 1 and string[index].isdigit():
                return True
        else:
            return True
            # scan the e|E
    if string[index] == "e" or string[index] == "E":
        index += 1
        if index <= length - 1:
            # scan the [sign] behind the e|E
            if string[index] == "+" or string[index] == "-":
                index += 1
            # scan the digit behind the e|E
            index = scan(string, index)
            if index == length - 1 and string[index].isdigit():
                return True
            else:
                return False
        else:
            return False

    return False


def scan(string, index):
    for i in range(index, len(string)):
        if not string[i].isdigit():
            break
    return i


# test
def Test(test_name_str, string, true_resulr):
    res = isNumeric(string)
    if res == true_resulr:
        print(test_name_str, ": OK!")
    else:
        print(test_name_str, ": Failed!")


Test("Test1", "100", True);
Test("Test2", "123.45e+6", True);  # false
Test("Test3", "+500", True);
Test("Test4", "5e2", True);  # false
Test("Test5", "3.1416", True);
Test("Test6", "600.", True);
Test("Test7", "-.123", False);
Test("Test8", "-1E-16", True);
Test("Test9", "1.79769313486232E+308", True);

Test("Test10", "12e", False);
Test("Test11", "1a3.14", False);
Test("Test12", "1+23", False);
Test("Test13", "1.2.3", False);
Test("Test14", "+-5", False);
Test("Test15", "12e+5.4", False);
Test("Test16", ".", False);  # false
Test("Test17", ".e1", False);
Test("Test18", "+.", False);  # false
