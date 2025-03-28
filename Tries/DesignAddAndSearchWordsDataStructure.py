"""
Problem: 
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Test Cases: 
Example:
    Input:
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output:
        [null,null,null,null,false,true,true,true]

    Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True

"""

#Time: O(n) for addword(), O(n) for search
#Space: O(t + n)

#Where n is the length of the string and t is the total number of TrieNodes created in the Trie.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word: 
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True


    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)): 
                c = word[i]
                if c == ".": 
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.word

        return dfs(0, self.root)