#Problem: given an array/list of strings, group the anagrams together 

#Constraints: 
    # 1. String array will always contain at least one string
    # 2. String in string array may be empty
    # 3. Strings will always be in lowercase letters 

#Edge Cases: 
    # 1. A list cannot be a key in a hashmap so make it a tuple when using it as a key

#Test Cases: 
    #Example 1:
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    # Example 2:
        # Input: strs = [""]
        # Output: [[""]]
    # Example 3:
        # Input: strs = ["a"]
        # Output: [["a"]]

#Time: O(n * m) where n is the size of the array (# of strings), 
#M is the average length of string
#Count array time is 26 but since it is a constant we dont include in time complexity

#Space: O(n) #Where n is the size of dic(hashmap)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key(letters in string) : list of strings associated with these letters in string
        res = defaultdict(list) #mapping charCount to list of Anagrams
        
        for s in strs:
            count = [0] * 26  #a .. z

            for c in s:
                count[ord(c) - ord("a")] += 1


            #in python, lists cannot by keys so we change count into a tuple which in non-mutable
            res[tuple(count)].append(s)
                    
        return res.values()
