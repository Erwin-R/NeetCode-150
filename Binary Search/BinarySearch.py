"""
Problem: 
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.

Test Cases: 

    Example 1:
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        Explanation: 9 exists in nums and its index is 4
    
    Example 2:
        Input: nums = [-1,0,3,5,9,12], target = 2
        Output: -1
        Explanation: 2 does not exist in nums so return -1
"""

#Time: O(log(n)) since we are splitting the array with each iteration 
#Space:O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            p = (r + l) // 2

            if nums[p] < target: 
                l = p + 1 
            elif nums[p] > target:
                r = p - 1
            else: 
                return p
        
        return -1