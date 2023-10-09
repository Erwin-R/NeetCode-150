#Problem: Return True if there are duplicates in nums array and False if not

#Solution 1
#Time: O(n) *Iterating over array
#Space: O(n) *Set will be size of array in worst case
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #We use set since it can only contain unique values 
        uniqueNums = set()

        #Iterate over array and return False if n is found in set
        for n in nums:
            if n in uniqueNums: 
                return True
            uniqueNums.add(n)
        
        return False