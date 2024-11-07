"""
Problem: 
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Test Cases: 
    Example 1:
        Input: root = [3,4,5,1,2], subRoot = [4,1,2]
        Output: true
    Example 2:
        Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
        Output: false
"""

#Time: O(n * m) where n and m are the size of the tree and subroot respectively
#Space: O(n + m) where n and m are the height of the tree respectively

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #null subRoot can be a subtree of root
        #however subRoot cannot be a subtree if root is null
        if not subRoot: return True
        if not root: return False
        
        #if subTrees are the same then we return true
        if self.sameTree(root, subRoot):
            return True
        
        #if subTrees are not the same we recursively iterate through one side of 
        #tree and see if we can reach a value that equals root of subRoot
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):    
        if not root and not subRoot:
            return True
        # if both nodes exist and values are equal we want to recusively iterate
        # to see if tree is the same
        if root and subRoot and root.val == subRoot.val: 
            return (self.sameTree(root.left, subRoot.left) and 
            self.sameTree(root.right, subRoot.right))
        
        #if one node is is non-null and the other is null we return false
        return False