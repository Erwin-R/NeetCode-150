"""
Problem: 
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    Return the minimum integer k such that she can eat all the bananas within h hours.

Test Cases: 
    Example 1:
        Input: piles = [3,6,7,11], h = 8
        Output: 4
    Example 2:
        Input: piles = [30,11,23,4,20], h = 5
        Output: 30
    Example 3:
        Input: piles = [30,11,23,4,20], h = 6
        Output: 23
"""

#Brute Force:
    #Time: O(max(P) * log(P)) where p is size of the piles array
    #Space: O(1)
class Solution1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #our upper bound is going to be the max number in the set
        #we divide each element by k until the solution adds up to h hours

        k = max(piles)

        #outer loop is checking how many banas we can eat
        for i in range(1, k + 1):
            hrs = 0 
            for p in piles: 
                hrs += math.ceil(p/i)
            if hrs <= h:
                return i
            

#Binary Search Optimized
class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #our upper bound is going to be the max number in the set
        #we can actually do a binary search to find val

        l, r = 1, max(piles)
        res = r 


        while l <= r: 
            k = (l + r) // 2
            hours = 0
            for p in piles: 
                hours += math.ceil(p/k)

            if hours <= h: 
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
    
        return res 