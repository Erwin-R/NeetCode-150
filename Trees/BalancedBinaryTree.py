"""
Problem:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
**** Each subtree must also be balanced

Test Cases: 
    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: true
    Example 2:
        Input: root = [1,2,2,3,3,null,null,4,4]
        Output: false
    Example 3:
        Input: root = []
        Output: true
"""

#Time: O(n) where n is amount of nodes in the tree since we are visiting all of them
#Space: O(n) where n is the height of of the tree

class Solution:
    def isBalanced1(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            #Balanced is True if...
            #if the left of right trees are not balanced then we can be sure that the parents are also not balanced
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root):
            if not root: 
                return 0

            left, right= dfs(root.left), dfs(root.right)

            if abs(left - right) > 1: 
                self.balanced = False

            return 1 + max(left, right)
        
        dfs(root)

        return self.balanced