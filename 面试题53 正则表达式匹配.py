# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请实现一个函数用来匹配包含'，'和'*'的正则表达式。模式中的任意字符'.'表示任意一个字符，而‘*’表示他前面的字符可以出现任意次（含0次）。在本题中匹配是指字符串的所有字符匹配整个模式。如"aaa"匹配"a.a"和"ab*ac*a"但是与"aa.a"和"ab*a"均不匹配。

【解题思路】：

如果字符串的字符是ch，而模式中的字符也是ch或者“.”,则两者匹配；
如果模式中的第二字符是“*”:
a. 模式跳过两个字符，表示忽略*；
b. 模式跳过两个字符，输入字符进入下一个字符，表示重复一次*前面的字符；
c. 模式不变，输入字符进入下一个字符，表示重复n次*前面的字符。
最后返回这三者结果的或。
'''


def match(string, pattern):
    if string == None or pattern == None:
        return False
    return matchCore(string, pattern)


def matchCore(string, pattern):
    if len(string) == 0 and len(pattern) == 0:
        return True
    if len(string) != 0 and len(pattern) == 0:
        return False

    if len(pattern) > 1 and pattern[1] == "*":
        if len(string) > 0 and pattern[0] == string[0] or (pattern[0] == '.' and len(string) != 0):
            return matchCore(string[1:], pattern[2:]) or matchCore(string[1:], pattern) or matchCore(string,
                                                                                                     pattern[2:])
        else:
            return matchCore(string, pattern[2:])

    if len(string) > 0 and string[0] == pattern[0] or (pattern[0] == '.' and len(string) != 0):
        return matchCore(string[1:], pattern[1:])

    return False


# test
def Test(test_name_str, test_str, pattern_str, true_result):
    result = match(test_str, pattern_str)
    if result == true_result:
        print(test_name_str, ": OK!")
    else:
        print(test_name_str, ": Failed!")


Test("Test01", "", "", True);
Test("Test02", "", ".*", True);
Test("Test03", "", ".", False);
Test("Test04", "", "c*", True);
Test("Test05", "a", ".*", True);
Test("Test06", "a", "a.", False);
Test("Test07", "a", "", False);
Test("Test08", "a", ".", True);
Test("Test09", "a", "ab*", True);
Test("Test10", "a", "ab*a", False);
Test("Test11", "aa", "aa", True);
Test("Test12", "aa", "a*", True);
Test("Test13", "aa", ".*", True);
Test("Test14", "aa", ".", False);
Test("Test15", "ab", ".*", True);
Test("Test16", "ab", ".*", True);
Test("Test17", "aaa", "aa*", True);
Test("Test18", "aaa", "aa.a", False);
Test("Test19", "aaa", "a.a", True);
Test("Test20", "aaa", ".a", False);
Test("Test21", "aaa", "a*a", True);
Test("Test22", "aaa", "ab*a", False);
Test("Test23", "aaa", "ab*ac*a", True);
Test("Test24", "aaa", "ab*a*c*a", True);
Test("Test25", "aaa", ".*", True);
Test("Test26", "aab", "c*a*b", True);
Test("Test27", "aaca", "ab*a*c*a", True);
Test("Test28", "aaba", "ab*a*c*a", False);
Test("Test29", "bbbba", ".*a*a", True);
Test("Test30", "bcbbabab", ".*a*a", False);
