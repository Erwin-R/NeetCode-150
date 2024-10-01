"""
Problem: 
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.

Test Cases
    Example 1:
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").
    Example 2:
        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false
"""

#Time: O(n) since we are only making one pass through the count array and through len(s2)
#Time: O(26) since are only storing at max letters in alphabet

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #checking to see if s1 is in s2
        #we could keep track of it by keeping count of characters from s1 and returning true if all values in map are 0 
        #we can adjust our window sized based on if the current character we are at is in string 1 or not

        if len(s1) > len(s2): return False

        countS1, countS2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord("a")] += 1
            countS2[ord(s2[i]) - ord("a")] += 1

        matches = 0 
        for i in range(26): #since there can only be a total of 26 matches (only 26 letters in alphabet)
            matches += (1 if countS1[i] == countS2[i] else 0)
    
        l = 0
        #we already added in the characters from the first string earlier so we start loop at
        #end of length of first string
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            #we want to calculate the index(character that we are currently at) at update its count
            index = ord(s2[r]) - ord("a")
            countS2[index] += 1 

            #after we just incremented it if we made the count equal then we can add a match
            if countS1[index] == countS2[index]: 
                matches += 1 
            #so if by incrementing the count of char at countS2 we could have possibly made the value
            #in countS2 too large (by +1) and in which case we would decrease the number of matches
            elif countS1[index] + 1 == countS2[index]: 
                matches -= 1


            #we are decrementing the count on this half since we are moving our window to the right and 
            #have to remove the character on the left since our window is of fixed size len(s1)
            index = ord(s2[l]) - ord("a")
            countS2[index] -= 1
            if countS1[index] == countS2[index]: 
                matches += 1 
            #if by decrementing the count in S2 we make the count too small compared to the count in S1 
            #then we decrement number of matches
            elif countS1[index] - 1 == countS2[index]:
                matches -= 1

            #we want to increment left at each iteration since we want to keep fixed size of window
            l += 1

        return matches == 26
