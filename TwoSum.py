# coding:utf-8
# author :yxf

'''
question1:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
'''

class Two_Sum(object):
    def twosum(self, numlist, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if len(numlist) < 2:
            return '您输入的数组格式不正确，请确保长度大于2'
        else:
            start = 0
            end = len(numlist) - 1
            while end > start:
                sum = numlist[start] + numlist[end]
                if sum == target:
                    return [start + 1, end + 1]
                elif sum < target:
                    start += 1
                elif sum > target:
                    end -= 1
            return '没有两个数字相加能得到目标值'


















