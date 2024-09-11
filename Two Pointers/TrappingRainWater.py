"""
Problem:
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Test Cases: 
    Example 1: 
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    Example 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9
"""
#Time: O(n) where n is the size of heights array 
#Space: O(1) 

class Solution:
    def trap(self, height: List[int]) -> int:
        #technically dont need this line since we are guaranteed 1 value in array
        if not height: return 0

        L, R = 0, len(height) - 1
        leftMax, rightMax = height[L], height[R]
        amount = 0

        while L < R: 
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                #We dont have to check if amount will always be negative since difference
                #will always be positive or 0. this is because we update the leftMax before we compute amount
                amount +=  leftMax - height[L]                
            else: 
                R -= 1
                rightMax = max(rightMax, height[R])
                amount +=  rightMax - height[R]                

        return amount