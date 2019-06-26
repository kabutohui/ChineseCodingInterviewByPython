# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目一】：
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变，为简单起见，标点符号和普通字符一样处理。如输入I am a student. 输出：student. a am I。

【题目二】：
字符串的左旋操作是将字符串前面的若干个字符串转移到字符串的尾部，如输入"abcdefg"和数字2，输出结果为"cdefgab"。

【解题思路】：
题目一： 在python中，可以先将句子按空格进行划分，再反序输出即可。通用解法是先整体翻转，然后再将每个单词翻转回来。 
题目二： 在python中，可以利用list切片来进行反转。通用解法是先反转前面n个字符，再反转后面的字符，最后总体进行反转。
'''


# Question 1 - Method  1
def reverseSentence_python(sentence):
    if not sentence:
        return
    s = sentence.split(" ")

    res = ""
    for i in range(len(s) - 1, 0, -1):
        res += s[i]
        res += " "
    res += s[0]

    return res


# Question 1 - Method 2
def reverse(sentence, start, end):
    if not sentence or start > end:
        return sentence
    while start <= end:
        temp = sentence[start]
        sentence[start] = sentence[end]
        sentence[end] = temp

        start += 1;
        end -= 1;

    return sentence


def reverseSentence_common(sentence):
    if not sentence:
        return
    sentence = list(sentence)
    start, end = 0, len(sentence) - 1
    # reverse whole sentence
    sentence = reverse(sentence, start, end)

    start, end = 0, 0
    while end < len(sentence):
        if sentence[end] != " ":
            end += 1
        else:
            sentence = reverse(sentence, start, end - 1)
            start = end = end + 1

    return "".join(sentence)


# Question 2 - Method 1
def leftRotateString_python(sentence, n):
    if not sentence or n > len(sentence):
        return
    sentence = sentence[n:] + sentence[:n]
    return sentence


def leftRotateString_common(sentence, n):
    if not sentence or n > len(sentence):
        return

    if n == 0:
        return sentence

    sentence = list(sentence)

    # reverse the first n characters
    sentence = reverse(sentence, 0, n - 1)
    # reverse the last characters
    sentence = reverse(sentence, n, len(sentence) - 1)
    # reverse the whole sentence
    sentence = reverse(sentence, 0, len(sentence) - 1)

    return "".join(sentence)


# test
sentence = "I am a student."
print("Q1_Pyhton:", reverseSentence_python(sentence))
print("Q1_Common:", reverseSentence_common(sentence))
sentence = "abcdefg"
print("Q2_Pyhton:", leftRotateString_python(sentence, 7))
print("Q2_Common:", leftRotateString_common(sentence, 7))