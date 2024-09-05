"""
Problem:
    Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Test Cases: 
    Example 1:
        Input: heights = [2,1,5,6,2,3]
        Output: 10
        Explanation: The above is a histogram where width of each bar is 1.
        The largest rectangle is shown in the red area, which has an area = 10 units.
    Example 2:
        Input: heights = [2,4]
        Output: 4
"""

#Time: O(n) where n is the size of the heights array   
#Space: O(n) where n is the size of the stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                #pop from stack bc we know that current rectangle cannot flow over since curr height is smaller
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start,h))

        #Leftover values in stack, we know that leftover values are heights that flow to end of array
        #width is length of array - start index of value
        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea