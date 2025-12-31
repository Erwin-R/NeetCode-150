"""
Problem: 
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges 
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to 
target

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible
for all the n nodes to receive the signal, return -1.

Test Cases:
    Example 1:
        Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2
    Example 2:
        Input: times = [[1,2,1]], n = 2, k = 1
        Output: 1
    Example 3:
        Input: times = [[1,2,1]], n = 2, k = 2
        Output: -1
"""

# Time: O(E log(V))
# Space: O(V + E)

# Where V is the number of vertices and E is the number of edges


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for i in range(1, n + 1):
            adjList[i] = []

        for src, dst, wgt in times:
            adjList[src].append([dst, wgt])

        visit = set()
        minHeap = [[0, k]]
        t = 0

        while minHeap: 
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit: 
                continue

            visit.add(n1)

            t = max(t, w1)

            for n2, w2 in adjList[n1]: 
                if n2 not in visit:
                    heapq.heappush(minHeap, [w2 + w1, n2])

        return t if len(visit) == n else -1
