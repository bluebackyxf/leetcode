# coding:utf-8
# author:yxf
# 2016-10-16

'''
question4: Longest Substring
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lista = []
        totallist = []
        item = list(s)
        for i in item:
            if i not in lista:
                lista.append(i)
            else:
                totallist.append(lista)
                lista = []
                lista.append(i)
        totallist.append(lista)
        return totallist

    def cleanlist(self, totallist):
        '''
        :param list of list:
        :return: int
        '''
        length = []
        for i in totallist:
            newlength = len(i)
            length.append(newlength)
        maxlength = max(length)
        return maxlength


if __name__ == "__main__":
    solution = Solution()
    sol2 = solution.lengthOfLongestSubstring("accdbe")
    print sol2
    solution = solution.cleanlist(sol2)
    print solution