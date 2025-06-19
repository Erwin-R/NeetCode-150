"""
Problem: 
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Test Cases:
    Example 1:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Example 2:
        Input: nums = [0,1]
        Output: [[0,1],[1,0]]
    Example 3:
        Input: nums = [1]
        Output: [[1]]
"""


"""
If the number of elements we are provided is n, then at each element, we have n! permutations.
However, inside each for loop, in both the solutions, we have have another for loop that runs from 
0 to each permutation's length, which is nbecause we are using all of the elements. n*n=n^2 
As a result, we get n^2 * n! which results in O(n^2 * n!)
""" 


#Iterative Solution
# Time: O(n^2 * n!)
# Space: O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums: 
            nextPerms = []
            for p in perms: #going through each permutation array
                for i in range(len(p) + 1): #going through each index in permutation to insert
                    pCopy = p.copy()
                    pCopy.insert(i, n)  #inserting num at "i"th index
                    nextPerms.append(pCopy)
            perms = nextPerms
        return perms

#Recursive Solution: 
# Time: O(n^2 * n!)
# Space: O(n)
def permutationsRecursive(nums):
    return helper(0, nums)

def helper(i, nums):
    if i == len(nums):
        return [[]]

    resPerms = []
    perms = helper(i + 1, nums)
    for p in perms:
        for j in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    return resPerms