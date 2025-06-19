"""
Problem: 
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Test Cases: 
Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]
Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]
"""

#Time: O(n * 2^n) where n is size of array/comb 
#Space: O(n) space in memory due to recursion

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curComb, res = [], []
        curSum = 0
        candidates.sort()

        def dfs(i, curComb, curSum):
            if curSum == target:
                res.append(curComb.copy())
                return
            if i >= len(candidates) or curSum > target:
                return

            #include candidates[i]
            curComb.append(candidates[i])
            dfs(i + 1, curComb, curSum  + candidates[i])

            #skip candidates[i]
            curComb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: #skipping duplicate nums
                i += 1
            dfs(i + 1, curComb, curSum)



        dfs(0, curComb, curSum)

        return res