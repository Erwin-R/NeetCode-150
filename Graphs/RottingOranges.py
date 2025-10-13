"""
Problem:
    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Test Cases:
    Example 1:
        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4

    Example 2:
        Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

    Example 3:
        Input: grid = [[0,2]]
        Output: 0
        Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

# Time: O(m * n)
# Space: O(m * n)
# Where m is the number of rows and n is the number of columns


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        
        q = deque()
        fresh = 0
        time = 0

        # Add all positions with rotten oranges (Multisource BFS)
        # and count fresh oranges in matrix
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2: 
                    q.append([r, c])

                if grid[r][c] == 1:
                    fresh += 1 
        
        # Q starts with rotten orange positions so 
        # we want to make adjacent positions rotten
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                
                # Check 4 directions of current position
                for dr, dc in directions:
                    row, col = r + dr, c + dc 

                    # Skip over out of bound positions or if 
                    # position doesn't have fresh orange
                    if (row < 0 or col < 0 or row >= ROWS or 
                        col >= COLS or grid[row][col] != 1):
                        continue

                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1