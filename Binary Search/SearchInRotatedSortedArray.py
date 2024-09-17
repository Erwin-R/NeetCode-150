"""
Problem: 
    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity.

Test Cases: 
    Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
    Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1
    Example 3:
        Input: nums = [1], target = 0
        Output: -1
"""

#Time: O(log(n))
#Space:O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            #left sorted portion
            if nums[l] <= nums[m]:
                #actually searching in left portion of array
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #right sorted portion
            else:
                #actually searching in right portion of array
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: 
                    l = m + 1
        return -1