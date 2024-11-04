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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #preorder traversal (visit parent, then left children, then right children) and swap the children down until we get to null

        def dfs(root):
            if not root: 
                return 

            tmp = root.left
            root.left = root.right
            root.right = tmp

            dfs(root.left)
            dfs(root.right)

            return root
        
        return dfs(root)
    

class Solution:
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        #Swap children 

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root