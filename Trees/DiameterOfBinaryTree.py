"""
Problem: 
    Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.

Test Cases: 
    Example 1:
        Input: root = [1,2,3,4,5]
        Output: 3
        Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
    Example 2:
        Input: root = [1,2]
        Output: 1
"""

#Time: O(n) where n is the amount of nodes in the tree(traversing through all of them)
#Space: O(n) where n is the height of the tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #dfs on left and right sides and then add the levels/height
        #per level, we take the depth from the levels below

        #adding "self" makes this a member variable (instance of the solution class)
        #this makes the variable accessible inside the dfs function
        self.res = 0
        #function returns height
        def dfs(curr):
            if not curr: 
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.res