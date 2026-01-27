"""
Problem: 
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there
is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, 
return -1.

Test Cases:
    Example 1: 
        Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
        Output: 700
        Explanation:
        The graph is shown above.
        The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
        Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

    Example 2: 
        Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
        Output: 200
        Explanation:
        The graph is shown above.
        The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

    Example 3: 
        Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
        Output: 500
        Explanation:
        The graph is shown above.
        The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
"""

# Time: O(n + (m * k))
# Space: O(n)
# Where n is the number of cities, m is the number of flights and k is the number of stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Keep track of prices and minimum cost (maps n nodes to index in array)
        prices = [float("inf")] * n

        # Price to get to src node is 0
        prices[src] = 0

        # We are iterating through k + 1 edges (if k was 0, we need loop to run once)
        # Doing k + 1 layers of bfs in graph
        for i in range(k + 1):
            tmpPrices = prices.copy() # Keep snapshot of current prices

            for s, d, p in flights:
                if prices[s] == float("inf"): # cant reach source node then continue
                    continue

                # Update tmpPrice if current price + p is less
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
                
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]