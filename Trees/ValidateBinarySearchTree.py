"""
Problem: 
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the node's key.
        - The right subtree of a node contains only nodes with keys greater than the node's key.
        - Both the left and right subtrees must also be binary search trees.

Test Cases: 
    Example 1:
        Input: root = [2,1,3]
        Output: true
    Example 2:
        Input: root = [5,1,4,null,null,3,6]
        Output: false
        Explanation: The root node's value is 5 but its right child's value is 4.
"""

#Time: O(n) where n is the the number of nodes, since we are checking both sides of the BST
#Space: O(n) where n is the height of the tree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):
            if not node: 
                return True
            
            #has to be less than or greater than, CANNOT BE EQUAL
            if not (node.val > left and node.val < right): 
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

            
        return dfs(root, float("-inf"), float("inf"))