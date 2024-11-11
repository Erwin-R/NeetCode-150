"""
Problem:
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.

Test Cases: 
    Example 1:
        Input: root = [1,2,3]
        Output: 6
        Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
    Example 2:
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""

#Time: O(n)
#Space: O(n)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node): 
            if not node: return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            #get the max val on left and right side of node
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #sum with split
            res[0] = max(res[0], node.val + leftMax + rightMax)

            #returning path without split
            return node.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]