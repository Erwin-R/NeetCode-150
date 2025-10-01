"""
Problem: 
    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
    You may assume all four edges of the grid are surrounded by water.
    The area of an island is the number of cells with a value 1 in the island.
    Return the maximum area of an island in grid. If there is no island, return 0.

Test Cases:
    Example 1:
        Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,1,1,0,0,0],
                        [0,1,1,0,1,0,0,0,0,0,0,0,0],
                        [0,1,0,0,1,1,0,0,1,0,1,0,0],
                        [0,1,0,0,1,1,0,0,1,1,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1,1,1,0,0,0],
                        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Output: 6
        Explanation: The answer is not 11, because the island must be connected 4-directionally.
        
    Example 2:
        Input: grid = [[0,0,0,0,0,0,0,0]]
        Output: 0
"""

# Time: O(n * m)
# Space: O(n * m)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Set variables needed to traverse
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        # DFS search
        def dfs(r, c): 
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or (r, c) in visit or
                grid[r][c] == 0):
                return 0
            

            visit.add((r, c))

            return (1 + dfs(r + 1, c) + 
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1)) 

        # Traverse through grid        
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, dfs(r, c))


        return maxArea
