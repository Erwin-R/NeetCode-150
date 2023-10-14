"""
Problem:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order.
"""

#Solution #1 (Brute Force)
#Time: O(n^2) have to iterate over array for each index(iterating over array more than once)
#Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#Solution 2 (One Pass Solution)
#Time: O(n)
#Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {} # val : index
        print(map)

        #enumerate allows you to get index and val of array
        for i, n in enumerate(nums): 
            diff = target - n
            if diff in map:
                return [map[diff], i]

            map[n] = i
