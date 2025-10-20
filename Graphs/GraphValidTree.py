"""
Problem: 
    You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] 
    indicates that there is an undirected edge between nodes ai and bi in the graph.

    Return true if the edges of the given graph make up a valid tree, and false otherwise.

Test Cases:
    Example 1:
        Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
        Output: true
    Example 2:
        Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
        Output: false
"""

# Time: O(V + E)
# Space: O(V + E)
# Where V is the number of nodes and E is the number of edges 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}

        # Create undirected graph adjacency list
        for src, dst in edges: 
            adj[src].append(dst)
            adj[dst].append(src)

        visit = set()

        # DFS each node and keep track of prev visited node
        def dfs(node, prev): 
            if node in visit: 
                return False

            visit.add(node)

            for neighbor in adj[node]: 
                # This helps us eliminate false positives since 
                # graph is undirected and can go back to parent
                if neighbor == prev:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)