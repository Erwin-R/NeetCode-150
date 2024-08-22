"""
Problem: 
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.

Test Cases:
    Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
        
    Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
    
"""

#Time: O(n) where n is the length of nums array/set since we are iterating through it
#Space: O(n) where n is the size of the nums array since we are putting in set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #eliminates the duplicates
        longest = 0 


        for n in numSet: 
            if (n - 1) not in numSet: # we know this is the start of sequence
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
            
        return longest