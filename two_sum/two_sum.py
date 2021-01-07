"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
#Link : https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        if target >= pow(-10 , 9) and target <= pow(10,9):
            if len(nums) >= 2 and len(nums) <= pow(10,3):
                total = []
                for fnum in range(0, len(nums) + 1):
                    if nums[fnum] <= pow(10,9) and nums[fnum] >= pow(-10 , 9):
                        for snum in range(fnum+1 , len(nums)):
                            if nums[fnum] + nums[snum] == target :
                                total.append(fnum)
                                total.append(snum)
                                return total
                            else:
                                continue

sol = Solution()
print(sol.twoSum([3,3],  6))

#Submit result : 
"""
Runtime: 52 ms, faster than 32.95% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 53.36% of Python3 online submissions for Two Sum.

"""