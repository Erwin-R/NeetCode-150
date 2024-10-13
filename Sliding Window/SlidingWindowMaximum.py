"""
Problem: 
    You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
    Return the max sliding window.

Test Cases: 
    Example 1:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        Explanation: 
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
        1 [3  -1  -3] 5  3  6  7       3
        1  3 [-1  -3  5] 3  6  7       5
        1  3  -1 [-3  5  3] 6  7       5
        1  3  -1  -3 [5  3  6] 7       6
        1  3  -1  -3  5 [3  6  7]      7
    Example 2:
        Input: nums = [1], k = 1
        Output: [1]
"""

#Time: O(n) as we are making one pass through nums array
#Space: O(n) where n is the size of the deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #start popping from left if out of bounds
            if l > q[0]: 
                q.popleft()

            #it wont hit this line until window is size k 
            if (r + 1) >= k:
                #maximum is left most position in queue
                res.append(nums[q[0]])

                #only increment left once window size is too large
                l += 1

            r += 1

        return res
