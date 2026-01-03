"""
Problem: 
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically 
by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules.
If there are multiple solutions, return any of them.

Test Cases: 
    Example 1:
        Input: words = ["wrt","wrf","er","ett","rftt"]
        Output: "wertf"

    Example 2:
        Input: words = ["z","x"]
        Output: "zx"
    
    Example 3:
        Input: words = ["z","x","z"]
        Output: ""
        Explanation: The order is invalid, so return "".
"""

# Time: O(N + V + E)
# Space: O(V + E)
# Where V is the number of unique characters, E is the number of edges
# and N is the sum of the lengths of all strings

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        #This for loop is used to build the adjacency list
        for i in range(len(words) - 1):
            #compare length of words  
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            #for words with same prefixes, for example if "apes" was sorted before "ape"
            #then we would return since it is not sorted correctly so there is no valid arrangement
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            #if words dont have the same prefix then we compare the words letter by letter
            for j in range(minLen): 
                #if letters are not the same then we know that the letter from w1 comes before letter in w2
                #only want the first differing characters
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False = visited, True = current path
        res = []

        #we will do dfs in post order traversal to make sure we reach all nodes in the correct order
        #for example if we traversed normally -> in (c <- a -> b -> c) we might reach c first 
        # even though b is supposed to go after a. Postorder dfs will give our answer in the reversed order 
        
        def dfs(char): 
            if char in visited: 
                return visited[char] 

            #want to mark characters we are currently visiting as True
            visited[char] = True

            #go through the neighbors of each character
            for neiChar in adj[char]: 
                if dfs(neiChar):
                    return True
            
            #Once we are done going through all neighbors or no neighbors mark as false
            #since char has been visited
            visited[char] = False
            res.append(char)

        for char in adj: 
            if dfs(char):
                return ""

        res.reverse()
        #joining with no spaces between letters
        return "".join(res)