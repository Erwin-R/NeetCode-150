"""
Problem: 
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Test Cases: 
    Example 1:
        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
    
    Example 2:
        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
"""

# Memoization Solution
# Time: O(n)
# Space: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def count(currStep):
            if currStep > n:
                return 0

            if currStep in cache:
                return cache[currStep]

            if currStep == n:
                return 1

            cache[currStep] = count(currStep + 1) + count(currStep + 2)

            return cache[currStep]

        return count(0)