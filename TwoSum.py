# coding:utf-8
# author :yxf

'''
question1:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
'''

class Solution(object):
    def twoSum(self, numlist, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if len(numlist) < 2:
            return '您输入的数组格式不正确，请确保长度大于2'
        else:
            for i in range(0, len(numlist)-2):
                start = i + 1
                while start < len(numlist)-1:
                    sum = numlist[i] + numlist[start]
                    if sum == target:
                        return [i + 1, start + 1]
                    else:
                        start += 1
                return '没有两个数字相加能得到目标值'

if __name__ == "__main__":
    solution = Solution()
    print solution.twoSum([3,2,4], 5)
















