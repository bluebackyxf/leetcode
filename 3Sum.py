# coding:utf-8
# author:yxf
# 2016-10-14

'''
question2: 3sum
Given an array S of n integers, are there elements a, b, c in S such that a +
b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''


# 解法1
'''
思路：首先对列表进行排序，之后从第一位，第二位及最后一位相加开始计算，
如果符合条件，则放入新列表中，如果不符合条件，>0则end-1,<0则start+1,
若符合条件，则start+1,end-1。
'''
class Solution():
    def threeSum(self, list):
        '''
        :param list:
        :return:tuple
        '''
        if len(list) < 3:
            return []
        else:
            totallist = []
            sortedlist = sorted(list)
            print sortedlist
            for i in range(0, len(list)-2):
                start = i + 1
                end = len(list) - 1
                while start < end:
                    totalsum = sortedlist[i] + sortedlist[start] + sortedlist[end]
                    if totalsum == 0:
                        newlist = [sortedlist[i], sortedlist[start], sortedlist[end]]
                        totallist.append(newlist)
                        start += 1
                        end -= 1
                    elif totalsum < 0:
                        start += 1
                    elif totalsum > 0:
                        end -= 1
            return totallist

    def cleanlist(self,list):
        '''

        :param list of list:
        :return: list of list
        '''
        newlist = []
        for i in list:
            if i not in newlist:
                newlist.append(i)
        return newlist


if __name__ == '__main__':
    solution = Solution()
    sol2 = solution.threeSum([-1,0,1,2,-1,-4])
    print  solution.cleanlist(sol2)