"""
Problem:
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Test Cases:
    Example 1:
        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

    Example 2:
        Input: n = 1
        Output: [["Q"]]
"""

# Time: O(n!) 
# Space: O(n^2) where the space is the board 


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Queens can go in any direction (horizontal, vertical, diagonal)
        # Therefore there can't be another queen in any of the other paths of this

        # Create sets to track queens in vertical/diagonal plane
        col = set()
        posDiag = set()
        negDiag = set()

        # Create n x n board and result arr
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # Skip if we already have a queen in the plane
                if c in col or (r + c) in posDiag or (r - c) in negDiag: 
                    continue

                # Add Q to current board position
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                board[r][c] = "Q"
                backtrack(r + 1)
                
                # Backtrack and remove Q from board position
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)

        return res