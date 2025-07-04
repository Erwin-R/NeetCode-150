"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
    Input: nums = [0]
    Output: [[],[0]]
"""

#Time: O(n * 2^n)
#Space: O(n * 2^n),  O(n) extra space and O(2^n) space for output list
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curSet, subsets = [], []
        
        def dfs(i, curSet, subsets):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            #decision to add nums[i]
            curSet.append(nums[i])
            dfs(i + 1, curSet, subsets)
            curSet.pop()
            
            #decision to only include one of the duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, curSet, subsets)
            

        dfs(0, curSet, subsets)

        return subsets