"""
Problem:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Test Cases:
    Example 1:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
    Example 2:
        Input: n = 1
        Output: ["()"]
"""

#Time: O(k * 2^n) where k is size of each string, branching factor of 2(2 decisions to include closing or not)
#and n is height of tree(based on number of pairs given)
#Space: O(n) where n is size of combination based on pair of parenthesis 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add a clothing parenthesis if closed < open
        #valid comb if open == closed == n 

        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append( "".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res