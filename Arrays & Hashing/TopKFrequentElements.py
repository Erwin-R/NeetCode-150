#Problem: Given an integer array "nums" and an integer "k", return the k most frequent elements. You may return the answer in any order.

#Constraints:
    # 1. Length of array nums is at least 1
    # 2. k is in the range [1, the number of unique elements in the array]
    # 3. It is guaranteed that the answer is unique

#Test Cases
    # Example 1:
        # Input: nums = [1,1,1,2,2,3], k = 2
        # Output: [1,2]
    # Example 2:
        # Input: nums = [1], k = 1
        # Output: [1]

#Time: O(n), where n is the number of unique elements (~size of input array)
#Technically O(n1 + n2) where n1 is size of input array and n2 for iterating over array per index 
#Worst case is where each element has the same number of occurences

#Space: O(n), where N is the size of the hashmap to count occurences of each value

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #num: # of occurences
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():  #[(num, # of occurences), (n, #Occ)]
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if(len(res) == k):
                return res