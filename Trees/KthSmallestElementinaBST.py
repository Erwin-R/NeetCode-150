"""
Problem: 
    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Test Cases: 
    Example 1:
        Input: root = [3,1,4,null,2], k = 1
        Output: 1
    Example 2:
        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3
"""

#Time: O(n) where n is the number of nodes
#Space: O(n) where n is the height of the tree

#DFS SOLUTION: 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST so left has smaller values, right has bigger values

        def dfs(node, nodeArr): 
            if not node:
                return nodeArr
            
            dfs(node.left, nodeArr)
            nodeArr.append(node.val)
            dfs(node.right, nodeArr)
            
            return nodeArr

        nodes = dfs(root, [])

        return nodes[k - 1]