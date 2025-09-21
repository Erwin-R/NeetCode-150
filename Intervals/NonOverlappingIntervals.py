"""
Problem: 
    Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to 
    remove to make the rest of the intervals non-overlapping.

    Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Test Cases: 
    Example 1:
        Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
    
    Example 2:
        Input: intervals = [[1,2],[1,2],[1,2]]
        Output: 2
        Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

    Example 3:
        Input: intervals = [[1,2],[2,3]]
        Output: 0
        Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""

# Time: O(n log(n))
# Space: O(1) or O(n) depending on sorting algorithm

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Remove intervals that are non-overlapping and count how many
        # you need to remove

        # sort intervals by first val
        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]

        # Non-overlapping 
        #   - nextStart >= currEnd

        # Overlapping
        #   - currEnd > nextStart
        #   - currStart == nextStart  

        for start, end in intervals[1:]:
            # Not overlapping
            if start >= prevEnd:
                prevEnd = end
            else:
                # Update count and remove interval with larger end val (keep smaller end val)
                count += 1
                prevEnd = min(end, prevEnd)

        return count