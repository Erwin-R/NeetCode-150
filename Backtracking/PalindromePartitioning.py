"""
Problem:
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Test Cases:
    Example 1:
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]

    Example 2:
        Input: s = "a"
        Output: [["a"]]
"""

#Time: O(n * 2^n)
#Space: 
#   O(n) extra space
#   O(n*2^n) space for the output list
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curSet, res = [], []


        def dfs(i):
            if i >= len(s):
                res.append(curSet.copy())
                return 

            for j in range(i, len(s)):
                if self.isPalindrome(s,i,j): 
                    curSet.append(s[i:j+1])
                    dfs(j + 1)
                    curSet.pop()


        dfs(0)

        return res
    
    def isPalindrome(self,s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1 

        return True