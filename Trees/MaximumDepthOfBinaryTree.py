"""
Problem: 
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Test Cases: 
    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3
    Example 2:
        Input: root = [1,null,2]
        Output: 2
"""

#DFS SOLUTION

#Time: O(n) where n number of nodes in tree
#Space: O(n) where n is the height of the tree(depth)
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #compare the left and right side of the tree, do inorder traversal

        if not root:
            return 0

        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)

        return max(left, right)