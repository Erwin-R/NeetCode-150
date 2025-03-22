"""
Problem: 
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    You may return the answer in any order.

Test Cases: 
    Example 1:
        Input: n = 4, k = 2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        Explanation: There are 4 choose 2 = 6 total combinations.
        Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

    Example 2:
        Input: n = 1, k = 1
        Output: [[1]]
        Explanation: There is 1 choose 1 = 1 total combination.
"""

#Time: O(k * 2^n) where k is the length of the combination and n is the length of the range
#Space: O(n) 

class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb, res = [], []

        def combinations(i, curComb):
            if len(curComb) >= k: 
                res.append(curComb.copy())
                return
            if i > n:
                return 

            curComb.append(i)
            combinations(i + 1, curComb)

            curComb.pop()
            combinations(i + 1, curComb)

        combinations(1, curComb)
        return res
    


#Optimized Solution: 
#Time: O(k * C(n,k)) where k is the length of the combination and n is the length of the range. 
#Space: O(n)
#In this solution we are not having to to through multiple levels in the branch
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb, res = [], []

        def combinations(i, curComb):
            if len(curComb) >= k: 
                res.append(curComb.copy())
                return
            if i > n:
                return 


            for j in range(i, n + 1):
                curComb.append(j)
                combinations(j + 1, curComb)
                curComb.pop()

        combinations(1, curComb)
        return res