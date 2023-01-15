"""
https://leetcode.com/problems/two-sum/
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = dict()
        for i,v in enumerate(nums):
            sec_value = target - v
            if sec_value in data:
                return [data[sec_value], i]
            else:
                data[v] = i