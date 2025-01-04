"""
Problem: 
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Test Cases: 
    Example 1:
        Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]

    Example 2:
        Input: board = [["a","b"],["c","d"]], words = ["abcb"]
        Output: []
"""

#Time: O(m∗n∗4∗3^t−1 +s)
#Space: O(s)

# where M is the number of rows, n is the number of columns, t is the maximum length of any word in the array words
# and s is the sum of the lengths of all the words

class TrieNode: 
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word: 
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #create root node and add the words to Trie
        root = TrieNode()
        for word in words:
            root.addWord(word)

        #Set row, cols and res/visit set. We use sets since we don't want duplicates
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        #create our backtracking function using dfs
        def dfs(r, c, node, word): 
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                (r, c) in visit or board[r][c] not in node.children):
                return

            #add current character to visited array and set the node to current character
            #add current character to word string until we reach the end of the word and then we check if
            # statement and add to result if current node is end of the word
            visit.add((r,c)) 
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord: 
                res.add(word)

            dfs(r - 1, c, node, word) 
            dfs(r + 1, c, node, word) 
            dfs(r, c - 1, node, word) 
            dfs(r, c + 1, node, word) 

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        #convert set to list
        return list(res) 