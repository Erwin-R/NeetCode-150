"""
Problem: 
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Test Cases: 
    Example 1:
        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.

    Example 2:
        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has the longest repeating letters, which is 4.
        There may exists other ways to achieve this answer too.
"""

#Original Solution: 
#Time: O(n) where n is size of string
#Space: O(26) since the longest map can b is 26 since only 26 letters in alphabet
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we could make an array to count the number of characters in the string in one pass
        #we would then want to take the character that occurs the most and replace characters that
        #occur less
        count = {}
        l = 0
        res = 0
        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r], 0)
            maxC = max(maxC, count[s[r]]) # Update max frequency in the current window

            # Check if the window is invalid (i.e., more than 'k' replacements needed)
            #calculating number of replacements we have to do
            while (r - l + 1) - max(count.values()) > k: 
                count[s[l]] -= 1 # Reduce frequency of the character at the left pointer
                l += 1  # Shrink the window by moving the left pointer forward
            
            res = max(res, r - l + 1)
            
        return res

#Optimized Solution: 
#Time: O(n) where n is size of string
#Space: O(26) since the longest map can b is 26 since only 26 letters in alphabet

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we could make an array to count the number of characters in the string in one pass
        #we would then want to take the character that occurs the most and replace characters that
        #occur less
        count = {}
        l = 0
        res = 0
        maxC = 0
        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r], 0)
            maxC = max(maxC, count[s[r]]) # Update max frequency in the current window

            # Check if the window is invalid (i.e., more than 'k' replacements needed)
            if (r - l + 1) - maxC > k: 
                count[s[l]] -= 1 # Reduce frequency of the character at the left pointer
                l += 1  # Shrink the window by moving the left pointer forward
            
            res = max(res, r - l + 1)
            
        return res