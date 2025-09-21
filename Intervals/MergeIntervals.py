"""
Problem:
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the 
    non-overlapping intervals that cover all the intervals in the input.

Test Cases:
    Example 1:
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    Example 2:
        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    Example 3:
        Input: intervals = [[4,7],[1,4]]
        Output: [[1,7]]
        Explanation: Intervals [1,4] and [4,7] are considered overlapping.
"""

# Time: O(n log(n))
# Space: O(n) for output list
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        #start at index 1 since we already put the first element in output array
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else: 
                output.append([start, end])
        
        return output