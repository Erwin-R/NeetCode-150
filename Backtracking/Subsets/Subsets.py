"""
Problem:
    Given an integer array nums of unique elements, return all possible subsets(the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.

Test Cases:
    Example 1:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Example 2:
        Input: nums = [0]
        Output: [[],[0]]
"""

#Time: O(n * 2^m) where n  is the size of the current set and m is the size of the tree
#Space: O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, subsets = [], []

        def dfs(i, curSet, subsets):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            #decision to include nums[i]
            curSet.append(nums[i])
            dfs(i + 1, curSet, subsets)

            #decision to not include nums[i]
            curSet.pop()
            dfs(i + 1, curSet, subsets)

        dfs(0, curSet, subsets)

        return subsets