"""
Find out if string T is an anagram of String S

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


#Time: O(n) iterating over strings 
#Space: O(n) hashmap is the length of strings
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Base Case: if length is different then T cannot be anagram of S
        if len(s) != len(t):
            return False
        
        #create map for both strings to keep track of characters
        sCount, tCount = {}, {}

        #Iterate through characters in strings to count number of occurences
        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0) 
            tCount[t[i]] = 1 + tCount.get(t[i], 0)

        return sCount == tCount
