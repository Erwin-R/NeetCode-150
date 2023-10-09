#Problem: Return True if there are duplicates in nums array and False if not

#Solution 1
#Time: O(n)
#Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()

        for n in nums:
            if n in uniqueNums: 
                return True
            uniqueNums.add(n)
        
        return False