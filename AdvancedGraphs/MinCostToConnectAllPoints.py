"""
Problem:
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the 
absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Test Cases:
    Example 1:
        Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        Output: 20
        Explanation: 
        We can connect the points as shown above to get the minimum cost of 20.
        Notice that there is a unique path between every pair of points.
    
    Example 2:
        Input: points = [[3,12],[-2,5],[-4,1]]
        Output: 18
"""

# Time: O(n^2 log(n))
# Space: O(n^2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # Adj list is point1 -> point2 in list
        adj = {i: [] for i in range(N)} # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0 # cost
        visit = set()

        minHeap = [[0, 0]] # [cost, point]

        #Stop algo once len(visit) == N
        while len(visit) < N:
            cost, n1 = heapq.heappop(minHeap)

            # Already visited shortest path to node
            if n1 in visit:
                continue
            
            # Add node to visit and increase cost
            res += cost
            visit.add(n1)
            for neiCost, nei in adj[n1]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res
