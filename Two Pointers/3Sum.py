"""
Problem: 
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

Test Cases: 
    Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
    Example 2:
        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.
    Example 3:
        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.
"""

#Time: O(nlog(n) + n^2) -> O(n^2)
#nlog(n) to sort and n to iterate through arrray
#Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort Array and use knowledge of 2sum II to help solve this

        #create result array
        res = []
        #sort the input array
        nums.sort()

        #Enumerate allows us to get value and index
        for i, a in enumerate(nums):
            #if index > 0 and value is the same as the previous index then we continue
            #ensures that we have unique triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            #using principle of 2sum II to get to our target of 0
            L, R = i + 1, len(nums) - 1
            while L < R: 
                threeSum = a + nums[L] + nums[R]
                #if sum is too big then we decrease R(to get smaller sum)
                if threeSum > 0: 
                    R -= 1
                #if sum too small then we increase L (to get bigger sum)
                elif threeSum < 0:
                    L += 1
                #if triplit equals 0 then we append the triplet to our array
                else: 
                    res.append([a, nums[L], nums[R]]) 
                    #since we computed the triplet we want to move left pointer so
                    #we dont compute the same sum
                    L += 1
                    #we verify that nums[L] is still not the same as the previous value
                    #by increasing it
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        
        return res
