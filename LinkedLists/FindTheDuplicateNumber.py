"""
Problem: 
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and using only constant extra space.

Test Cases: 
    Example 1:
        Input: nums = [1,3,4,2,2]
        Output: 2
    Example 2:
        Input: nums = [3,1,3,4,2]
        Output: 3
    Example 3:
        Input: nums = [3,3,3,3,3]
        Output: 3
"""

#Time: O(n) where n is the size of the array we are traversing
#Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        #1.) find the point where fast and slow meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break

        #2.) now that we are at the point where slow == fast meet, we know that the distance where the start of the cycle is from the start of the list and from the intersection point is the same 

        slow2 = 0
        # now we iterate though and increment both slow pointers until they reach the start of the cycle
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: 
                return slow