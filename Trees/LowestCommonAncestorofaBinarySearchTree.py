"""
Problem: 
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Test Cases: 
    Example 1:
        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        Output: 6
        Explanation: The LCA of nodes 2 and 8 is 6.
    Example 2:
        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
        Output: 2
        Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
    Example 3:
        Input: root = [2,1], p = 2, q = 1
        Output: 2
"""

# Time: O(log(n)) since we will only be going through half the nodes (small nodes on left and large nodes on right)
# Worst case the time will be O(h) where h is the height of the tree
# Space: O(1)

#ITERATION SOLUTION
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root 

        while curr: 
            if p.val > curr.val and q.val > curr.val: 
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else: 
                return curr
            

#RECURSIVE SOLUTION
#Time: O(n) Worst case
#Space: O(1)
class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root