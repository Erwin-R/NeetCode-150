"""
Problem: 
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Test Cases:
    Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Example 2:
        Input: digits = ""
        Output: []
    
    Example 3:
        Input: digits = "2"
        Output: ["a","b","c"]
"""

# Time: O(n * 4^n) since we are iterating through digits and a digit may contain at most 4 characters
# Space: O(n) extra space(string) and O(n * 4^n) for output list

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Create a map for each digit and its letters, i.e {2: abc}
        # Initialize result array
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz" }   


        def dfs(i, curStr):
            # Append curStr if length == digits
            if len(curStr) == len(digits):
                res.append(curStr)
                return 

            # Check each letter in digits[i]
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c) 
        
        #Only call if digits since if digits is empty return empty string
        if digits:
            dfs(0, "")
        
        return res