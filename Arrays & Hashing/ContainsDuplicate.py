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


#Solution 2
#Although slower Time Complexity it would operate faster on larger arrays since
#we wouldnt have to iterate over entire array
#Time: O(n log(n)) 
#Time: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Sort array so duplicates are next to each other
        nums.sort()

        for i in range(len(nums) - 1):
            #Return true if adjacent numbers are the same
            if nums[i] == nums[i + 1]:
                return True        
        return False