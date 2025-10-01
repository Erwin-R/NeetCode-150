"""
Problem:
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.

Test Cases:
    Example 1:
        Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]
        Output: 1
    
    Example 2:
        Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
        Output: 3
"""

# DFS Solution
# Time: O(m * n)
# Space: O(m * n)

class Solution1:
    def numIslands1(self, grid: List[List[str]]) -> int:
        # Create a set to store cells visit so far
        # Start at [0,0] and recursively check for cells with "1"
        # Convert all cells with 1 to 0 and once we come back all the way to original call 
        # then we can increment number of islands

        row, col = len(grid), len(grid[0])
        islands = 0
        visit = set() # (row, col)

        # Return true or false depending on if we hit a 1 or not 
        def dfs(r, c): 
            # Base Case 1: Out of bounds, (r,c) in visit, or [r][c] == 0
            if (r < 0 or c < 0 or r >= row
                or c >= col
                or (r,c) in visit
                or grid[r][c] == "0"):
                return

            grid[r][c] = "0"
            

            # Add tuple to set and then move to next cell
            visit.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1) 
            dfs(r, c - 1)

        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1": 
                    dfs(r, c)
                    islands += 1 

        return islands
    

# BFS Solution
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and 
                        grid[r][c] == "1" and (r,c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands