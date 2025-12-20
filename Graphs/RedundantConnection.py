"""
Problem: 
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different 
vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where 
edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph. Return an edge that can be removed so that the resulting
graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Test Cases:
    Example 1: 
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]
    Example 2:
        Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        Output: [1,4]
"""

# Time: O(V + E * aV)
# Space: O(V)
# Where V is the number of verties and E is the number of edges in the graph.a() is used for amortized complexity

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n): # finds root(parent) of node
            p = par[n] # store parent of n in variable p
            while p != par[p]: # while parent != grandparent

                # Sets current parent to grandparent
                par[p] = par[par[p]] # not needed but used for path compression (optimization)
                p = par[p] # iterate up tree

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # Nodes already connected, do nothing
            # Both nodes have same parent so could be a cycle
            if p1 == p2:
                return False

            # If not we add node to disjointed set (by rank/tree height)

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            # return true because we connected nodes 
            return True

        for n1, n2 in edges: 
            if not union(n1, n2):
                return [n1, n2]