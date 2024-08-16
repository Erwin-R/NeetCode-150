"""
Problem:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Test Cases: 
Example 1: 
    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

Example 2:
    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
    Since there are two 8's in the top left 3x3 sub-box, it is invalid.


"""
#Time: O(9^2) iterating through each cell in board (9 x 9)
#Space: O(9^2) size of the sudoku board(9 x 9)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #creating sets to ensure no repitions in row/col/square
        row = collections.defaultdict(set) #row : num
        column = collections.defaultdict(set) #column : num
        square = collections.defaultdict(set) #key - (r,c) : val - num ((r//3, c//3) : num)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    continue
                if (
                board[r][c] in row[r] 
                or board[r][c] in column[c] 
                or board[r][c] in square[(r//3),(c//3)]
                ):
                    return False

                row[r].add(board[r][c])
                column[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
                 

        return True