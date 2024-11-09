"""
Problem: 
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Test Cases: 
    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
    Example 2:
        Input: root = [1]
        Output: [[1]]
    Example 3:
        Input: root = []
        Output: []
"""

#Time: O(n) iterating through each level of tree
#Space: O(n) where n is the size of queue 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we ca do level order traversal by doing a bfs on this tree
        #create a deque where we start with root 
        # while our deque is nonempty we will add each node from left to right and add to res
        # once there are no more elements in the level we add to res

        if not root: return []

        res = []
        q = deque([root])

        while q:
            level = [] 
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)

            if level: 
                res.append(level)   
                    
        return res