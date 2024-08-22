"""
Problem: 
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
    
Test Cases: 
    Example 1:
        Input: s = "()"
        Output: true
    
    Example 2:
        Input: s = "()[]{}"
        Output: true

    Example 3:
        Input: s = "(]"
        Output: false
"""

#Time: O(n) where n is the length of the string
#Space: O(1) even in solution we use map, map will always have size of 3 parenthesis

#Solution 1: 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(" , "]" : "[", "}" : "{" }

        for c in s: 
            if c in closeToOpen: #checks key in map (only adding closed brackets to map)
                if stack and stack[-1] == closeToOpen[c]: #if brackets match
                    stack.pop()
                else:  #if brackets dont match
                    return False
            else: #only pushing open parenthesis in stack
                stack.append(c)
        
        return True if not stack else False

#Solution 2: 
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif i == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif i == ")" and stack and stack[-1] == "(":
                stack.pop()
            else: 
                stack.append(i)


        return len(stack) == 0