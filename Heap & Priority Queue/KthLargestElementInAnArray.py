"""
Problem: 
    Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
    By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
    Follow-up: Can you solve it without sorting?

Test Cases:
    Example 1:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5

    Example 2:
        Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4
"""

# Time: O(n log k) where n is the length of the array nums
# Space: O(k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Want to use a heap to sort the array with largest numbers at the front 
        # since we are returning kth largest (max heap)

        # Convert numbers in nums to negative numbers to track max number
        nums = [-n for n in nums]

        # Heapify nums
        heapq.heapify(nums)

        # Pop heap until we get kth largest
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        return nums[0] * -1