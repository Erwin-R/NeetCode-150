"""
Problem: 
    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

Test Cases: 
    Input: 
    matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]], target = 3
    
    Output: true

    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false
"""

#Time: O(log(m * n))
#Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        #first we find the row we need to be in
        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            #this means that our target value falls within the current row
            else:
                break
        
        #This means that our pointers have crossed and we were not able to find a valid row for target
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r: 
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False