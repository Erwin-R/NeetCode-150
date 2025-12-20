"""
Problem: 
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

    - Every adjacent pair of words differs by a single letter.
    - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    - sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence 
from beginWord to endWord, or 0 if no such sequence exists.

Test Cases: 
    Example 1:
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    Example 2:
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        Output: 0
        Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

# Time: O(m^2 * n)
# Space: O(m^2 * n)
# Where n is the number of words and m is the length of the word

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Search for wordpath from beginWord to endWord and each word along the path can 
        # only differ by 1 character. Path must be made of words from wordList. beginWord does
        # not have to be in word list

        if endWord not in wordList: # No possible path if endWord not in list
            return 0

        # mapping {pattern: word} (ex. {*ot: [hot, dot, lot]})
        nei = collections.defaultdict(list)

        # Add begin word to word list
        wordList.append(beginWord)

        # Add patterns and their respective words
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])

        # Length of path
        res = 1 


        # Iterate through queue and add neighboring nodes
        while q: 
            for i in range(len(q)):
                word = q.popleft()

                # We have found shortest path 
                if word == endWord: 
                    return res

                # Else we add neighboring nodes/words (words that differ by 1 letter)
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:] # first get pattern
                    for neiWord in nei[pattern]: # then based off pattern we can see neighbors
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
                
            res += 1

        return 0