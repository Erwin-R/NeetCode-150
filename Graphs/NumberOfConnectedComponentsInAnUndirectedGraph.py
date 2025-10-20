"""
Problem: 
    You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an 
    edge between ai and bi in the graph.

    Return the number of connected components in the graph.

Test Cases:
    Example 1:
        Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        Output: 2

    Example 2:
        Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
        Output: 1
"""

# Time: O(V + E)
# Space: O(V + E)
# Where V is the number of nodes and E is the number of edges 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build our Adjacency list
        graphMap = {i: [] for i in range(n)}

        for n1, n2 in edges: 
            graphMap[n1].append(n2)
            graphMap[n2].append(n1)

        # Step 2: Create our graph traversal
        res = 0
        visit = set()

        def dfs(i, visit): 
            if i in visit:
                return

            # Add visited nodes in visit set
            visit.add(i)

            for neighbor in graphMap[i]:       
                dfs(neighbor, visit)

        # Check all nodes and traverse down graph
        for i in range(n):             
            if i not in visit:
                dfs(i, visit)
                res += 1
        
        return res
            