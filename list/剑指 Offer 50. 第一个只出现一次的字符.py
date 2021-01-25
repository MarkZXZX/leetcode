'''
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_a = []
        list_b = []
        for i in range(len(s)):
            if s[i] not in list_a:
                list_a.append(s[i])
                list_b.append(1)
            else:
                list_b[list_a.index(s[i])] = 0
        if list_a == []:
            return ' '
        return list_a[list_b.index(1)] if 1 in list_b else ' '