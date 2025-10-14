"""
Problem: 
    You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    Connect: A cell is connected to adjacent cells horizontally or vertically.
    Region: To form a region connect every 'O' cell.
    Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
    
    To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Test Cases: 
    Example 1:
        Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        Explanation:
        In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

    Example 2:
        Input: board = [["X"]]
        Output: [["X"]]
"""

# Time: O(n * m)
# Space: O(n * m)

# Where n is the number of rows and m is the number of columns

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c] != "O"): 
                return

            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. (DFS) Capture Unsurrounded regions ("O" on the border -> T)
        for r in range(ROWS): 
            for c in range(COLS): 
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    dfs(r, c)

        # 2. Capture Surrounded Regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS): 
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS): 
                if board[r][c] == "T":
                    board[r][c] = "O"
