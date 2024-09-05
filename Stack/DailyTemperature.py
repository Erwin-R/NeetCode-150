"""
Problem: 
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
    If there is no future day for which this is possible, keep answer[i] == 0 instead.

Test Cases: 
    Example 1:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]

    Example 2:
        Input: temperatures = [30,40,50,60]
        Output: [1,1,1,0]
    
    Example 3:
        Input: temperatures = [30,60,90]
        Output: [1,1,0]
"""

#Time: O(n) where n is the length of the array
#Space: O(n) where n is the size of our stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([t, i])


        return res