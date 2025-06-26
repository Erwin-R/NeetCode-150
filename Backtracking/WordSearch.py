"""
Problem:
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
    The same letter cell may not be used mo re than once.

Test Cases:
    Example 1:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: true

    Example 2: 
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
        Output: true

    Example 3:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
        Output: false
"""

# Time: O(m * 4^n) Where m is the number of cells in the board and n is the length of the word
# Space: O(n)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[i] != board[r][c] or 
                (r,c) in path):
                return False

            path.add((r,c))
            res =   (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))

            path.remove((r,c))
            return res

        #Run dfs on each index in the array as the starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True

        return False