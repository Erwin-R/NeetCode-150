"""
Problem: 
    Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
    return the minimum number of conference rooms required.

Test Cases: 
    Example 1:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2

    Example 2:
        Input: intervals = [[7,10],[2,4]]
        Output: 1
"""

# Time: O(n log(n))
# Space: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # Create start/end array and sort by start/end vals
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        # Create count variables
        res, count = 0, 0

        # Create pointers for start/end array
        s, e = 0, 0

        while s < len(intervals): 
            # s < e (needing to occupy more than 1 room)
            if start[s] < end[e]:
                s += 1 
                count += 1

            # s >= e (meeting has ended, can decrease count)
            else: 
                e += 1
                count -= 1
            
            # Update res
            res = max(res, count)
        
        return res