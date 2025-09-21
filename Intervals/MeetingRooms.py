"""
Problem:
    Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Test Cases:
    Example 1:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: false

    Example 2:
        Input: intervals = [[7,10],[2,4]]
        Output: true
"""

# Time: O(n log(n))
# Space: O(1) or O(n) depending on the sorting algorithm
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort intervals and check for overlaps
        # if overlaps then they cannot attend all meetings, return false

        intervals.sort()

        # Non-overlap
        #   - currStart > prevEnd

        for i in range(1, len(intervals)): 
            i1 = intervals[i - 1]
            i2 = intervals[i]

            # Next meeting starts before current meeting ends
            if i2[0] < i1[1]:
                return False

        return True
