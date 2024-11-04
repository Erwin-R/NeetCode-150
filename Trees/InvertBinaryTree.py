"""
Problem:
    Given the root of a binary tree, invert the tree, and return its root.

Test Cases: 
    Example 1:
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
    Example 2:
        Input: root = [2,1,3]
        Output: [2,3,1]
    Example 3:
        Input: root = []
        Output: []
"""

#Time: O(n) since we are visiting every node in the tree (size of tree)
#Space: O(h) where h is the height of the tree