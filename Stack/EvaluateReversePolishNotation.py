"""
Problem: 
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
    Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a 32-bit integer.

Test Cases: 
    Example 1:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9
    Example 2:
        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6
    Example 3:
        Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        Output: 22
        Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22
"""

#Time: O(n) where n is the size of the array
#Space: O(n) where n is the size of the stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for c in tokens: 
            if c == "+":
                numStack.append(numStack.pop() + numStack.pop())
            elif c == "-":
                n1, n2 = numStack.pop(), numStack.pop()
                numStack.append(n2 - n1)
            elif c == "*":
                numStack.append(numStack.pop() * numStack.pop())
            elif c == "/":
                n1, n2 = numStack.pop(), numStack.pop()
                numStack.append(int(n2 / n1))
            else:
                numStack.append(int(c))
        
        return numStack[-1]
