"""
Problem: 
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Test Cases: 
    Example 1:
        Input: root = [1,2,3,null,5,null,4]
        Output: [1,3,4]
    Example 2:
        Input: root = [1,null,3]
        Output: [1,3]
    Example 3:
        Input: root = []
        Output: []
"""

#Time: O(n)
#Space: O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we want to do BFS on this tree, and for each level, as we add the nodes we want to 
        #keep popping until we reach the last node in the level

        if not root: return []
        
        res = []
        q = deque([root])

        while q: 
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node             
                    q.append(node.left)
                    q.append(node.right)
            if rightSide: 
                res.append(rightSide.val)
        
        return res
